# name: RadarRatRace.py
# author: bartramj025070

# imports

import pygame
import time
import os

import Sprites

# variables

game_running = True
window_data = {
	"window_x": 400,
	"window_y": 400
}

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
	response = sprite.add("window")
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
	window.fill(pygame.Color(255, 0, 255))

	add_sprite(spr)

	pygame.display.flip()
	clock.tick(int(60))