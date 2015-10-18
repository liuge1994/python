import Image

im = Image.open('/home/liuge/python/1.jpg')

w, h = im.size

im.thumbnail(( w//2, h//2))

im.save('/home/liuge/python/1.jpg')

