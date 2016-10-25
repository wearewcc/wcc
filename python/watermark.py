#import Image
from PIL import Image
#
# background = Image.open('photo.jpg')
# foreground = Image.open('woc.png')
#
# print background.size
# print foreground.size
#
# background.paste(foreground, (10, 10))
# background.save('photo-watermarked.jpg', quality=95)
# #pip install --upgrade --user pip
# #pip install Image --user


im = Image.open('photo.jpg')
im.thumbnail(200)
im.save('photo-thumb.jpg', "JPEG", quality=95)
