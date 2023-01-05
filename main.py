import multiprocessing
import time

from PIL import Image

from example_scene import scene
from src.tracing import raytrace
from src.vec3 import Rgb

t0 = time.time()
rays = scene.get_rays()

# Multiprocessing to speed up rendering
def fn(ray) -> Rgb:
    return raytrace(scene.camera, ray, scene)


print(f"Found {multiprocessing.cpu_count()} cores")
with multiprocessing.Pool() as p:
    colours = p.map(fn, rays)

print("Took", time.time() - t0)

pixels = [tuple(int(255 * x) for x in c.components()) for c in colours]
img = Image.new("RGB", (scene.screen.width, scene.screen.height))
img.putdata(pixels)

img.save("output.png")
img.show()
