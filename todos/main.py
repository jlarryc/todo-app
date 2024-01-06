

# from functions import get_todos, write_todos
import functions
import time

today = time.asctime()
print(today)
now = time.strftime("%Y%m%d%I%p%M%S")
print(now)
now = time.strftime("%b %d, %Y %H:%M:%S")
print(f"It is {now}")

while True:
    user_action = input("Type add, show, edit, complete, delete or exit:")
    user_action = user_action.strip()  # strip any unexpected spaces

    if user_action.startswith("add"):
        todo = user_action[4:]
        todos = functions.get_todos()
        todos.append(f"{todo}\n")
        # print("TODOS", todos)

        functions.write_todos(todos)

    elif user_action.startswith("show"):
        todos = functions.get_todos("todos.txt")
        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index + 1}. {item}")

    elif user_action.startswith('edit'):
        try:
            my_num = int(user_action[5:])
            todos = functions.get_todos()
            for index, item in enumerate(todos):
                item = item.strip('\n')
                print(f"{index + 1}. {item}")
            new_todo = input("Change your todo: ")
            todos[my_num - 1] = new_todo + '\n'
            # with open('todos.txt', 'w') as fn:
            #     fn.writelines(todos)
            functions.write_todos(todos)

        except ValueError:
            print("Error in command. Should be: edit n (where 'n' is the number of the todo to edit)")
            continue
        except IndexError:
            print("Error in command.  A number was given that is out of range.")
            continue

    elif user_action.startswith('complete'):
        try:
            my_num = int(user_action[9:])
            todos = functions.get_todos()
            todos[my_num - 1] = "X " + todos[my_num - 1]
            # with open('todos.txt', 'w') as fn:
            #     fn.writelines(todos)
            functions.write_todos(todos)
        except ValueError:
            print("Error in command. Should be: complete n (where 'n' is the number of the todo to mark as complete)")
            continue
        except IndexError:
            print("Error in command.  A number was given that is out of range.")
            continue

    elif user_action.startswith('delete'):
        try:
            my_num = int(user_action[7:])
            todos = functions.get_todos()
            message = f"Todo {todos[my_num - 1]} was removed from the list."  # NOT YET but soon
            todos.pop(my_num - 1)
            print(message)
            # with open('todos.txt', 'w') as fn:
            #     fn.writelines(todos)
            functions.write_todos(todos)
        except ValueError:
            print("Error in command. Should be: delete n (where 'n' is the number of the todo to delete)")
            continue
        except IndexError:
            print("Error in command.  A number was given that is out of range.")
            continue

    elif user_action.startswith('exit'):
        break  # or could user exit()
    else:  # _ is a common programmer convention for a default variable
        print("You entered an unknown command")
save_data = input("Save Data? y/n: ")
if save_data == 'y':
    with open('todos.txt', "w") as fn:
        for todo in todos:
            fn.writelines(f"{todo}\n")

# print("TODOS: ", todos)

print("Bye!")
