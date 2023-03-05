from io import BytesIO
from PIL import Image
import random
import requests
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
    ):
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

        self.horizontal_brush_move = 0.5
        self.vertical_brush_move = 0.5

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

        mask_ = self.mask.crop(box)
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
        logger.info(f"Canvas.generate: received {image_url}")

        response = requests.get(image_url)
        image_data = response.content
        image__ = Image.open(BytesIO(image_data))
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

        return image__

    def init_cursor(self):
        self.cursor = (
            self.canvas_width // 2,
            self.canvas_height // 2,
        )
        self.log()

    def move_cursor(self):
        self.cursor = (
            min(
                self.canvas_width - self.brush_width,
                max(
                    self.brush_width,
                    int(
                        random.normalvariate(
                            0, self.horizontal_brush_move * self.brush_width
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
                        random.normalvariate(
                            0, self.vertical_brush_move * self.brush_height
                        )
                        + self.cursor[1]
                    ),
                ),
            ),
        )
        self.log()
        return self

    def log(self):
        logger.info(
            "Canvas: {:,}x{:,}, brush: {:,}x{:,}, @ {:,}x{:,}".format(
                self.canvas_height,
                self.canvas_width,
                self.brush_width,
                self.brush_height,
                self.cursor[1],
                self.cursor[0],
            )
        )
