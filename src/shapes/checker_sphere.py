from src.shapes.sphere import Sphere


class CheckerSphere(Sphere):
    def diffuseColourAt(self, M):
        # TASK 7: Change this method to form a checkerboard pattern on the sphere.
        # Then add a CheckeredSphere somewhere in the scene if you haven't already.
        return super().diffuseColourAt(M)
