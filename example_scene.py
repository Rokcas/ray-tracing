from src.vec3 import Vec3, Rgb
from src.shapes.sphere import Sphere
from src.shapes.checkered_sphere import CheckeredSphere
from src.shapes.texture_sphere import TextureSphere
from src.scene import Screen, Scene, LightSource

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
            Vec3(-1, -1 / RATIO + 0.25, 0)
        ),
        width=WIDTH,
        height=HEIGHT
    ),
    objects=[
        Sphere(                                     # Blue sphere
            diffuse_colour=Rgb(0, 0, 1),
            centre=Vec3(.75, .1, 1),
            radius=.6
        ),
        Sphere(                                     # Green sphere
            diffuse_colour=Rgb(.3, .7, .3),
            centre=Vec3(-.75, .1, 2.25),
            radius=.6,
            roughness=30,
            reflectivity=.1
        ),
        TextureSphere(                              # Red sphere
            diffuse_colour=Rgb(1, .2, .1),
            centre=Vec3(-2.75, .1, 3.5),
            radius=.6,

            # Attributes to make cat texture more visible
            specular_colour=Rgb(0, 0, 0),
            reflectivity=0,
            texture_path="cat.webp"
        ),
        CheckeredSphere(
            diffuse_colour=Rgb(.75, .75, .75),
            centre=Vec3(0, -99999.5, 0),
            radius=99999
        )
    ],
    ambient_light=Rgb(.1, .1, .1),
    light_sources=[
        LightSource(
            position=Vec3(5, 5, -10),
            colour=Rgb(0.8, 1, 1)
        ),
        LightSource(
            position=Vec3(-10, 10, 0),
            colour=Rgb(1, 0.9, 0.9)
        )
    ]
)
