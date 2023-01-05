import math
from dataclasses import dataclass
from functools import cached_property

from PIL import Image

from src.shapes.sphere import Sphere
from src.vec3 import Rgb


@dataclass
class TextureSphere(Sphere):
    texture_path: str = "textures/cat.webp"

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
        # TASK 8: Change the following method to render the specified texture on the sphere.

        # You will first need to calculate the spherical polar coordinates of
        # the sphere at point M and then map them to the Cartesian coordinates
        # on the image.

        # You can get the pixel at coordinates (u, v) from the
        # texture image using the following line of code:
        Rgb(*self.texture[u, v]) / 255

        return super().diffuseColourAt(M)
