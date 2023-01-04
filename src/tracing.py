from src.scene import Scene
from functools import reduce
import numpy as np
from src.vec3 import Vec3, Rgb
from src.constants import FARAWAY, MAX_BOUNCES
import math

def raytrace(O: Vec3, D: Vec3, scene: Scene, bounce: int = 0) -> Rgb:
    # O is the ray origin, D is the normalized ray direction
    # scene is a list of Sphere objects (see below)
    # bounce is the number of the bounce, starting at zero for camera rays

    objects = scene.objects
    distance_map = {obj.intersect(O, D): obj for obj in objects}
    shortest_distance = min(distance_map.keys())
    nearest_object = distance_map[shortest_distance]

    colour = Rgb(0, 0, 0)
    if shortest_distance != FARAWAY:
        return illuminate(nearest_object, O, D, shortest_distance, scene, bounce)
    return Rgb(0, 0, 0)


def illuminate(obj, O, D, d, scene: Scene, bounce):
    M = (O + D * d)                         # intersection point
    N = obj.normalAt(M)                    # normal
    toO = (scene.camera - M).norm()                    # direction to ray origin
    nudged = M + N * .0001                  # M nudged to avoid itself
    objects = scene.objects

    # Ambient
    diffuse_colour = obj.diffuseColourAt(M)
    colour = Rgb(0.05, 0.05, 0.05).compwise_mul(diffuse_colour)

    # Calculate diffuse and specular illumination from each light source
    for light_source in scene.light_sources:
        toL = (light_source.position - M).norm()              # direction to light

        # Shadow: find if the point is shadowed or not.
        # This amounts to finding out if M can see the light
        light_distances = [s.intersect(nudged, toL) for s in objects]
        shortest_light_distance = min(light_distances)
        sees_light = shortest_light_distance == obj.intersect(nudged, toL)

        if sees_light:
            # Lambert shading (diffuse)
            lv = max(N.dot(toL), 0)
            colour += light_source.colour.compwise_mul(diffuse_colour) * lv

            # Blinn-Phong shading (specular)
            phong = N.dot((toL + toO).norm())
            colour += light_source.colour.compwise_mul(obj.specular_colour) * math.pow(np.clip(phong, 0, 1), obj.roughness)

    # Reflection
    if bounce < MAX_BOUNCES:
        rayD = (D - N * 2 * D.dot(N)).norm()
        colour *= 1 - obj.reflectivity
        colour += raytrace(nudged, rayD, scene, bounce + 1) * obj.reflectivity

    return colour
