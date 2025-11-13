def hash_function(k, size):
    return k % size


def insert(k):
    size = len(ht)
    index = hash_function(k, size)

    for _ in range(size):
        if ht[index] == -1:
            ht[index] = k
            print("KEY INSERTED AT INDEX", index)
            return

        elif ht[index] == k:
            print("KEY ALREADY EXISTS AT INDEX", index)
            return

        else:
            index = (index + 1) % size

    print("HASH TABLE IS FULL")


def search(k):
    size = len(ht)
    index = hash_function(k, size)

    for _ in range(size):
        if ht[index] == -1:
            break

        elif ht[index] == k:
            print("KEY FOUND AT INDEX", index)
            return

        else:
            index = (index + 1) % size

    print("KEY NOT FOUND.")


def delete(k):
    size = len(ht)
    index = hash_function(k, size)

    for _ in range(size):
        if ht[index] == -1:
            break

        elif ht[index] == k:
            ht[index] = -1
            print("KEY DELETED FROM INDEX", index)
            return

        else:
            index = (index + 1) % size

    print("KEY NOT FOUND, CANNOT DELETE.")


def display():
    print("\nHASH TABLE:")
    for i in range(len(ht)):
        print(f"INDEX {i}: {ht[i]}")
    print()


# MAIN PROGRAM
size = int(input("ENTER SIZE OF HASH TABLE: "))
ht = [-1] * size

while True:
    print("****** PRACTICAL NO-08 (C-2) HASHING ******")
    print("****** PREPARED BY : NANDINI N MATE ******")
    print("\n==== MENU ===")
    print("1. INSERT")
    print("2. SEARCH")
    print("3. DELETE")
    print("4. DISPLAY")
    print("5. EXIT")

    choice = input("ENTER YOUR CHOICE: ")

    if choice == "1":
        k = int(input("ENTER KEY TO INSERT: "))
        insert(k)

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
        print("INVALID CHOICE PLEASE ENTER (1–5).")

