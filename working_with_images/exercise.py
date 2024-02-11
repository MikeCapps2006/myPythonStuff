from PIL import Image

matrix = Image.open('word_matrix.png')
mask = Image.open('mask.png')


#print(matrix.size)
#1015, 559
#print(mask.size)
#505, 251


#mask.resize((1015, 559)).save('new_mask.png')

new_mask = Image.open('new_mask.png')
new_mask.putalpha(200)
matrix.paste(new_mask, box=(0,0), mask=new_mask)
matrix.show()






