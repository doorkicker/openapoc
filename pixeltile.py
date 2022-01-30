from PIL import Image

h_key = Image.open("elevations.bmp")
world_map = Image.open("biomes.bmp")
w, h = h_key.size
#Now look through h_key, and if the pixel at [i][j] is NOT a 'water' pixel, then copy
#the corresponding at pixel [i][j] in world_map, and save it at [i][j] into a new image
hkey_px = h_key.load()
world_px = world_map.load()
img_out = Image.new("RGB", (w, h), (100, 0, 100))
img_px = img_out.load()

i = 0
j = 0
while i < w:
	j = 0
	while j < h:
		#if hkey_px.getpixel([i, j]) != (232, 182, 98) and hkey_px.getpixel([i, j]) != (239, 219, 84):
		if h_key.getpixel((i, j)) != (232, 182, 98) and h_key.getpixel((i, j)) != (239, 219, 84):
			pass
		j = j + 1
	i = i + 1

#when we're done save the output image

h_key.close()
world_map.close()