def hello(name):
    print(f"Hello {name}!")

def pack(food_0, food_1, food_2):
    return [food_0, food_1, food_2]

def eat_lunch(lunch_items):
    if len(lunch_items) == 0:
        print("My lunchbox is empty")
    else:
        for index in range(len(lunch_items)):
            if index == 0:
                print(f"First I eat {lunch_items[index]}")
            else:
                print(f"Then I eat {lunch_items[index]}")

hello("Hayley")
print(pack("watermelon", "sandwich", "cake"))

eat_lunch(pack("watermelon", "sandwich", "cake"))