from src.vec3 import Vec3, Rgb
from src.sphere import Sphere, CheckeredSphere
from src.scene import Screen, Scene, LightSource

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
        Sphere(Vec3(.75, .1, 1), .6, Rgb(0, 0, 1)),
        Sphere(Vec3(-.75, .1, 2.25), .6, Rgb(.5, .223, .5)),
        Sphere(Vec3(-2.75, .1, 3.5), .6, Rgb(1, .572, .184)),
        CheckeredSphere(Vec3(0,-99999.5, 0), 99999, Rgb(.75, .75, .75), 0.25),
    ],
    [
        LightSource(Vec3(5, 5, -10), Rgb(0.8, 1, 1)),
        LightSource(Vec3(-10, 10, 0), Rgb(1, 0.9, 0.9))
    ]
)
