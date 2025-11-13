def hashFuction(k, size):
    return k % size


def insert(k, v):
    size = len(ht)
    index = hashFuction(k, size)

    # Check if key already exists
    for pair in ht[index]:
        if pair[0] == k:
            print("KEY ALREADY EXISTS AT INDEX", index, "→ Updating value")
            pair[1] = v
            return

    # Insert new key-value pair
    ht[index].append([k, v])
    print("KEY INSERTED AT INDEX", index)


def search(k):
    size = len(ht)
    index = hashFuction(k, size)

    for pair in ht[index]:
        if pair[0] == k:
            print("KEY FOUND AT INDEX", index, "→ Value:", pair[1])
            return
    print("KEY NOT FOUND.")


def delete(k):
    size = len(ht)
    index = hashFuction(k, size)

    for pair in ht[index]:
        if pair[0] == k:
            ht[index].remove(pair)
            print("KEY DELETED FROM INDEX", index)
            return
    print("KEY NOT FOUND, CANNOT DELETE.")


def display():
    print("\nHASH TABLE:")
    for i in range(len(ht)):
        print(f"INDEX {i}: {ht[i]}")
    print()


# MAIN PROGRAM
size = int(input("ENTER SIZE OF HASH TABLE: "))
ht = [[] for _ in range(size)]  # initialize with empty lists for chaining

while True:
    print("\n****** PRACTICAL NO-08 (C-2) HASHING ******")
    print("****** PREPARED BY : NANDINI N. MATE ******")
    print("\n==== MENU ===")
    print("1. INSERT")
    print("2. SEARCH")
    print("3. DELETE")
    print("4. DISPLAY")
    print("5. EXIT")

    choice = input("ENTER YOUR CHOICE: ")

    if choice == "1":
        k = int(input("ENTER KEY TO INSERT: "))
        v = input("ENTER VALUE TO INSERT: ")
        insert(k, v)

    elif choice == "2":
        k = int(input("ENTER KEY TO SEARCH: "))
        search(k)

    elif choice == "3":
        k = int(input("ENTER KEY TO DELETE: "))
        delete(k)

    elif choice == "4":
        display()

    elif choice == "5":
        print("THANK YOU!!!!")
        break

    else:
        print("INVALID CHOICE! PLEASE ENTER (1–5).")


