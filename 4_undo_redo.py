# Main Program
undo_stack = []
redo_stack = []
current_text = ""


def type_text(char):
    global current_text
    undo_stack.append(current_text)
    current_text += char
    redo_stack.clear()
    print("Current Text:", current_text)


def undo():
    global current_text
    if undo_stack:
        redo_stack.append(current_text)
        current_text = undo_stack.pop()
        print("Undo Done. Current Text:", current_text)
    else:
        print("Nothing to undo.")


def redo():
    global current_text
    if redo_stack:
        undo_stack.append(current_text)
        current_text = redo_stack.pop()
        print("Redo Done. Current Text:", current_text)
    else:
        print("Nothing to redo.")


while True:
    print("\n1. Type Text")
    print("2. Undo")
    print("3. Redo")
    print("4. Show Text")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        char = input("Enter character to type: ")
        type_text(char)

    elif choice == '2':
        undo()

    elif choice == '3':
        redo()

    elif choice == '4':
        print("Current Text:", current_text)

    elif choice == '5':
        print("Thank you!")
        break

    else:
        print("Invalid choice.")

