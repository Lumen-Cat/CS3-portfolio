Section: 9 Balingkilat                                      Score:____________

C# / Name: 19,20,21 / Bondoc, Carbungco, Cato               Date: 08/08/26


Scenario

The PSHS school canteen is small and often gets crowded during lunch break. Students line up to buy food, but the process is slow because:

Some students take too long to decide what to order.
The cashier has to calculate totals and give change manually.
There is no system to track which food items are running out.
Your group’s task is to decompose this problem into smaller, manageable parts that could be solved with computational thinking (CT) Skills.

Step 1: Identify the Big Problem

Main Problem: The transactions in the canteen are slow and inefficient.

Step 2: Identify three to four Sub-Problems
Please list possible sub-problems:

1. Some students take too long to decide what to order. ---  some students are indecisive

2. The cashier has to calculate totals and give change manually. --- manual calculations per checkout.

3. There is no system to track which food items are running out. --- no inventory registry to check available stock.

Step 3: Define Computational Thinking Approaches
For each sub-problem, apply CT skills:

Sub-Problem 1: 
CT Skill: Pattern Recognition | 
Example Solution: Post the menus digitally so students can view them anytime, more quickly and efficiently.

Sub-Problem 2:
CT Skill: Algorithmic Thinking | 
Example Solution: Make a program that automatically calculates the total cost and amount of change.

Sub-Problem 3:
CT Skill: Algorithmic Thinking |
Example Solution: Create a system that tracks the quantity of each item and automatically updates the stock after every purchase.

Step 4: Draw a flowchart or write pseudocode for the identified sub-problem
START

INPUT NumOfItems

SET TotalCost TO 0

REPEAT
	INPUT ItemPrice
	SET TotalCost TO TotalCost + ItemPrice
	SET NumOfItems TO NumOfItems - 1
UNTIL NumOfItems = 0
	
DISPLAY TotalCost
	
DISPLAY “Total Change”

INPUT MoneyGave

SET TotalChange TO MoneyGave - TotalCost

DISPLAY TotalChange

END
