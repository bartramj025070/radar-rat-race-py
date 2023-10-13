# name: RadarRatRace.py
# author: bartramj025070

# imports

import pygame
from pygame import mixer as Audio

import time
import os

import Sprites

# variables

game_running = True
window_data = {
	"window_x": 800,
	"window_y": 600
}

Audio.init()

Audio.music.load("GameMusic.mp3")
Audio.music.set_volume(1)

Audio.music.play(-1)

spr = Sprites.new("sprite0", [
	[0,0,0,0,1,0,0,0,0],
	[0,1,1,0,1,0,1,1,0],
	[1,1,1,1,1,1,1,1,1],
	[1,1,1,1,1,1,1,1,1],
	[0,1,1,1,1,1,1,1,0],
	[0,0,0,1,1,1,0,0,0],
	[0,0,0,1,1,1,0,0,0],
	[0,0,1,1,1,1,1,0,0],
	[0,0,1,1,1,1,1,0,0],
	[0,0,0,1,1,1,0,0,0],
	[0,0,0,0,1,0,0,0,0],
	[0,0,0,0,1,0,0,0,0],
	[0,0,0,0,0,1,0,0,0],], "blue")
spr.deploy()

pygame.init()

clock = pygame.time.Clock()
window = pygame.display.set_mode((window_data["window_x"], window_data["window_y"]))

def add_sprite(sprite):
	response = sprite.add()
	for chunk in response:
		for byte in chunk:
			if byte != "":
				exec(byte)

while game_running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			Sprites.quit()
			game_running = False

	pygame.display.set_caption("VC_20: Radar Rat Race")
	window.fill(pygame.Color(255, 255, 255))

	mouse_pos = pygame.mouse.get_pos()

	add_sprite(spr)
	spr.move([str(mouse_pos[0]), str(mouse_pos[1])])

	print(str(mouse_pos))

	pygame.display.flip()
	clock.tick(int(60))
	if not Audio.music.get_busy():
		print("hi")
		Audio.music.rewind()