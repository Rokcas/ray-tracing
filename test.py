import thread
import time

t0 = time.time()
rays = scene.get_rays()

colour = [raytrace(scene.camera, ray, scene) for ray in rays]
print("Took", time.time() - t0)
