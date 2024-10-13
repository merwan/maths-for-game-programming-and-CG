from OpenGL.GL import glBegin, glEnd, glVertex3fv, GL_LINE_LOOP


class Mesh3D:
    def __init__(self) -> None:
        self.vertices = [
            (0.5, -0.5, 0.5),
            (-0.5, -0.5, 0.5),
            (0.5, 0.5, 0.5),
            (-0.5, 0.5, 0.5),
            (0.5, 0.5, -0.5),
            (-0.5, 0.5, -0.5),
        ]
        self.triangles = [0, 2, 3, 0, 3, 1]

    def draw(self):
        for t in range(0, len(self.triangles), 3):
            glBegin(GL_LINE_LOOP)
            glVertex3fv(self.vertices[self.triangles[t]])
            glVertex3fv(self.vertices[self.triangles[t + 1]])
            glVertex3fv(self.vertices[self.triangles[t + 2]])
            glEnd()


class Cube(Mesh3D):
    def __init__(self) -> None:
        self.vertices = [
            (-0.5, -0.5, 0.5),
            (0.5, -0.5, 0.5),
            (0.5, 0.5, 0.5),
            (-0.5, 0.5, 0.5),
            (-0.5, -0.5, -0.5),
            (0.5, -0.5, -0.5),
            (0.5, 0.5, -0.5),
            (-0.5, 0.5, -0.5),
        ]
        self.triangles = [
            0, 1, 3,
            1, 2, 3,
            1, 5, 2,
            5 ,6 ,2,
            4, 5, 6,
            4, 6, 7,
            4, 0, 7,
            0, 3, 7,
            3, 2, 7,
            2, 6, 7,
            0, 1, 4,
            1, 4, 5,
        ]
