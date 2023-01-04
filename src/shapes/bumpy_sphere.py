from src.shapes.base import BaseShape
from src.vec3 import Vec3
from dataclasses import dataclass
import numpy as np
from src.constants import FARAWAY

@dataclass
class BumpySphere(Sphere):
    bump_map_path: str

    def normalAt(self, M):
        # TODO
        return (M - self.centre) * (1. / self.radius)
