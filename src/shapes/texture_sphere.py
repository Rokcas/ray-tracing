from src.shapes.base import BaseShape
from src.vec3 import Vec3, Rgb
from dataclasses import dataclass
import numpy as np
from src.constants import FARAWAY
import math
from PIL import Image
from src.shapes.sphere import Sphere

@dataclass
class TextureSphere(Sphere):
    texture_path: str

    def diffuseColourAt(self, M):
        # TODO
        # Get spherical polar coordinates and use them on the texture map
        R = M - self.centre

        theta = np.arccos(R.y / self.radius)
        phi = np.arctan2(R.x, R.z)

        texture = Image.open(self.texture_path)
        texture_width, texture_height = texture.size
        texture = np.array(texture.getdata()).reshape(texture_width * texture_height, 3).transpose()

        r = texture[0] / 255
        g = texture[1] / 255
        b = texture[2] / 255

        v = (theta / math.pi * texture_height).astype(int)
        u = (phi / 2 / math.pi * texture_width).astype(int)
        i = texture_width * v + u

        return Rgb(r[i], g[i], b[i])


    def polarCoordToNormal(self, theta: float, phi: float):
        y = self.radius * cos(theta)
        r = self.radius * sin(theta)
        x = r * sin(phi)
        z = r * cos(phi)

    def polarCoordAt(self, M):
        theta = np.arccos(M.y / self.radius)
        phi = np.arctan2(x, z)

        v = np.floor(theta / math.pi * texture_height)
        u = np.floor(phi / 2 / math.pi * texture_width)

