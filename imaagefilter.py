import Image, ImageFilter

im = Image.open('/home/liuge/python/test.jpg')
im2 = im.filter(ImageFilter.BLUR)
im2.save('/home/liuge/python/blur.jpg', 'jpeg')

