from PIL import Image
import numpy as np

all_letters = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`\'.            '
less_letters = '•••••••••      '
length = len(all_letters) # change if want less_letters


image = Image.open(input('file name : '))
width = int(input('width : '))


image = image.convert("L")


temp_width = image.width
temp_height = image.height

height = int(width * (temp_height / temp_width) * 0.5)

image = image.resize((width, height), Image.Resampling.LANCZOS)


img = np.array(image)
# text = []
for i in range(height):
    for j in range(width):
        brightness = img[i, j]
        if brightness == 256 :
            pos = 0
        else:
            _pos = int(np.floor(brightness / 256 * length))
            pos = length - 1 - _pos
        
        print(all_letters[pos], end = '') # change if want less_letters
        # text.append(all_letters[pos])

    print()
    # text.append('\n')

# with open('h.txt', 'w') as f:
#     f.write(''.join(text))



