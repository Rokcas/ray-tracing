from src.shapes.sphere import Sphere


class CheckeredSphere(Sphere):
    def diffuseColourAt(self, M):
        """Return either the diffuse colour of the object or black, to form a checker pattern."""
        checker = int(M.x * 2) % 2 == int(M.z * 2) % 2
        checker ^= (M.x < 0) ^ (M.z < 0)
        return self.diffuse_colour * checker
