from PIL import Image


RESIZE = 48

img = Image.open('./icons/image2.JPEG')
new_img = img.resize((RESIZE, RESIZE))
new_img.save('./icons/Aimage2' + str(RESIZE) + '.JPEG')