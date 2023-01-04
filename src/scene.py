from dataclasses import dataclass
from src.vec3 import Vec3, Rgb
from src.shapes.base import BaseShape
import numpy as np


@dataclass
class LightSource:
    position: Vec3
    colour: Rgb


@dataclass
class Screen:
    corners: tuple[Vec3, Vec3, Vec3, Vec3]  # Clockwise order starting from top-left

    # Resolution in pixels
    width: int
    height: int

    def get_pixel_locations(self) -> list[Vec3]:
        w = self.width
        h = self.height
        corners = self.corners

        X = np.tile(np.linspace(corners[0].x, corners[1].x, w), h)
        X += np.repeat(np.linspace(0, corners[3].x - corners[0].x, h), w)

        Y = np.tile(np.linspace(corners[0].y, corners[1].y, w), h)
        Y += np.repeat(np.linspace(0, corners[3].y - corners[0].y, h), w)

        Z = np.tile(np.linspace(corners[0].z, corners[1].z, w), h)
        Z += np.repeat(np.linspace(0, corners[3].z - corners[0].z, h), w)

        return [Vec3(x, y, z) for x, y, z in zip(X, Y, Z)]


@dataclass
class Scene:
    camera: Vec3
    screen: Screen
    objects: list[BaseShape]
    light_sources: list[LightSource]

    def get_rays(self) -> list[Vec3]:
        pixel_locations = self.screen.get_pixel_locations()

        return [(ploc - self.camera).norm() for ploc in pixel_locations]
