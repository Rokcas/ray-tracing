from src.scene import Scene
from functools import reduce
import numpy as np
from src.vec3 import Rgb
from src.constants import FARAWAY, MAX_BOUNCES
from src.utils import extract

def raytrace(O, D, scene: Scene, bounce = 0):
    # O is the ray origin, D is the normalized ray direction
    # scene is a list of Sphere objects (see below)
    # bounce is the number of the bounce, starting at zero for camera rays

    objects = scene.objects
    distances = [s.intersect(O, D) for s in objects]
    nearest = reduce(np.minimum, distances)
    colour = Rgb(0, 0, 0)
    for (s, d) in zip(objects, distances):
        hit = (nearest != FARAWAY) & (d == nearest)
        if np.any(hit) or True:
            dc = extract(hit, d)
            Oc = O.extract(hit)
            Dc = D.extract(hit)
            cc = illuminate(s, Oc, Dc, dc, scene, bounce)
            colour += cc.place(hit)
    return colour


def illuminate(obj, O, D, d, scene: Scene, bounce):
    M = (O + D * d)                         # intersection point
    N = obj.normalAt(M)                    # normal
    toO = (scene.camera - M).norm()                    # direction to ray origin
    nudged = M + N * .0001                  # M nudged to avoid itself

    # Ambient
    colour = Rgb(0.05, 0.05, 0.05)

    objects = scene.objects

    # Calculate diffuse and specular illumination from each light source
    for light_source in scene.light_sources:
        toL = (light_source.position - M).norm()              # direction to light

        # Shadow: find if the point is shadowed or not.
        # This amounts to finding out if M can see the light
        light_distances = [s.intersect(nudged, toL) for s in objects]
        light_nearest = reduce(np.minimum, light_distances)
        seelight = light_distances[objects.index(obj)] == light_nearest

        # Lambert shading (diffuse)
        lv = np.maximum(N.dot(toL), 0)
        colour += light_source.colour.compwise_mul(obj.diffuseColourAt(M)) * lv * seelight

        # Blinn-Phong shading (specular)
        phong = N.dot((toL + toO).norm())
        colour += light_source.colour * np.power(np.clip(phong, 0, 1), 50) * seelight

    # Reflection
    if bounce < MAX_BOUNCES:
        rayD = (D - N * 2 * D.dot(N)).norm()
        colour *= 1 - obj.mirror
        colour += raytrace(nudged, rayD, scene, bounce + 1) * obj.mirror

    return colour
