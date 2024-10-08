import random
# 1. Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
def shuffle_list(input_list):
    shuffled_list = input_list.copy()
    random.shuffle(shuffled_list)
    return shuffled_list
print(shuffle_list([1,2,3,4,5,6,7,8]))

# 2. Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique
def seven_random_numbers():
    return random.sample(range(0,10), 7)
print(seven_random_numbers())