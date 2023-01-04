from src.shapes.base import BaseShape
from src.vec3 import Vec3
from dataclasses import dataclass
import numpy as np
from src.constants import FARAWAY


@dataclass
class Sphere(BaseShape):
    centre: Vec3 = Vec3(0, 0, 0)
    radius: float = 1

    def intersect(self, O: Vec3, D: Vec3) -> float:
        b = 2 * D.dot(O - self.centre)
        c = (
            abs(self.centre)
            + abs(O)
            - 2 * self.centre.dot(O)
            - (self.radius * self.radius)
        )
        disc = (b**2) - (4 * c)

        if disc < 0:
            return FARAWAY

        sq = np.sqrt(disc)
        h0 = (-b - sq) / 2
        h1 = (-b + sq) / 2

        if min(h0, h1) > 0:
            return min(h0, h1)
        if max(h0, h1) > 0:
            return max(h0, h1)
        return FARAWAY

    def normalAt(self, M):
        return (M - self.centre) * (1.0 / self.radius)
