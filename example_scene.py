from src.scene import LightSource, Scene, Screen
from src.shapes.checker_sphere import CheckerSphere
from src.shapes.sphere import Sphere
from src.shapes.texture_sphere import TextureSphere
from src.vec3 import Rgb, Vec3
from src.shapes.cylinder import Cylinder
from src.shapes.plane import Plane

WIDTH = 300
HEIGHT = 200
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
        Cylinder(  # Red cylinder
            diffuse_colour=Rgb(1, 0.2, 0.1),
            centre=Vec3(-0.2, -0.1, 2.5),
            radius=0.4,
            height=1,
            normal=Vec3(-1, 0.01, -1).norm(),
            reflectivity=0.1,
        ),
        Plane(  # Light green plane
            diffuse_colour=Rgb(0.6, 0.9, 0.6),
            centre=Vec3(-0.75, 0.1, 60),
            normal=Vec3(1, 1, -1).norm(),
            reflectivity=0,
            specular_colour=Rgb(0, 0, 0)
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
