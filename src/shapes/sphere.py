from src.shapes.base import BaseShape
from src.vec3 import Vec3
from dataclasses import dataclass
import numpy as np
from src.constants import FARAWAY

@dataclass
class Sphere(BaseShape):
    centre: Vec3
    radius: float

    def intersect(self, O, D):
        b = 2 * D.dot(O - self.centre)
        c = abs(self.centre) + abs(O) - 2 * self.centre.dot(O) - (self.radius * self.radius)
        disc = (b ** 2) - (4 * c)
        sq = np.sqrt(np.maximum(0, disc))
        h0 = (-b - sq) / 2
        h1 = (-b + sq) / 2
        h = np.where((h0 > 0) & (h0 < h1), h0, h1)
        pred = (disc > 0) & (h > 0)
        return np.where(pred, h, FARAWAY)

    def diffuseColourAt(self, M):
        return self.diffuse_colour

    def normalAt(self, M):
        return (M - self.centre) * (1. / self.radius)
