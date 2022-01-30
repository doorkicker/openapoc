from PIL import Image

h_key = Image.open("elevations2.bmp")
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
px = None
while i < w:
	j = 0
	while j < h:
		px = h_key.getpixel((i, j))
		#if px != (28, 44, 168) and px != (12, 14, 156):
		if px != (28, 44, 168) and px != (12, 14, 156) and px != (44, 74, 180):
			#print(f"match! i: {i}, j: {j}")
			img_out.putpixel((i, j), world_map.getpixel((i, j)))
			#img_out.putpixel((i, j), (0, 0, 0))
		j = j + 1
	i = i + 1

#when we're done save the output image

h_key.close()
world_map.close()
img_out.save("world_no_ocean.bmp")
img_out.close()