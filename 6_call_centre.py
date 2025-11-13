# FUNCTION TO ADD CALL
def addCall(customerId, callTime):
    callQueue.append((customerId, callTime))
    print(f"CALL FROM CUSTOMER '{customerId}' WITH TIME {callTime} MIN ADDED TO THE QUEUE.\n")


# FUNCTION TO ANSWER CALL
def answerCall():
    if callQueue:
        customerId, callTime = callQueue.pop(0)
        print(f"ANSWERING CALL FROM CUSTOMER '{customerId}' WITH TIME {callTime} MIN.\n")
    else:
        print("NO CALLS TO ANSWER!!!\n")


# FUNCTION TO VIEW CALL QUEUE
def viewQueue():
    if callQueue:
        print("CURRENT CALLS IN QUEUE:")
        for cid, ctime in callQueue:
            print(f"- Customer ID: {cid}, Call Time: {ctime} min")
    else:
        print("NO CALLS IN QUEUE.\n")


# FUNCTION TO CHECK IF QUEUE IS EMPTY
def isQueueEmpty():
    if not callQueue:
        print("YES, CALL QUEUE IS EMPTY.\n")
    else:
        print("NO, CALL QUEUE HAS PENDING CALLS.\n")


# MAIN PROGRAM
callQueue = []

print("***** PRACTICAL NO-06(B-3) CALL CENTER QUEUE SYSTEM *****")
print("*********** Prepared By: NANDINI MATE **********")

while True:
    print("\n****** CALL CENTER QUEUE MANAGEMENT SYSTEM ********")
    print("1. ADD CALL")
    print("2. ANSWER NEXT CALL")
    print("3. VIEW CALL QUEUE")
    print("4. IS QUEUE EMPTY?")
    print("5. EXIT")

    ch = int(input("\nENTER YOUR CHOICE: "))

    if ch == 1:
        customerId = input("ENTER CUSTOMER ID: ")
        callTime = int(input("ENTER CALL TIME (in minutes): "))   # FIXED INPUT TYPE
        addCall(customerId, callTime)

    elif ch == 2:
        answerCall()

    elif ch == 3:
        viewQueue()

    elif ch == 4:
        isQueueEmpty()

    elif ch == 5:
        print("\nTHANK YOU!!!!")
        break

    else:
        print("INVALID CHOICE!!!!\n")
