from dataclasses import dataclass, field
from math import sqrt, atan2, isclose

from src.shapes.base import BaseShape
from src.vec3 import Rgb, Vec3
from src.constants import FARAWAY


@dataclass
class Cylinder(BaseShape):
    centre: Vec3 = field(default_factory=lambda: Vec3(0.2, 0.5, 0))
    radius: float = 0.6
    height: float = 0.5
    normal: Vec3 = field(default_factory=lambda: Vec3(0, 0, 1))

    def intersectTop(self, O: Vec3, D: Vec3) -> float:
        Cs = self.centre + self.normal * self.height
        c = self.normal.dot(Cs - O) / self.normal.dot(D)
        if c > 0 and (O + D * c - Cs).length() <= self.radius:
            return c
        else:
            return FARAWAY

    def intersectBottom(self, O: Vec3, D: Vec3) -> float:
        c = self.normal.dot(self.centre - O) / self.normal.dot(D)
        if c > 0 and (O + D * c - self.centre).length() <= self.radius:
            return c
        else:
            return FARAWAY

    def intersectSide(self, O: Vec3, D: Vec3) -> float:
        N = self.normal
        P = O - self.centre

        a = 1 - N.dot(D) ** 2
        b = 2 * (P.dot(D) - N.dot(D) * N.dot(P))
        c = P.dot(P) - N.dot(P) ** 2 - self.radius ** 2
        disc = (b ** 2) - (4 * a * c)

        if disc < 0:
            return FARAWAY

        sq = sqrt(disc)
        h0 = (-b - sq) / 2 / a
        h1 = (-b + sq) / 2 / a

        k0 = self.normal.dot(O - self.centre + D * h0)
        k1 = self.normal.dot(O - self.centre + D * h1)

        # Return smallest nonnegative solution that satisfies conditions
        if (h0 < 0 or k0 < 0 or k0 > self.height):
            if (h1 < 0 or k1 < 0 or k1 > self.height):
                return FARAWAY
            return h1
        return h0

    def intersect(self, O: Vec3, D: Vec3) -> float:
        """Return the closest intersection distance with the shape."""

        return min(self.intersectBottom(O, D), self.intersectTop(O, D), self.intersectSide(O, D))

    def isOnBottom(self, M: Vec3) -> bool:
        # Have to use `isclose` because of precision errors
        return isclose(M.dot(self.normal), self.centre.dot(self.normal)) and (self.centre - M).length() <= self.radius

    def isOnTop(self, M: Vec3) -> bool:
        Cs = self.centre + self.normal * self.height

        # Have to use `isclose` because of precision errors
        return isclose(M.dot(self.normal), Cs.dot(self.normal)) and (Cs - M).length() <= self.radius

    def normalAt(self, M: Vec3) -> Vec3:
        if self.isOnBottom(M):  # Bottom disk
            return -self.normal
        if self.isOnTop(M):  # Top disk
            return self.normal

        # Side of the cylinder
        k = self.normal.dot(M - self.centre)
        Cs = self.centre + self.normal * k
        return M - Cs

