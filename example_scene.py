from src.vec3 import Vec3, Rgb
from src.shapes.sphere import Sphere
from src.shapes.checkered_sphere import CheckeredSphere
from src.shapes.texture_sphere import TextureSphere
from src.scene import Screen, Scene, LightSource

WIDTH = 600
HEIGHT = 300
RATIO = WIDTH / HEIGHT

scene = Scene(
    Vec3(0, 0.35, -1),
    Screen(
        (
            Vec3(-1, 1 / RATIO + 0.25, 0),
            Vec3(1, 1 / RATIO + 0.25, 0),
            Vec3(1, -1 / RATIO + 0.25, 0),
            Vec3(-1, -1 / RATIO + 0.25, 0)
        ),
        WIDTH,
        HEIGHT
    ),
    [
        TextureSphere(Rgb(0, 0, 1), 0, Vec3(.75, .1, 1), .6, "cat.webp"),
        # Sphere(Rgb(0, 0, 1), 0.3, Vec3(.75, .1, 1), .6),                # Blue sphere
        Sphere(Rgb(.3, .7, .3), 0.1, Vec3(-.75, .1, 2.25), .6),         # Green sphere
        Sphere(Rgb(1, .2, .1), 0.2, Vec3(-2.75, .1, 3.5), .6),          # Red sphere
        CheckeredSphere(Rgb(.75, .75, .75), 0.25, Vec3(0,-99999.5, 0), 99999),
    ],
    [
        LightSource(Vec3(5, 5, -10), Rgb(0.8, 1, 1)),
        LightSource(Vec3(-10, 10, 0), Rgb(1, 0.9, 0.9))
    ]
)
