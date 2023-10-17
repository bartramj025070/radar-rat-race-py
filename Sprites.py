# name: Sprites.py
# author: bartramj025070

# version: v1.0.0r

# imports

import os
import json
import math

import pygame

# variables

AllSprites = []
AllColors = {
    "red": {
        "r": 255,
        "g": 0,
        "b": 0
    },
    "blue": {
        "r": 0,
        "g": 0,
        "b": 255
    }
}

# methods

def get_color(name):
    return AllColors[name]

def get_pycolor(name):
    color_table = AllColors[name]
    return pygame.Color(int(color_table["r"]), int(color_table["g"]), int(color_table["b"]))

class Sprite:
    def __init__(self, identifier, binary_data, color, rotation=0, width=16, height=16, window_name="window"):
        self.identifier=identifier
        self.binary_data=binary_data
        self.color=color
        self.width=width
        self.height=height
        self.size=1
        self.position=["", ""]
        self.window_name=window_name
        self.rotation=rotation

    def deploy(self):
        print("Deploying Sprite File: " + self.identifier + "...")
        self.position=[f"{self.window_name}.get_width() / 2", f"{self.window_name}.get_height() / 2"]

    def move(self, newPos):
        self.position=newPos

    def set_rotation(self, newRot):
        # Ensure the rotation is a valid multiple of 90 degrees
        newRot = int(newRot) % 360  # Keep rotation within 0-359 degrees
        if newRot % 90 != 0:
            raise ValueError("Rotation angle must be a multiple of 90 degrees.")

        # Calculate the difference between the current rotation and the target rotation
        rotation_diff = (newRot - self.rotation) % 360

        # Calculate the effective number of rotations needed
        num_rotations = rotation_diff // 90

        # Rotate the binary data to the specified angle
        for _ in range(num_rotations):
            self.binary_data = list(zip(*reversed(self.binary_data)))

        # Update the rotation angle
        self.rotation = newRot

    #def set_rotation(self, newRot):
    #    self.rotation=newRot

    def add(self):
        color_table = AllColors[self.color]

        r = str(int(color_table["r"]))
        g = str(int(color_table["g"]))
        b = str(int(color_table["b"]))


        col_str = "pygame.Color(" + r + ", " + g + ", " + b + ")"

        response = []

        chunkIndex = 0
        byteIndex = 0

        for chunk in self.binary_data:
            response_chunk = []

            byteIndex = 0
            chunkIndex += 1
            for byte in chunk:
                byteIndex += 1
                isFilled = (int(byte)==1)
                if isFilled:
                    rotated_rect_str = (
                        f"pygame.Rect(int({self.position[0]}) + {byteIndex * 7}, int({self.position[1]}) + {chunkIndex * 7}, int(7), int(7))"
                        f".rotate({self.rotation})"
                    )
                    rect_str = f"pygame.Rect(int({self.position[0]}) + {byteIndex * 7}, int({self.position[1]}) + {chunkIndex * 7}, int(7), int(7))"
                    response_chunk.append(f"pygame.draw.rect({self.window_name}, {col_str}, {rect_str})")
                else:
                    response_chunk.append("")
            response.append(response_chunk)
        return response

def new(identifier, binary_data, color):
    if binary_data:
        with open(identifier + ".sprite", 'w') as f:
            f.write("color=" + color + "\n" + json.dumps(binary_data))
            spr = Sprite(identifier, binary_data, color)

            AllSprites.append(spr)
            return spr

def quit():
    for Sprite in AllSprites:
        if os.path.exists(Sprite.identifier + ".sprite"):
            os.remove(Sprite.identifier + ".sprite")