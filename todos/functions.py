
FILEPATH = "todos.txt"

# todos = []  # Not needed if using a list comprehension which produces a new list
def get_todos(filepath=FILEPATH):
    """ Return the todo items list from the text file located at filepath """
    try:
        with open(filepath, "r") as fn_local:
            todos_local = fn_local.readlines()
            """ Using a list comprehension to strip \n from each line """
            # todos_local = [line.strip('\n') for line in todos_local]
        # print(todos_local)
        return todos_local
    except FileNotFoundError as e:
        print(e, "todos.txt file not found")


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the todo items list to the text file located at filepath """
    with open(filepath, 'w') as fn:
        fn.writelines(todos_arg)

""" This code runs when importing functions.py OR running this module directly"""
print("This message is from functions.py but is outside of any functions which makes it global")

""" The following code ONLY executes when running functions.py directly"""
""" This concept is explained in lesson # 135 """
if __name__ == "__main__":
    print("hello from functions")
    print(get_todos())
