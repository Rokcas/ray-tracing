from dataclasses import dataclass

import numpy as np

from src.constants import FARAWAY
from src.shapes.base import BaseShape
from src.vec3 import Vec3


@dataclass
class Sphere(BaseShape):
    centre: Vec3 = Vec3(0, 0, 0)
    radius: float = 1

    def intersect(self, O: Vec3, D: Vec3) -> float:
        """Return the distance to the nearest intersection of the object and the ray coming from O in direction D.

        Return FARAWAY if there is no intersection.
        """

        # TASK 2: Implement this method for finding the distance to the nearest intersection
        return FARAWAY

    def normalAt(self, M):
        return (M - self.centre) * (1.0 / self.radius)
