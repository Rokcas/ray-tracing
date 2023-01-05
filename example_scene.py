from src.scene import LightSource, Scene, Screen
from src.shapes.checker_sphere import CheckerSphere
from src.shapes.sphere import Sphere
from src.shapes.texture_sphere import TextureSphere
from src.vec3 import Rgb, Vec3

WIDTH = 600
HEIGHT = 300
RATIO = WIDTH / HEIGHT

scene = Scene(
    camera=Vec3(0, 0.35, -1),
    screen=Screen(
        corners=(
            Vec3(-1, 1 / RATIO + 0.25, 0),
            Vec3(1, 1 / RATIO + 0.25, 0),
            Vec3(1, -1 / RATIO + 0.25, 0),
            Vec3(-1, -1 / RATIO + 0.25, 0),
        ),
        width=WIDTH,
        height=HEIGHT,
    ),
    objects=[
        Sphere(  # Blue sphere
            diffuse_colour=Rgb(0, 0, 1), centre=Vec3(0.75, 0.1, 1), radius=0.6
        ),
        Sphere(  # Green sphere
            diffuse_colour=Rgb(0.3, 0.7, 0.3),
            centre=Vec3(-0.75, 0.1, 2.25),
            radius=0.6,
            roughness=30,
        ),
        TextureSphere(  # Red sphere
            diffuse_colour=Rgb(1, 0.2, 0.1),
            centre=Vec3(-2.75, 0.1, 3.5),
            radius=0.6,
            # Attributes to make cat texture more visible
            specular_colour=Rgb(0, 0, 0),
            reflectivity=0,
            texture_path="textures/cat.webp",
        ),
        # TASK 3: Add an object that looks like a flat surface under the 3 spheres
    ],
    ambient_light=Rgb(0.1, 0.1, 0.1),
    light_sources=[
        LightSource(position=Vec3(5, 5, -10), colour=Rgb(0.8, 1, 1)),
        LightSource(position=Vec3(-10, 10, 0), colour=Rgb(1, 0.9, 0.9)),
    ],
)
