from PIL import Image

computer = Image.open('example.jpg')

#<PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=1993x1257 at 0x101CF59D0>
print(computer)
#width, height
print(computer.size)
#example.jpg
print(computer.filename)
#JPEG (ISO 10918)
print(computer.format_description)

#Opens up the computer image in another app
#computer.show()
#Crops the picture and opens in another app
#computer.crop((0,0,100,100)).show()

pencils = Image.open('pencils.jpg')
x = 0
y = 0

#Graps about 10% in the y direction, and 3% in the x direction
w = 1950/3
h = 1300/10

#pencils.crop((x, y, w, h)).show()

x = 0 
y = 1100
w = 1950/3
h = 1300

#pencils.crop((x, y, w, h)).show()

#width: 1993, height: 1257
print(computer.size)

halfway = 1993/2

x = halfway - 200
w = halfway + 200

y = 800
h = 1257

mac = computer.crop((x, y, w, h))

computer.paste(im=mac, box=(0,0))

computer.paste(im=mac, box=(796,0))

h, w = computer.size

new_h = int(h/3)
new_w = int(w/3)

#computer.resize((new_h, new_w)).show()

#pencils.rotate(120).show()

red = Image.open('red_color.jpg')
im = Image.open("blue_color.png")
rgb_im = im.convert('RGB')
rgb_im.save('blue_color.jpg')
blue = Image.open('blue_color.jpg')

red.putalpha(128)
blue.putalpha(128)

blue.paste(red,box=(0,0),mask=red)
blue.save('purple.png')

purple = Image.open('purple.png')
purple.show()



