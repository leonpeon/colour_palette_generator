import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

img = Image.open("test_image.jpg").convert("RGB")
img_array = np.array(img)

pixels = img_array.reshape(-1, 3)
pixels = (pixels // 32) * 32
values, frequencies = np.unique(
    pixels,
    axis=0,
    return_counts=True
)

frequency = dict(zip(map(lambda colour: tuple(map(int, colour)), values), map(int, frequencies)))
pixel_frequency = dict(
    sorted(frequency.items(), key=lambda item: item[1], reverse=True)
)

for colour, frequency in list(pixel_frequency.items())[:10]:
    hex_colour = "#{:02X}{:02X}{:02X}".format(*colour)
    print(f"Colour: {hex_colour} - {frequency}")

# plt.imshow(img)
# plt.show()