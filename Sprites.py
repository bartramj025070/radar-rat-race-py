import os
import json

import pygame

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

def get_color(name):
    return AllColors[name]

def get_pycolor(name):
    color_table = AllColors[name]
    return pygame.Color(int(color_table["r"]), int(color_table["g"]), int(color_table["b"]))

class Sprite:
    def __init__(self, identifier, binary_data, color, width=16, height=16):
        self.identifier=identifier
        self.binary_data=binary_data
        self.color=color
        self.width=width
        self.height=height
        self.size=1

    def deploy(self):
        print("Deploying Sprite File: " + self.identifier + "...")

    def add(self, window_name):
        color_table = AllColors[self.color]

        r = str(int(color_table["r"]))
        g = str(int(color_table["g"]))
        b = str(int(color_table["b"]))

        dimension_x = f"int({window_name}.get_width() / 2)"
        dimension_y = f"int({window_name}.get_height() / 2)"

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
                    rect_str = f"pygame.Rect({dimension_x} + {byteIndex * 7}, {dimension_y} + {chunkIndex * 7}, int(7), int(7))"
                    response_chunk.append(f"pygame.draw.rect({window_name}, {col_str}, {rect_str})")
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