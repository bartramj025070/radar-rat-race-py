# name: RadarRatRace.py
# author: bartramj025070

# imports

import pygame
from pygame import mixer as Audio

import math

import time
import os

import Sprites

# variables

game_running = True
game_fps = 60

window_data = {
	"window_x": 800,
	"window_y": 600
}

direction = 0

spr = Sprites.new("playerRat", [
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

spr2 = Sprites.new("enemyRat0", [
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
	[0,0,0,0,0,1,0,0,0],], "red")
spr2.deploy()

pygame.init()

def startup():
	if os.path.exists("fpsCap.lock"):
		with open("fpsCap.lock", 'r') as cap:
			content = cap.read()
			game_fps=int(content.splitlines()[0])
	else:
		try:
			game_fps=int(input("Welcome to the VIC 20 Radar Rat Race experience! You appear to be new, please set an FPS Limit: "))
			with open("fpsCap.lock", 'w') as cap:
				cap.write(str(game_fps))

			string = f"GAME FPS SET TO: {str(game_fps)}"
			print("\n" + ("*" * len(string)))
			print(string)
			print("*" * len(string))
		except Exception as e:
			print(f"Failure!\n{e}")
			startup()

startup()

clock = pygame.time.Clock()
window = pygame.display.set_mode((window_data["window_x"], window_data["window_y"]))

# methods

def add_sprite(sprite):
	response = sprite.add()
	for chunk in response:
		for byte in chunk:
			if byte != "":
				exec(byte)

Audio.init()

Audio.music.load("GameMusic.mp3")
Audio.music.set_volume(1)

Audio.music.play(-1)
while game_running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			Sprites.quit()
			game_running = False
		else:
			continue

	window.fill(pygame.Color(255, 255, 255))

	keys = pygame.key.get_pressed()
	if keys[pygame.K_LEFT]:
		direction = 270
	elif keys[pygame.K_UP]:
		direction = 0
	elif keys[pygame.K_RIGHT]:
		direction = 90
	elif keys[pygame.K_DOWN]:
		direction = 180

	mouse_pos = pygame.mouse.get_pos()
	pygame.display.set_caption("VC_20: Radar Rat Race")

	add_sprite(spr)
	add_sprite(spr2)

	spr.move([str(mouse_pos[0]), str(mouse_pos[1])])
	spr2.move([str(mouse_pos[0] +  (7 * 9)), str(mouse_pos[1])])

	spr.set_rotation(direction)

	# print(str(mouse_pos))

	pygame.display.flip()
	clock.tick(int(game_fps))
	pygame.event.pump()
	if not Audio.music.get_busy():
		print("hi")
		Audio.music.rewind()