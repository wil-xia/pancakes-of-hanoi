# William Xia
# 10/9/23
# Assignment 2: Informed Search 

# This program searches for the best path to flip a set of pancakes 
# (integers 1-10) by inserting a "spatula" at any point in the stack and
# flipping all pancakes above it.

import random
import heapq

#print the stack as an array
def printStack(stack):
    print("Pancake stack order (Top to Bottom): ")
    for pancake in stack:
        print(str(pancake)+" ", end="")
    print("")

#print the pancake stack as ascii art using - and |
def prettyPrintStack(stack):
    for pancake in stack:
        print("   ",end="")
        for j in range(1,abs(10-pancake),2):
            print(" ",end="")
        print("|", end="")
        for i in range(1,pancake+1):
            print("-", end="")
        print("|")
    #print the plate
    for i in range(18):
        print("\u2588",end="")
    print("")

#print 2 pancakes next to eachother, print a flip message at a certain stack level
def print2Stacks(stack1, stack2, solution):
    n = len(stack1)
    for i in range(n):
        pancake1 = stack1[i]
        print("   ", end="")
        for j in range(1, abs(10 - pancake1), 2):
            print(" ", end="")
        print("|", end="")
        for k in range(1, pancake1 + 1):
            print("-", end="")
        print("|", end="")
        for j in range(1, abs(10 - pancake1), 2):
            print(" ", end="")
        if(i+1 == solution):
            print("  Flip at "+ str(solution)+" ->",end="")
        else:
            print("              ", end="")

        pancake2 = stack2[i]
        print("   ", end="")
        for l in range(1, abs(10 - pancake2), 2):
            print(" ", end="")
        print("|", end="")
        for m in range(1, pancake2 + 1):
            print("-", end="")
        print("|")

    for i in range(18):
        print("\u2588", end="")
    print("          ", end="")
    for i in range(18):
        print("\u2588", end="")
    print("")

#print the entire flip process of a pancake stack
def flipAnimation(stack, solution):
    n = len(solution)
    tempStack = stack

    for i in range(n):
        flipped = flipStack(tempStack,solution[i])
        print2Stacks(tempStack, flipped, solution[i])
        tempStack = flipStack(tempStack,solution[i])
        print("")
        
#calculate the number of adjacent +1/-1 stacks
def gapHeuristic(stack):
    count = 0
    n = len(stack)
    for i in range(n-1):
        currPancake = stack[i]
        nextPancake = stack[i+1]
        if not((currPancake == nextPancake+1)or(currPancake == nextPancake-1)):
            count += 1
    return count

#This function returns a copy of the array flipped an integer distance from the
#top. The flip is inclusive. (Ex: if you say 3, the top 3 items are flipped)
def flipStack(stack, flip_location):
    return stack[:flip_location][::-1] + stack[flip_location:]

#Check if the stack is in chronological order (flipped)
def isSorted(stack):
    if (all(stack[i] <= stack[i + 1] for i in range(len(stack) - 1))):
        return True
    return False

#Find best path to solution using heuristic
def aStarSolution(stack):
    print("Calculating best path to proper flippage...")
    #Each tuple contains (cost, state, path). These tuples will populate prio-q
    #Cost starts at 0
    queue = [(0, stack, [])] 

    #Store visited tuples here
    visited = set()

    print("Nodes explored: ",end="")
    nodes = 0

    while queue:
        nodes += 1
        #remove the lowest cost option using heapq.pop
        cost, state, path = heapq.heappop(queue)

        #if sorted, terminate and return sequence of flips to reach the destination
        if isSorted(state):
            print(nodes)
            return path 
        
        #add current tuple to the visited set
        visited.add(tuple(state))

        #scan all possible flip positions and add their data to the queue
        for k in range(2, len(state) + 1):
            new_state = flipStack(state, k)

            #if the pancake config is already in the system, skip
            if tuple(new_state) not in visited:
                #calculate new cost and new path, add new
                # +1 cost for each node (backward cost)
                new_cost = cost + 1 + gapHeuristic(new_state)
                new_path = path + [k]
                heapq.heappush(queue, (new_cost, new_state, new_path))

