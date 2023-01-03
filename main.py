from PIL import Image
from functools import reduce
import numpy as np
import time
from src.vec3 import Vec3, Rgb
from src.utils import extract
from src.sphere import Sphere, CheckeredSphere
from src.constants import FARAWAY
from src.scene import Scene
from example_scene import scene


def raytrace(O, D, scene: Scene, bounce = 0):
    # O is the ray origin, D is the normalized ray direction
    # scene is a list of Sphere objects (see below)
    # bounce is the number of the bounce, starting at zero for camera rays

    objects = scene.objects
    distances = [s.intersect(O, D) for s in objects]
    nearest = reduce(np.minimum, distances)
    color = Rgb(0, 0, 0)
    for (s, d) in zip(objects, distances):
        hit = (nearest != FARAWAY) & (d == nearest)
        if np.any(hit):
            dc = extract(hit, d)
            Oc = O.extract(hit)
            Dc = D.extract(hit)
            cc = illuminate(s, Oc, Dc, dc, scene, bounce)
            color += cc.place(hit)
    return color


def illuminate(obj, O, D, d, scene: Scene, bounce):
    M = (O + D * d)                         # intersection point
    N = obj.normalAt(M)                    # normal
    toL = (scene.light_sources[0].position - M).norm()                    # direction to light
    toO = (scene.camera - M).norm()                    # direction to ray origin
    nudged = M + N * .0001                  # M nudged to avoid itself

    # Shadow: find if the point is shadowed or not.
    # This amounts to finding out if M can see the light
    objects = scene.objects
    light_distances = [s.intersect(nudged, toL) for s in objects]
    light_nearest = reduce(np.minimum, light_distances)
    seelight = light_distances[objects.index(obj)] == light_nearest

    # Ambient
    color = Rgb(0.05, 0.05, 0.05)

    # Lambert shading (diffuse)
    lv = np.maximum(N.dot(toL), 0)
    color += obj.diffusecolor(M) * lv * seelight

    # Reflection
    if bounce < 2:
        rayD = (D - N * 2 * D.dot(N)).norm()
        color += raytrace(nudged, rayD, scene, bounce + 1) * obj.mirror

    # Blinn-Phong shading (specular)
    phong = N.dot((toL + toO).norm())
    color += Rgb(1, 1, 1) * np.power(np.clip(phong, 0, 1), 50) * seelight
    return color


t0 = time.time()
rays = scene.get_rays()
color = raytrace(scene.camera, rays, scene)
print("Took", time.time() - t0)

width = scene.screen.width
height = scene.screen.height

rgb = [Image.fromarray((255 * np.clip(c, 0, 1).reshape((height, width))).astype(np.uint8), "L") for c in color.components()]
result = Image.merge("RGB", rgb)
result.show()
# res.save("output.png")

