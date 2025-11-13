def average(lib):     
    total = sum(lib)     
    avg = total / len(lib) 
    print(f"\nTotal books borrowed: {total}")     
    print(f"Average books per student: {avg:.2f}") 
 
def highest(lib): 
    print("Maximum books borrowed by a student:", max(lib)) 
 
def lowest(lib): 
    print("Minimum books borrowed by a student:", min(lib)) 
 
def count_zero(lib):     
    count = lib.count(0) 
    print("Number of students who borrowed 0 books:", count) 
 
def most_frequent(lib): 
    freq_dict = {}     
    for num in lib: 
        if num in freq_dict:             
            freq_dict[num] += 1         
        else: 
            freq_dict[num] = 1 
 
    max_freq = 0     
    most_common = None     
    for num, freq in freq_dict.items(): 
        if freq > max_freq:             
            max_freq = freq 
            most_common = num 
 
    print(f"Most frequently borrowed book count: {most_common} (appears {max_freq} times)") 
 
# --- Main Program --- 
 
lib = [] 
n = int(input("Enter total number of students: ")) 
 
for i in range(n): 
    books = int(input(f"Books borrowed by student {i+1}: "))     
    lib.append(books) 
 
while True: 
    print("\n### LIBRARY MENU ###")  
    print("1. Average of books borrowed")   
    print("2. Highest number of books borrowed")     
    print("3. Lowest number of books borrowed")     
    print("4. Count of students who borrowed 0 books") 
    print("5. Most frequent number of books borrowed")     
    print("6. Exit") 
 
    choice = int(input("Enter your choice (1-6): ")) 
 
    if choice == 1:         
        average(lib)     
    
    elif choice == 2:         
        highest(lib)     
    
    elif choice == 3:         
        lowest(lib)     
    
    elif choice == 4:         
        count_zero(lib)     
    
    elif choice == 5: 
        most_frequent(lib)     

    elif choice == 6: 
        print("Program exited.") 
        break     

    else: 
        print("Invalid choice! Please try again.")
