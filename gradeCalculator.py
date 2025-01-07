def calculateGrade():
    # Implement your solution in between the two comment blocks
    print("Calculating Grade")
    # This first line is provided for you
    try:
        inRange = True
        hrs = float(input("Enter score:"))
        if hrs<0: inRange = False
        if hrs>1: inRange = False
    except: inRange = False
    if inRange == False: print("Bad score")
    else:
        if hrs >= 0.9: print("A")
        elif hrs >= 0.8: print("B")
        elif hrs >= 0.7: print("C")
        elif hrs >= 0.6: print("D")
        else: print("F")

    # end assignment

## If you want to test locally before you try to sync
## Run > python calculateGrade.py

if __name__ == "__main__":
    calculateGrade()
