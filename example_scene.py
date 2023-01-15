from src.scene import LightSource, Scene, Screen
from src.shapes.checker_sphere import CheckerSphere
from src.shapes.cylinder import Cylinder
from src.shapes.texture_cylinder import TextureCylinder
from src.vec3 import Rgb, Vec3
from src.shapes.plane import Plane

WIDTH = 800
HEIGHT = 400
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
        TextureCylinder(
            diffuse_colour=Rgb(1, 0.2, 0.1),
            centre=Vec3(1, -0.5, 1.5),
            radius=0.4,
            height=1,
            normal=Vec3(0, 1, 0).norm(),
            reflectivity=0.1,
            texture_path="textures/maxwell.jpg"
        ),
        TextureCylinder(
            diffuse_colour=Rgb(1, 0.2, 0.1),
            centre=Vec3(0, -0.5, 1.5),
            radius=0.4,
            height=1,
            normal=Vec3(0, 1, 0).norm(),
            reflectivity=0.1,
            texture_path="textures/maxwell.jpg"
        ),
        TextureCylinder(
            diffuse_colour=Rgb(1, 0.2, 0.1),
            centre=Vec3(-1, -0.5, 1.5),
            radius=0.4,
            height=1,
            normal=Vec3(0, 1, 0).norm(),
            reflectivity=0.1,
            texture_path="textures/maxwell.jpg"
        ),
        CheckerSphere(
            diffuse_colour=Rgb(0.75, 0.75, 0.75),
            centre=Vec3(0, -99999.5, 0),
            radius=99999,
        ),
    ],
    ambient_light=Rgb(0.1, 0.1, 0.1),
    light_sources=[
        LightSource(position=Vec3(5, 5, -10), colour=Rgb(0.8, 1, 1)),
        LightSource(position=Vec3(-10, 10, 0), colour=Rgb(1, 0.9, 0.9)),
    ],
)
