PATH = './BOULEVARD'
vapers_path = PATH + '/vapers'
candy_path = PATH + '/candy'
weed_path = PATH + '/weed'
image_path = PATH + '/Asset-2.jpeg'
video_path = PATH + '/oreo_blizzard.mp4'
video_bye = PATH + '/smk-g.mp4'
image_bye = PATH + '/GFgEEU-WUAExx4B.jpeg'

# Vapers
# vaper1 = vapers_path + 'vaper1.png'
# vaper_images = [f'{vapers_path}/vaper{i}.png' for i in range(1, 6)]
# vaper_images_jpeg = [f'{vapers_path}/vaper{i}.jpeg' for i in range(6, 11)]
# vaper_images.extend(vaper_images_jpeg)

vaper_images = [f'{vapers_path}/vaper{i}.jpg' for i in range(1, 6)]
vaper_images2m = [f'{vapers_path}/vap{i}.jpg' for i in range(7, 14)]
vaper_images.extend(vaper_images2m)

# Candies:
# candy1 = candy_path + 'candy1.jpeg'
candy_images = [f'{candy_path}/candy{i}.jpeg' for i in range(1, 5)]

# Weed
# weed1 = weed_path + '/weed1.jpg'
weed_images = [f'{weed_path}/weed{i}.jpg' for i in range(1, 6)]