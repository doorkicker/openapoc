from PIL import Image

h_key = Image.open("elevations.bmp")
world_map = Image.open("biomes.bmp")
#Now look through h_key, and if the pixel at [i][j] is NOT a 'water' pixel, then copy
#the corresponding at pixel [i][j] in world_map, and save it at [i][j] into a new image
hkey_px = h_key.load()
world_px = world_map.load()

#when we're done save the output image

h_key.close()
world_map.close()