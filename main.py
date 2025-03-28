from PIL import Image, ImageOps

image = Image.open('monro.jpg')

red, green, blue = image.split()

cropped_r = red.crop((100, 0, red.width, red.height))
cropped_re = red.crop((50, 0, red.width - 50, red.height))

Image.blend(cropped_r, cropped_re, 0.2)

cropped_b = blue.crop((0, 0, blue.width - 100, blue.height)) 
cropped_bl = blue.crop((50, 0, blue.width - 50, blue.height))

Image.blend(cropped_b, cropped_bl, 0.5)

cropped_g = green.crop((50, 0, green.width - 50, green.height))

new_image = Image.merge('RGB', (Image.blend(cropped_r, cropped_re, 0.2), cropped_g, Image.blend(cropped_b, cropped_bl, 0.5))).save('new.jpg')

image_new = Image.open('new.jpg')
image_new.thumbnail((80, 80))
