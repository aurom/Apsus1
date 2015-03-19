#!/usr/bin/env python
import pygame
import pygame.camera
from pygame.locals import *
import pygame.mixer
pygame.init() #inicias
pygame.camera.init() #inicias camara
size = (640,480) #tamaño del display
display = pygame.display.set_mode(size) #generas display
list_cam = pygame.camera.list_cameras() #generas la lista de camaras
id_cam = list_cam[0] #camara por defecto
cam = pygame.camera.Camera(id_cam, size,"RGB") # generas la camara a utilizar
cam.start() #inicias camara
clock = pygame.time.Clock() #inicias reloj
instantanea = pygame.surface.Surface(size,0,display)
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('Alabama 3 - Woke Up This Morning.mp3')
pygame.mixer.music.play()
pygame.mixer.music.set_volume(1)
fin = False
while not fin:
	eventos = pygame.event.get()
	for ev in eventos:
		if ev.type == QUIT or (ev.type == KEYDOWN and ev.key == K_ESCAPE):
			fin = True
	if cam.query_image():
		instantanea = cam.get_image(instantanea)
	else:
		instantanea = cam.get_image(display)
	pygame.display.flip()
	clock.tick()
pygame.quit()