#Find best path to solution using UCS
def UniformCostSolution(stack):
    print("Calculating best path to proper flippage (no heuristic, this might take a while) ...")
    #Each tuple contains (cost, state, path). These tuples will populate prio-q
    #Cost starts at 0
    queue = [(0, stack, [])] 

    #Store visited tuples here
    visited = set()

    print("Nodes explored: ",end="")
    nodes = 0

    while queue:
        nodes += 1
        #remove the lowest cost option using heapq.pop
        cost, state, path = heapq.heappop(queue)

        #if sorted, terminate and return sequence of flips to reach the destination
        if isSorted(state):
            print(nodes)
            return path 
        
        #add current tuple to the visited set
        visited.add(tuple(state))

        #scan all possible flip positions and add their data to the queue
        for k in range(2, len(state) + 1):
            new_state = flipStack(state, k)

            #if the pancake config is already in the system, skip
            if tuple(new_state) not in visited:
                #Here's the different from A*, no heuristic function used. Just +1 cost per flip
                #calculate new cost and new path, add new
                #no need to have the queue check if duplicate states have different paths, since
                #the duplicate state will always have a higher cost than the original
                new_cost = cost + 1
                new_path = path + [k]
                heapq.heappush(queue, (new_cost, new_state, new_path))


#### User input and program main ####
while True:
    while True:
        try:
            init_method = int(input("Enter init method for the pancake stack, [1] for Random, [2] for Manual: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer 1 or 2.")
            print("")
    print("")
    if(init_method == 1):
        pancake_stack = list(range(1, 11))
        random.shuffle(pancake_stack)
    else:
        pancake_stack = []
        print("Pancakes will be inserted Top to Bottom")
        for i in range(10):
            while True:
                try:
                    user_input = int(input(f"Enter pancake {i+1} size: "))
                    if((user_input > 10)or(user_input < 1)):
                        print("Invalid pancake size, please enter an integer 1-10")
                        print("")
                    # elif(user_input in pancake_stack):
                    #     print("Please enter a size you haven't entered yet")
                    #     print("You've entered: ",end="")
                    #     for p in pancake_stack:
                    #         print(str(p)+" ",end="")
                    #     print("")
                    #     print("")
                    else:
                        pancake_stack.append(user_input)
                        break
                except ValueError:
                    print("Invalid input. Please enter an integer 1-10.")
                    print("")
        print("")



    printStack(pancake_stack)
    print("")
    prettyPrintStack(pancake_stack)
    print("")
    print("The current value of the gap Heuristic of your stack is "+str(gapHeuristic(pancake_stack)))
    print("")

    while True:
        try:
            search_method = int(input("Would you like to use A* using the gap heuristic [1] or Uniform Cost Search [2] to find the flip solution? \n(Please note that UCS may timeout on stacks with a heuristic greater than 5): "))
            if((search_method > 2)or(search_method < 1)):
                print("Invalid input. Please enter an integer 1 or 2.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter an integer 1 or 2.")
            print("")

    print("")
    if(search_method == 1):
        solution = aStarSolution(pancake_stack)
        print("Optimal flips to acheive proper stack, in order:" + str(solution))
    else:
        solution = UniformCostSolution(pancake_stack)
        print("Optimal flips to acheive proper stack, in order:" + str(solution))
    print("Total flips: " + str(len(solution)))
    print("")

    while True:
        try:
            option = int(input("Would you like to print visual demonstration of the solution [1], generate another pancake stack [2], \nor exit the program [3]: "))
            if((option > 3)or(option < 1)):
                print("Invalid input. Please enter an integer 1 or 2.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter an integer 1, 2, or 3.")
            print("")
    print("")

    if(option == 1):
        flipAnimation(pancake_stack,solution)
        print("")
    elif(option == 3):
        print("Goodbye!")
        break