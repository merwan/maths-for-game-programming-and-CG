import pygame
from pygame.locals import DOUBLEBUF, OPENGL
from OpenGL.GL import glClear, GL_COLOR_BUFFER_BIT, GL_DEPTH_BUFFER_BIT
from Mesh3D import Mesh3D

pygame.init()

screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption("OpenGL in Python")
done = False
white = pygame.Color(255, 255, 255)
mesh = Mesh3D()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    mesh.draw()
    pygame.display.flip()

pygame.quit()
