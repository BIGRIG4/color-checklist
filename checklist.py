checklist = list()

def create(item):
    checklist.append(item)
    return

def read(index):
    item = checklist[index]
    return item

def update(index, item):
    checklist[index] = item

def destroy(index):
    checklist.pop(index)
    return

def list_all_items():
    index = 0
    for list_item in checklist:
        print(str(index) + list_item)
        index += 1
    while condition:
        running = True

def mark_completed(index):

    return

def select(function_code):
    if function_code == "C":
        input_item = user_input("Input item:")
        create(input_item)
    elif function_code == "R":
        item_index = user_input("Index Number?")
    elif function_code == "P":
        list_all_items()
    else:
        print("Unknown Option")

def user_input(prompt):
    user_input = input(prompt)
    return user_input
user_value = user_input
print(user_value)


def test():
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")
    destroy(1)

    print(read(0))
    print(read(1))

    test()

running = True

while running:
    selection = user_input(
        "Press C to add to list, R to Read from list and P to display list >")
running = select(selection)
