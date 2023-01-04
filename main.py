from PIL import Image
from functools import reduce
import numpy as np
import time
from src.vec3 import Vec3, Rgb
from src.constants import FARAWAY, MAX_BOUNCES
from src.scene import Scene
from src.tracing import raytrace
from example_scene import scene


t0 = time.time()
rays = scene.get_rays()

colour = [raytrace(scene.camera, ray, scene) for ray in rays]
print("Took", time.time() - t0)

width = scene.screen.width
height = scene.screen.height

pixels = [tuple(int(255 * x) for x in c.components()) for c in colour]
img = Image.new("RGB", (width, height))
img.putdata(pixels)
# rgb = [Image.fromarray((255 * np.clip(c, 0, 1).reshape((height, width))).astype(np.uint8), "L") for c in colour.components()]
# result = Image.merge("RGB", rgb)
img.show()
# res.save("output.png")

