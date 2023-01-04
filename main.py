from PIL import Image
from functools import reduce
import numpy as np
import time
from src.vec3 import Vec3, Rgb
from src.constants import FARAWAY, MAX_BOUNCES
from src.scene import Scene
from src.tracing import raytrace
from example_scene import scene
import multiprocessing


t0 = time.time()
rays = scene.get_rays()

# Multiprocessing to speed up rendering
def fn(ray):
    return raytrace(scene.camera, ray, scene)

print(f"Found {multiprocessing.cpu_count()} cores")
with multiprocessing.Pool() as p:
    colours = p.map(fn, rays)

print("Took", time.time() - t0)

pixels = [tuple(int(255 * x) for x in c.components()) for c in colours]
img = Image.new("RGB", (scene.screen.width, scene.screen.height))
img.putdata(pixels)

img.save("output.png")  # Uncomment to save the result
img.show()

