from src.shapes.sphere import Sphere

class CheckeredSphere(Sphere):
    def diffuseColourAt(self, M):
        checker = ((M.x * 2).astype(int) % 2) == ((M.z * 2).astype(int) % 2)
        return self.diffuse_colour * checker
