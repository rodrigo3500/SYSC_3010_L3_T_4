import buttonControl.py as buttonControl

# Number of persons currently in the room 
currentOccupants = 0

# Max number of persons allowed in the room, default is 5
maxCapacity = 5

# update the roop capacity based on user Input
def updateCapacity():
    global maxCapacity
    userInput = buttonControl.readButtonInputs()
    if(userIput is buttonControl.increaseCapacity):
        maxCapacity = maxCapacity + 1
    elif(userInput is buttonControl.decreaseCapacity):
        maxCapacity = maxCapacity - 1

def increaseOccupants():
    global currentOccupants
    currentOccupants = currentOccupants + 1

def decreaseOccupants():
    global currentOccupants
    currentOccupants = currentOccupants - 1


