# CREATE NODE
def createNode(value):
    return {"data": value, "left": None, "right": None}


# CONSTRUCT EXPRESSION TREE FROM PREFIX
def constructTree(prefix):
    stack = []
    # iterate prefix in reverse
    for symbol in prefix[::-1]:
        if symbol.isalpha() or symbol.isdigit():
            node = createNode(symbol)
            stack.append(node)
        else:
            # operator: pop two nodes (left, right)
            left = stack.pop()
            right = stack.pop()
            node = createNode(symbol)
            node["left"] = left
            node["right"] = right
            stack.append(node)
    return stack[-1] if stack else None


# POSTORDER TRAVERSAL (NON-RECURSIVE)
def postorderNonRecursive(root):
    if root is None:
        print("Tree is empty.")
        return

    stack1 = []
    stack2 = []
    stack1.append(root)
    while stack1:
        node = stack1.pop()
        stack2.append(node)
        if node["left"]:
            stack1.append(node["left"])
        if node["right"]:
            stack1.append(node["right"])

    print("POSTORDER TRAVERSAL (Non-Recursive):", end="  ")
    while stack2:
        node = stack2.pop()
        print(node["data"], end="  ")
    print()


# DISPLAY (INORDER)
def displayInorder(root):
    if root:
        displayInorder(root["left"])
        print(root["data"], end="  ")
        displayInorder(root["right"])


# DELETE TREE
def deleteTree(root):
    if root is None:
        return None
    deleteTree(root["left"])
    deleteTree(root["right"])
    print("Deleting node:", root["data"])
    root.clear()  # clear dict representing the node
    return None


# MAIN PROGRAM
prefix = "+--a*bc/def"
root = None

while True:
    print("\n****** PRACTICAL NO-11 (EXPRESSION TREE FROM PREFIX) ******")
    print("****** PREPARED BY : NANDINI N MATE ******")
    print("\n==== MENU ===")
    print("1. CONSTRUCT EXPRESSION TREE")
    print("2. DISPLAY (Inorder Traversal)")
    print("3. POSTORDER TRAVERSAL (Non-Recursive)")
    print("4. DELETE TREE")
    print("5. EXIT")

    choice = input("ENTER YOUR CHOICE: ").strip()

    if choice == "1":
        root = constructTree(prefix)
        print("Expression Tree constructed successfully for PREFIX:", prefix)

    elif choice == "2":
        if root:
            print("Inorder Traversal:", end="  ")
            displayInorder(root)
            print()
        else:
            print("Tree not constructed yet!")

    elif choice == "3":
        postorderNonRecursive(root)

    elif choice == "4":
        root = deleteTree(root)
        print("Tree deleted successfully!")

    elif choice == "5":
        print("THANK YOU!!!!")
        break

    else:
        print("INVALID CHOICE. PLEASE ENTER (1–5).")

