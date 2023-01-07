from dataclasses import dataclass, field

import numpy as np

from src.constants import FARAWAY
from src.shapes.base import BaseShape
from src.vec3 import Vec3
from math import sqrt

@dataclass
class Plane(BaseShape):
    normal: Vec3 = field(default_factory=lambda: Vec3(1, 0, 0))
    centre: Vec3 = field(default_factory=lambda: Vec3(0, 0, 0))

    def intersect(self, O: Vec3, D: Vec3) -> float:
        c = (self.centre - O).dot(self.normal) / D.dot(self.normal)

        return c if c >= 0 else FARAWAY


    def normalAt(self, M):
        return self.normal
