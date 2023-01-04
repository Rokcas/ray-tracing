from src.shapes.sphere import Sphere

class CheckeredSphere(Sphere):
    def diffuseColourAt(self, M):
        checker = int(M.x * 2) % 2 == int(M.z * 2) % 2
        checker ^= (M.x < 0) ^ (M.z < 0)
        return self.diffuse_colour * checker
