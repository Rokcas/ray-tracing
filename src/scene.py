from dataclasses import dataclass
from src.vec3 import Vec3
from src.sphere import Sphere
from src.light import LightSource
import numpy as np

@dataclass
class Scene:
    camera: Vec3
    screen: tuple[Vec3, Vec3, Vec3, Vec3]
    objects: list[Sphere]
    light_sources: list[LightSource]

    def get_rays(self):
        (w, h) = (1920, 1080)         # Screen size
        r = float(w) / h
        # Screen coordinates: x0, y0, x1, y1.
        S = (-1, 1 / r + .25, 1, -1 / r + .25)
        x = np.tile(np.linspace(S[0], S[2], w), h)
        y = np.repeat(np.linspace(S[1], S[3], h), w)

        return Vec3(x, y, 0)
