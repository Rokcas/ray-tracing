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

    # Calculate diffuse and specular illumination from each light source
    for light_source in scene.light_sources:
        to_light = (light_source.position - ipoint).norm()  # direction to light

        # Shadow: find if the point is shadowed or not.
        # This is equivalent to finding if other objects are between ipoint and the light source
        light_distances = [o.intersect(nudged, to_light) for o in objects]
        shortest_light_distance = min(light_distances)
        sees_light = shortest_light_distance == obj.intersect(nudged, to_light)

        if sees_light:
            # Lambert shading (diffuse)
            lv = max(normal.dot(to_light), 0)
            colour += light_source.colour.compwise_mul(diffuse_colour) * lv

            # Blinn-Phong shading (specular)
            phong = normal.dot((to_light + to_ray_origin).norm())
            colour += light_source.colour.compwise_mul(obj.specular_colour) * math.pow(
                np.clip(phong, 0, 1), obj.roughness
            )

    # Reflection
    if bounce < MAX_BOUNCES:
        reflection_direction = (
            ray_direction - normal * 2 * ray_direction.dot(normal)
        ).norm()
        colour *= 1 - obj.reflectivity
        colour += (
            raytrace(nudged, reflection_direction, scene, bounce + 1) * obj.reflectivity
        )

    return colour
