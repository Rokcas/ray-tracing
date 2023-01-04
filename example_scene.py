from src.vec3 import Vec3, Rgb
from src.shapes.sphere import Sphere
from src.shapes.checkered_sphere import CheckeredSphere
from src.shapes.texture_sphere import TextureSphere
from src.scene import Screen, Scene, LightSource
from src.shapes.plane import Plane

WIDTH = 1920
HEIGHT = 1080
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
        Sphere(Rgb(.5, .223, .5), 0.0, Vec3(-.75, .1, 2.25), .6),
        Sphere(Rgb(1, .572, .184), 0.0, Vec3(-2.75, .1, 3.5), .6),
        # CheckeredSphere(Rgb(.75, .75, .75), 0.25, Vec3(0,-99999.5, 0), 99999),
        Plane(Rgb(.5, .5, .5), 0.0, Vec3(0, 1, 0), Vec3(0, -0.5, 0)),
        Plane(Rgb(.2, .9, .9), 0, Vec3(0, 0, -1), Vec3(0, 0, 50))
    ],
    [
        LightSource(Vec3(5, 5, -10), Rgb(0.8, 1, 1)),
        LightSource(Vec3(-10, 10, 0), Rgb(1, 0.9, 0.9)),
        # LightSource(Vec3(5, 5, 45), Rgb(0.8, 1, 1))
    ]
)
