import random
import numpy as np
import math
from openai_commands.logger import logger


class Brush:
    def __init__(
        self,
        canvas,
        width=256,
        height=256,
    ):
        self.width = width
        self.height = height

        self.cursor = [
            canvas.width // 2,
            canvas.height // 2,
        ]

    def move(self, canvas):
        self.cursor = [
            min(
                canvas.width - self.width,
                max(self.width, int(self.cursor[0])),
            ),
            min(
                canvas.height - self.height,
                max(self.height, int(self.cursor[1])),
            ),
        ]

        return self


class RandomWalkBrush(Brush):
    def __init__(
        self,
        canvas,
        width=256,
        height=256,
    ):
        super().__init__(canvas, width, height)

        self.horizontal_move = 1
        self.vertical_move = 1

    def move(self, canvas):
        self.cursor = [
            random.uniform(
                -self.horizontal_move * self.width,
                self.horizontal_move * self.width,
            )
            + self.cursor[0],
            random.uniform(
                -self.horizontal_move * self.height,
                self.horizontal_move * self.height,
            )
            + self.cursor[1],
        ]

        return super().move(canvas)


class TilingBrush(Brush):
    def __init__(
        self,
        canvas,
        width=256,
        height=256,
    ):
        super().__init__(canvas, width, height)

        self.ring = 0
        self.delta_angle = 2 * np.pi
        self.angle = 2 * np.pi

        self.ring_size = 0.7

        self.verbose = canvas.verbose

    def move(self, canvas):
        self.angle += self.delta_angle

        if self.angle >= 2 * np.pi - self.delta_angle / 2:
            self.ring += 1
            self.delta_angle = 2 * math.asin(1 / 2 / self.ring)
            self.angle = 0

        if self.verbose:
            logger.info(
                "TilingBrush: ring:{} @ {:.02f} deg".format(
                    self.ring, self.angle / np.pi * 180
                )
            )

        self.cursor[0] = (
            canvas.width // 2
            + self.ring * self.ring_size * math.cos(self.angle) * self.width
        )
        self.cursor[1] = (
            canvas.height // 2
            + self.ring * self.ring_size * math.sin(self.angle) * self.height
        )

        return super().move(canvas)
