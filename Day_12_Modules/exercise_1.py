import string, random
# 1. Write a function which generates a six digit/character random_user_id. 
def random_user_id():
    char = string.ascii_letters + string.digits
    random_user_id = ''.join(random.choice(char) for i in range(6))
    return random_user_id
print(random_user_id())

# 2. Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated
def user_id_gen_by_user():
    num_of_char = int(input("Enter the number of characters: "))
    num_of_id = int(input("Enter the number of ID: "))
    char = string.ascii_letters + string.digits
    for i in range(num_of_id):
        random_user_id = ''.join(random.choice(char) for c in range(num_of_char))
        print(random_user_id)
user_id_gen_by_user()

# 3. Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each)
def rgb_color_gen():
    r = random.randrange(0, 256)
    g = random.randrange(0, 256)
    b = random.randrange(0, 256)
    print(f"rgb({r}, {g}, {b})")
rgb_color_gen()