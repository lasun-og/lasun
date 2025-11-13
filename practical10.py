# CREATE NODE
def createNode(key):
    return {"key": key, "left": None, "right": None}


# INSERT NODE
def insert(root, key):
    if root is None:
        return createNode(key)

    if key < root["key"]:
        root["left"] = insert(root["left"], key)
    elif key > root["key"]:
        root["right"] = insert(root["right"], key)
    else:
        print("Duplicate key not allowed:", key)
    return root


# SEARCH NODE
def search(root, key):
    if root is None:
        print("Key not found:", key)
        return None
    if root["key"] == key:
        print("Key found:", key)
        return root
    elif key < root["key"]:
        return search(root["left"], key)
    else:
        return search(root["right"], key)


# FIND MINIMUM NODE
def minValueNode(node):
    current = node
    while current["left"] is not None:
        current = current["left"]
    return current


# DELETE NODE
def delete(root, key):
    if root is None:
        print("Key not found, cannot delete:", key)
        return root

    if key < root["key"]:
        root["left"] = delete(root["left"], key)
    elif key > root["key"]:
        root["right"] = delete(root["right"], key)
    else:
        # Node with only one child or no child
        if root["left"] is None:
            temp = root["right"]
            root = None
            return temp
        elif root["right"] is None:
            temp = root["left"]
            root = None
            return temp

        # Node with two children: get the inorder successor
        temp = minValueNode(root["right"])
        root["key"] = temp["key"]
        root["right"] = delete(root["right"], temp["key"])
    return root


# DISPLAY TRAVERSALS
def inorder(root):
    if root:
        inorder(root["left"])
        print(root["key"], end=" ")
        inorder(root["right"])


def preorder(root):
    if root:
        print(root["key"], end=" ")
        preorder(root["left"])
        preorder(root["right"])


def postorder(root):
    if root:
        postorder(root["left"])
        postorder(root["right"])
        print(root["key"], end=" ")


# MAIN PROGRAM
root = None

while True:
    print("\n****** PRACTICAL NO-10 (BINARY SEARCH TREE OPERATIONS) ******")
    print("****** PREPARED BY : NANDINI N MATE ******")
    print("\n==== MENU ===")
    print("1. INSERT NODE")
    print("2. DELETE NODE")
    print("3. SEARCH NODE")
    print("4. DISPLAY TREE (Inorder, Preorder, Postorder)")
    print("5. EXIT")

    choice = input("ENTER YOUR CHOICE: ").strip()

    if choice == "1":
        key = int(input("ENTER VALUE TO INSERT: "))
        root = insert(root, key)
        print("Node inserted:", key)

    elif choice == "2":
        key = int(input("ENTER VALUE TO DELETE: "))
        root = delete(root, key)

    elif choice == "3":
        key = int(input("ENTER VALUE TO SEARCH: "))
        search(root, key)

    elif choice == "4":
        print("\nINORDER  (LNR): ", end="")
        inorder(root)
        print("\nPREORDER (NLR): ", end="")
        preorder(root)
        print("\nPOSTORDER (LRN): ", end="")
        postorder(root)
        print()

    elif choice == "5":
        print("THANK YOU!!!!")
        break

    else:
        print("INVALID CHOICE. PLEASE ENTER (1–5).")

