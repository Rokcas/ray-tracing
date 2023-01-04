from src.shapes.base import BaseShape
from src.vec3 import Vec3, Rgb
from dataclasses import dataclass
import numpy as np
from src.constants import FARAWAY
import math
from PIL import Image
from src.shapes.sphere import Sphere
from functools import cached_property

@dataclass
class TextureSphere(Sphere):
    texture_path: str = "cat.webp"

    @cached_property
    def texture_width(self):
        return Image.open(self.texture_path).size[0]

    @cached_property
    def texture_height(self):
        return Image.open(self.texture_path).size[1]

    @cached_property
    def texture(self):
        return Image.open(self.texture_path).load()

    def diffuseColourAt(self, M):
        R = M - self.centre

        theta = math.acos(R.y / self.radius)
        phi = math.atan2(R.x, R.z)

        texture = Image.open(self.texture_path)

        u = int(phi / 2 / math.pi * self.texture_width)
        v = int(theta / math.pi * self.texture_height)

        return Rgb(*self.texture[u, v]) / 255
