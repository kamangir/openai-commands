from io import BytesIO
from PIL import Image
import random
import requests
import numpy as np
import abcli.logging
import logging


logger = logging.getLogger()


class Canvas(object):
    def __init__(
        self,
        canvas_width=2048,
        canvas_height=1024,
        brush_width=256,
        brush_height=256,
        verbose=False,
        demo_mode=False,
    ):
        self.verbose = verbose
        self.demo_mode = demo_mode

        self.canvas_width = canvas_width
        self.canvas_height = canvas_height

        self.image = Image.new(
            "RGB",
            (self.canvas_width, self.canvas_height),
            (0, 0, 0),
        )
        self.mask = Image.new(
            "L",
            (self.canvas_width, self.canvas_height),
            (0,),
        )

        self.brush_width = brush_width
        self.brush_height = brush_height

        self.init_cursor()

        self.horizontal_brush_move = 1
        self.vertical_brush_move = 1

    def generate(self, prompt):
        import openai

        box = (
            self.cursor[0] - self.brush_width // 2,  # left,
            self.cursor[1] - self.brush_height // 2,  # top,
            self.cursor[0] + self.brush_width // 2,  # right,
            self.cursor[1] + self.brush_height // 2,  # bottom,
        )

        image_ = self.image.crop(box)
        image_byte_stream = BytesIO()
        image_.save(image_byte_stream, format="PNG")
        image_byte_array = image_byte_stream.getvalue()

        mask_ = image_.copy().convert("RGBA")
        mask_.putalpha(self.mask.crop(box))
        mask_byte_stream = BytesIO()
        mask_.save(mask_byte_stream, format="PNG")
        mask_byte_array = mask_byte_stream.getvalue()

        response = openai.Image.create_edit(
            image=image_byte_array,
            mask=mask_byte_array,
            prompt=prompt,
            n=1,
            size=f"{self.brush_width}x{self.brush_height}",
        )

        image_url = response["data"][0]["url"]
        if self.verbose:
            logger.info(f"Canvas.generate: received {image_url}")

        response = requests.get(image_url)
        image_data = response.content
        image__ = Image.open(BytesIO(image_data))
        if self.verbose:
            logger.info(f"Canvas.generate: downloaded {image__.size}, {image__.mode}")

        self.image.paste(image__, box)
        self.mask.paste(
            Image.new(
                "L",
                (self.brush_width, self.brush_height),
                (255,),
            ),
            box,
        )

        if self.demo_mode:
            from IPython.display import display, clear_output

            clear_output(wait=True)

            image = Image.new("RGB", (3 * self.brush_width, self.brush_height))
            image.paste(image_, (0, 0))
            image.paste(mask_, (self.brush_width, 0))
            image.paste(image__, (2 * self.brush_width, 0))
            display(image)

            image = Image.new("RGB", (2 * self.canvas_width, self.canvas_height))
            image.paste(self.mask, (0, 0))
            image.paste(self.image, (self.canvas_width, 0))
            display(image)

        return self

    def init_cursor(self):
        self.cursor = (
            self.canvas_width // 2,
            self.canvas_height // 2,
        )

        if self.verbose:
            self.log()

    def move_cursor(self):
        self.cursor = (
            min(
                self.canvas_width - self.brush_width,
                max(
                    self.brush_width,
                    int(
                        random.uniform(
                            -self.horizontal_brush_move * self.brush_width,
                            self.horizontal_brush_move * self.brush_width,
                        )
                        + self.cursor[0]
                    ),
                ),
            ),
            min(
                self.canvas_height - self.brush_height,
                max(
                    self.brush_height,
                    int(
                        random.uniform(
                            -self.vertical_brush_move * self.brush_height,
                            self.vertical_brush_move * self.brush_height,
                        )
                        + self.cursor[1]
                    ),
                ),
            ),
        )

        if self.verbose:
            self.log()

        return self

    def log(self):
        logger.info(
            "Canvas: {:,}x{:,}, brush: {:,}x{:,}, @ {:,}x{:,} - {:.2f}%".format(
                self.canvas_height,
                self.canvas_width,
                self.brush_width,
                self.brush_height,
                self.cursor[1],
                self.cursor[0],
                np.array(self.mask).mean() / 255 * 100,
            )
        )
