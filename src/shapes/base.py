from functools import reduce
import numpy as np
from src.constants import FARAWAY
from src.vec3 import Vec3, Rgb
from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class BaseShape(ABC):
    """Abstract class for shapes that can be rendered."""

    diffuse_colour: Rgb  # Used to scale the RGB values of diffuse lighting
    specular_colour: Rgb = Rgb(
        1, 1, 1
    )  # Used to scale the RGB values of specular lighting
    reflectivity: float = 0.3  # Specifies the fraction of light that is fully reflected
    specular_coef: float = 0.5  # Coefficient for scaling specular lighting intensity
    diffuse_coef: float = 0.5  # Coefficient for scaling diffuse lighting intensity
    roughness: float = 50  # Used to control the spread of specular lighting

    @abstractmethod
    def intersect(self, O, D):
        """Return the distance to intersection of the object and a ray coming from O in direction D.

        Return FARAWAY if there is no intersection.
        """
        pass

    @abstractmethod
    def normalAt(self, M):
        """Given a point on the object, return the surface normal at that point."""
        pass

    def diffuseColourAt(self, M):
        """Return the diffuse colour of the object at the given point on its surface."""
        return self.diffuse_colour
