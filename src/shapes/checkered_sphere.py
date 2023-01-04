from src.shapes.sphere import Sphere

class CheckeredSphere(Sphere):
    def diffuseColourAt(self, M):
        checker = ((M.x * 2).astype(int) % 2) == ((M.z * 2).astype(int) % 2)
        checker ^= (M.x < 0) ^ (M.z < 0)
        return self.diffuse_colour * checker
