import math
from dataclasses import dataclass
from functools import cached_property

from PIL import Image

from src.shapes.sphere import Sphere
from src.vec3 import Rgb


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
        """Return the colour of the texture that maps to point M."""
        R = M - self.centre

        theta = math.acos(R.y / self.radius)
        phi = math.atan2(R.x, R.z)

        u = int(phi / 2 / math.pi * self.texture_width)
        v = int(theta / math.pi * self.texture_height)

        return Rgb(*self.texture[u, v]) / 255
