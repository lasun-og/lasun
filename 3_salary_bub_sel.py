# Function for Selection Sort
def selection_sort(sal):
    n = len(sal)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if sal[j] < sal[min_index]:
                min_index = j
        sal[i], sal[min_index] = sal[min_index], sal[i]
    return sal


# Function for Bubble Sort
def bubble_sort(sal):
    n = len(sal)
    for i in range(n):
        for j in range(0, n - i - 1):
            if sal[j] > sal[j + 1]:
                sal[j], sal[j + 1] = sal[j + 1], sal[j]
    return sal


# Function to display top 5 salaries
def display_top_five(sorted_salaries):
    print("\nTop five highest salaries in the company:")
    for salary in sorted_salaries[-1:-6:-1]:
        print(f"₹{salary:.2f}")


# -------- Main Program --------

salaries = []

print("****** PRACTICAL NO-03(A-3) LIBRARY INFORMATION ******")
print("******** Prepared By : NANDINI MATE *************")

n = int(input("Enter total number of employees: "))

# Accepting salaries
for i in range(n):
    sal = float(input(f"Enter salary of employee {i + 1}: "))
    salaries.append(sal)

print("\nEntered Salaries:", salaries)

# Menu Display
while True:
    print("\n--- SORT MENU ---")
    print("1. Selection Sort")
    print("2. Bubble Sort")
    print("3. Top 5 (Selection Sort)")
    print("4. Top 5 (Bubble Sort)")
    print("5. Exit")

    ch = int(input("Enter your choice: "))

    # Selection Sort
    if ch == 1:
        sorted_salaries = selection_sort(salaries.copy())
        print("\n***** SELECTION SORT *****")
        print("Sorted Salaries:", sorted_salaries)

    # Bubble Sort
    elif ch == 2:
        sorted_salaries = bubble_sort(salaries.copy())
        print("\n***** BUBBLE SORT *****")
        print("Sorted Salaries:", sorted_salaries)

    elif ch == 3:
        print("\nTop five salaries from selection sort:")
        sorted_salaries = selection_sort(salaries.copy())
        display_top_five(sorted_salaries)

    elif ch == 4:
        print("\nTop five salaries from bubble sort:")
        sorted_salaries = bubble_sort(salaries.copy())
        display_top_five(sorted_salaries)

    elif ch == 5:
        print("Thank you! Exiting program.")
        break

    else:
        print("Invalid choice! Please try again.")

