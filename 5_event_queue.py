# FUNCTION TO ADD EVENT
def addEvent(event):
    eventQueue.append(event)
    print(f"EVENT '{event}' ADDED TO THE QUEUE.\n")


# FUNCTION TO PROCESS EVENT
def processEvent():
    if eventQueue:
        event = eventQueue[0]
        eventQueue.pop(0)
        print(f"EVENT '{event}' PROCESSED AND REMOVED FROM THE QUEUE.\n")
    else:
        print("NO EVENTS TO PROCESS!!!\n")


# FUNCTION TO DISPLAY PENDING EVENTS
def displayEvents():
    if eventQueue:
        print("PENDING EVENTS IN QUEUE:")
        for e in eventQueue:
            print(f"- {e}")
    else:
        print("NO PENDING EVENTS IN QUEUE.\n")


# FUNCTION TO CANCEL EVENT
def cancelEvent(event):
    if event in eventQueue:
        eventQueue.remove(event)
        print(f"EVENT '{event}' CANCELED SUCCESSFULLY.\n")
    else:
        print(f"EVENT '{event}' NOT FOUND OR ALREADY PROCESSED.\n")


# ----- MAIN PROGRAM -----
eventQueue = []

print("***** PRACTICAL NO-02(B-2) EVENT PROCESSING SYSTEM *****")
print("*********** Prepared By: NANDINI MATE **********")

while True:
    print("\n****** REAL-TIME EVENT PROCESSING SYSTEM USING QUEUE ********")
    print("1. ADD NEW EVENT")
    print("2. PROCESS NEXT EVENT")
    print("3. DISPLAY PENDING EVENTS")
    print("4. CANCEL AN EVENT")
    print("5. EXIT")

    ch = int(input("\nENTER YOUR CHOICE: "))

    if ch == 1:
        event = input("ENTER EVENT NAME TO ADD: ")
        addEvent(event)

    elif ch == 2:
        processEvent()

    elif ch == 3:
        displayEvents()

    elif ch == 4:
        event = input("ENTER EVENT NAME TO CANCEL: ")
        cancelEvent(event)

    elif ch == 5:
        print("\nTHANK YOU!!!!")
        break

    else:
        print("INVALID CHOICE!!!!\n")


