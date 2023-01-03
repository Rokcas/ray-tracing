from dataclasses import dataclass
from src.vec3 import Vec3, Rgb


@dataclass
class LightSource:
    position: Vec3
    colour: Rgb
