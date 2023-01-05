import math

import numpy as np

from src.constants import FARAWAY, MAX_BOUNCES
from src.scene import Scene
from src.shapes.base import BaseShape
from src.vec3 import Rgb, Vec3


def raytrace(
    ray_origin: Vec3, ray_direction: Vec3, scene: Scene, bounce: int = 0
) -> Rgb:
    """Trace the given ray to find its RGB colour."""

    objects = scene.objects
    distance_map = {obj.intersect(ray_origin, ray_direction): obj for obj in objects}
    shortest_distance = min(distance_map.keys())
    nearest_object = distance_map[shortest_distance]

    if shortest_distance != FARAWAY:
        return illuminate(
            nearest_object, ray_origin, ray_direction, shortest_distance, scene, bounce
        )
    return Rgb(0, 0, 0)


def illuminate(
    obj: BaseShape,
    ray_origin: Vec3,
    ray_direction: Vec3,
    distance: float,
    scene: Scene,
    bounce: int,
) -> Rgb:
    """Return the object's illumination at the point it intersects with the ray."""

    ipoint = ray_origin + ray_direction * distance  # intersection point
    normal = obj.normalAt(ipoint)  # normal

    to_ray_origin = (ray_origin - ipoint).norm()  # direction to ray origin
    nudged = (
        ipoint + normal * 0.0001
    )  # ipoint nudged to avoid intersecting with the same object
    objects = scene.objects

    # Ambient
    diffuse_colour = obj.diffuseColourAt(ipoint)
    colour = scene.ambient_light.compwise_mul(diffuse_colour)

    # TASK 4: Calculate the diffuse lighting component and add it to colour.
    # This component is equal to the sum of diffuse lighting on the object
    # from all light sources that are not covered by other objects.

    # TASK 5: Calculate the specular lighting component.

    # TASK 6: Calculate perfectly reflected light.
    # This can be done by recursively tracing another ray coming from the intersection point.
    # Make sure the origin of this new ray is a small distance away from the surface of the object.
    # Otherwise, the new ray would collide with it again.
    # Use obj.reflectiveness to combine the perfectly reflected light with the previously
    # calculated colour.

    return colour
