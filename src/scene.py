from dataclasses import dataclass
from src.vec3 import Vec3, Rgb
from src.sphere import Sphere
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

    def get_pixel_locations(self) -> Vec3:
        w = self.width
        h = self.height
        corners = self.corners

        x = np.tile(np.linspace(corners[0].x, corners[1].x, w), h)
        x += np.repeat(np.linspace(0, corners[3].x - corners[0].x, h), w)

        y = np.tile(np.linspace(corners[0].y, corners[1].y, w), h)
        y += np.repeat(np.linspace(0, corners[3].y - corners[0].y, h), w)

        z = np.tile(np.linspace(corners[0].z, corners[1].z, w), h)
        z += np.repeat(np.linspace(0, corners[3].z - corners[0].z, h), w)

        return Vec3(x, y, z)


@dataclass
class Scene:
    camera: Vec3
    screen: Screen
    objects: list[Sphere]
    light_sources: list[LightSource]

    def get_rays(self) -> Vec3:
        pixel_locations = self.screen.get_pixel_locations()

        return (pixel_locations - self.camera).norm()
