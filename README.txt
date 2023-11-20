# William Xia
# 10/9/23
# Assignment 2: Informed Search README

HOW TO RUN:

Open command prompt and switch to the directory containing the pancake.py
Type python main.py in the command line

The program will prompt you to generate a pancake stack and choose your search
method. You can type 1 or 2 into the command line and then enter pancake sizes into
the command line.

To a view a generated animation of your pancake stack, enter 1 into the command line
when it prompts you.

ASSUMPTIONS:
In the A* search, each flip is considered to have a backward cost of 1. The 
actual cost of each flip is determined by the heuristic. The total cost per 
flip is heuristic + 1

In the UCS search, each flip is considered to have a cost of 1. 

The ordering of the pancakes is top to bottom, meaning the first index of the 
array is the top. A perfectly solved stack would be (1,2,3,4,5,6,7,8,9,10)