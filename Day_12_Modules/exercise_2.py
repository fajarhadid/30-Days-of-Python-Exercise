import random
# 1. Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples)
def list_of_hexa_colors(num):
    hexas = []
    for i in range(num):
        hexa = f'#{random.randint(0, 0xFFFFFF):06x}'
        hexas.append(hexa)
    return hexas
print(list_of_hexa_colors(3))

# 2. Write a function list_of_rgb_colors which returns any number of RGB colors in an array
def list_of_rgb_colors(num):
    rgbs = []
    for i in range(num):
        r = random.randrange(0, 256)
        g = random.randrange(0, 256)
        b = random.randrange(0, 256)
        rgb = f'rgb({r}, {g}, {b})'
        rgbs.append(rgb)
    return rgbs
print(list_of_rgb_colors(2))

# 3. Write a function generate_colors which can generate any number of hexa or rgb colors
def generate_colors(color, num_of_color):
    if color == 'hexa':
        hexas = list_of_hexa_colors(num_of_color)
        print(hexas)
    else:
        rgbs = list_of_rgb_colors(num_of_color)
        print(rgbs)
generate_colors('hexa', 4)
generate_colors('rgb', 4)
    