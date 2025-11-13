# Function for Linear Search 

def linear(b): 
    key = int(input("Enter the element to be searched: "))     

    for i in range(len(b)): 
        if key == b[i]: 
            return i     

    return -1 
 
# Function for Binary Search 

def binary(b, low, high, key):     

    if high >= low: 
        mid = (low + high) // 2         

        if b[mid] == key: 
            return mid         

        elif b[mid] > key: 
            return binary(b, low, mid - 1, key) 
        
        else:             

            return binary(b, mid + 1, high, key)     
    
    return -1 
 
# Main Program 

ecom = [] 
tid = int(input("Enter total number of account holders: ")) 
 
# Accepting account IDs 

for i in range(tid): 
    aid = int(input(f"Enter account ID for client {i + 1}: ")) 
    ecom.append(aid) 
 
print("Entered Account IDs:", ecom) 
 
# Menu Display 
while True: 
    print("\n--- SEARCH MENU ---")     
    print("1. Linear Search")   
    print("2. Binary Search (sorted list)")     
    print("3. Exit") 
 
    ch = int(input("Enter your choice: ")) 
 
# Linear Search     
    if ch == 1: 
        r = linear(ecom)         
        print("\n***** LINEAR SEARCH *****") 
        if r != -1: 
            print(f"Element found at index: {r+1}") 
        else: 
            print("Element not found!") 
 
    
    # Binary Search     
    elif ch == 2: 
        key = int(input("Enter the element to be searched: "))         
        sorted_ecom = sorted(ecom)  
        # Ensure the list is sorted         
        r = binary(sorted_ecom, 0, len(sorted_ecom) - 1, key)         

        print("\n***** BINARY SEARCH *****") 
        if r != -1: 
            print(f"Element found at index (in sorted list): {r+1}") 
        else: 
            print("Element not found!") 
    # Exit     
    elif ch == 3: 
        print("Thank you! Exiting program.")         
        break     
    
    else: 
        print("Invalid choice! Please try again.") 
