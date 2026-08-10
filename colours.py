import numpy as np
from PIL import Image

class Colours:
    def __init__(self, image):
        self.img = Image.open(image).convert("RGB")
        self.img.thumbnail((300, 300))
        self.img.save(image, "JPEG")
        self.img_array = np.array(self.img)
        self.pixels = self.img_array.reshape(-1, 3)
        self.pixels = (self.pixels // 32) * 32
        self.values, self.frequencies = np.unique(
            self.pixels,
            axis=0,
            return_counts=True
        )
        self.frequency =  dict(zip(
            map(lambda colour: tuple(map(int, colour)), self.values), map(int, self.frequencies)
            ))
        self.pixel_frequency = dict(
            sorted(self.frequency.items(), key=lambda item: item[1], reverse=True)
        )

    def top_colours(self):
        top_ten_colours = []
        for colour in list(self.pixel_frequency)[:12]:
            hex_colour = "#{:02X}{:02X}{:02X}".format(*colour)
            top_ten_colours.append(hex_colour)
        return top_ten_colours