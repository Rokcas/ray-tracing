from functools import reduce
import numpy as np
from src.constants import FARAWAY
from src.vec3 import Vec3, Rgb
from dataclasses import dataclass
from src.shapes.base import BaseShape

@dataclass
class Plane(BaseShape):
    normal: Vec3
    point: Vec3  # Any point on the plane

    def intersect(self, O, D):
        N = self.normal
        distance = N.dot(self.point - O) / N.dot(D)
        return np.where(distance < 0, FARAWAY, distance)

    def normalAt(self, M):
        return self.normal

    def diffuseColourAt(self, M):
        return self.diffuse_colour
