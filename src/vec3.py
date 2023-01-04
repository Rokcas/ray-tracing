import numpy as np
import math

from dataclasses import dataclass

@dataclass
class Vec3():
    x: float
    y: float
    z: float

    def __neg__(self):
        return Vec3(-self.x, -self.y, -self.z)
    def __mul__(self, other):
        return Vec3(self.x * other, self.y * other, self.z * other)
    def __truediv__(self, other):
        return Vec3(self.x / other, self.y / other, self.z / other)
    def __add__(self, other):
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)
    def __sub__(self, other):
        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)
    def dot(self, other):
        return (self.x * other.x) + (self.y * other.y) + (self.z * other.z)
    def cross(self, other):
        return Vec3(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y - other.x
        )
    def __abs__(self):
        return self.dot(self)
    def length(self):
        return math.sqrt(abs(self))
    def compwise_mul(self, other):
        return Vec3(self.x * other.x, self.y * other.y, self.z * other.z)
    def norm(self):
        length = self.length()
        return self if length == 0 else self / length
    def components(self):
        return (self.x, self.y, self.z)

Rgb = Vec3
