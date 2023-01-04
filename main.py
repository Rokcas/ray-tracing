from PIL import Image
from functools import reduce
import numpy as np
import time
from src.vec3 import Vec3, Rgb
from src.utils import extract
from src.constants import FARAWAY, MAX_BOUNCES
from src.scene import Scene
from src.tracing import raytrace
from example_scene import scene


t0 = time.time()
rays = scene.get_rays()
colour = raytrace(scene.camera, rays, scene)
print("Took", time.time() - t0)

width = scene.screen.width
height = scene.screen.height

rgb = [Image.fromarray((255 * np.clip(c, 0, 1).reshape((height, width))).astype(np.uint8), "L") for c in colour.components()]
result = Image.merge("RGB", rgb)
result.show()
# res.save("output.png")

