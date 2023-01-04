from functools import reduce
import numpy as np
from src.constants import FARAWAY
from src.vec3 import Vec3, Rgb
from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass
class BaseShape(ABC):
    diffuse_colour: Rgb
    mirror: float

    @abstractmethod
    def intersect(self, O, D):
        pass

    @abstractmethod
    def intersect(self, O, D):
        pass

    @abstractmethod
    def normalAt(self, M):
        pass

    def diffuseColourAt(self, M):
        return self.diffuse_colour
