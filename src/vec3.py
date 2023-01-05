import math
from dataclasses import dataclass


@dataclass
class Vec3:
    x: float
    y: float
    z: float

    def __neg__(self):
        """Negate the vector."""
        return Vec3(-self.x, -self.y, -self.z)

    def __mul__(self, other):
        """Scale the vector by a number."""

        # TASK 1: Fix the implementation
        return self

    def __truediv__(self, other):
        """Scale the vector by the inverse of the given number."""
        return Vec3(self.x / other, self.y / other, self.z / other)

    def __add__(self, other):
        """Add two vectors."""

        # TASK 1: Fix the implementation
        return self

    def __sub__(self, other):
        """Subtract one vector from another."""
        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)

    def dot(self, other) -> float:
        """Calculate the dot product of two vectors."""

        # TASK 1: Fix the implementation
        return 1

    def cross(self, other):
        """Calculate the cross product of two vectors."""
        return Vec3(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y - other.x,
        )

    def __abs__(self) -> float:
        """Find the square length of the vector."""
        return self.dot(self)

    def length(self) -> float:
        """Calculate the length of the vector."""
        return math.sqrt(abs(self))

    def compwise_mul(self, other):
        """Multiply two vectors element-wise."""
        return Vec3(self.x * other.x, self.y * other.y, self.z * other.z)

    def norm(self):
        """Normalise the vector to have a length of 1."""
        length = self.length()
        return self if length == 0 else self / length

    def components(self) -> tuple[float, float, float]:
        """Return the components of the vector as a tuple."""
        return (self.x, self.y, self.z)


Rgb = Vec3
