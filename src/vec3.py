import numpy as np
from src.utils import extract

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
        return np.sqrt(abs(self))
    def compwise_mul(self, other):
        return Vec3(self.x * other.x, self.y * other.y, self.z * other.z)
    def norm(self):
        length = self.length()
        return self * (1.0 / np.where(length == 0, 1, length))
    def components(self):
        return (self.x, self.y, self.z)
    def extract(self, cond):
        return Vec3(extract(cond, self.x),
                    extract(cond, self.y),
                    extract(cond, self.z))
    def place(self, cond):
        r = Vec3(np.zeros(cond.shape), np.zeros(cond.shape), np.zeros(cond.shape))
        np.place(r.x, cond, self.x)
        np.place(r.y, cond, self.y)
        np.place(r.z, cond, self.z)
        return r
    def where(self, cond, other):
        return Vec3(
            np.where(cond, self.x, other.x),
            np.where(cond, self.y, other.y),
            np.where(cond, self.z, other.z),
        )

Rgb = Vec3
