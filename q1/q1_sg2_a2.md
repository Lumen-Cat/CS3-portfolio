Section: 9 Balingkilat                                      Score:____________

C# / Name: 19-20-21 / Bondoc, Carbungco, Cato               Date: 08/14/26


The problem: Finding the highest (Maximum) number from a given list of numbers.


PseudoCode 1

Algorithm FindMax1(numbers)

   max ← numbers[0]

   For i from 1 to length(numbers)-1

      If numbers[i] > max Then

         max ← numbers[i]

      EndIf

   EndFor

   Return max

EndAlgorithm

PseudoCode 2

Algorithm FindMax2(numbers)

   For i from 0 to length(numbers)-1bigger ← true

      For j from 0 to length(numbers)-1

         If numbers[j] > numbers[i] Then

            bigger ← false

         EndIf

      EndFor

      If bigger = true Then

         Return numbers[i]

      EndIf

   EndFor

EndAlgorithm


1. Efficiency
Which algorithm is faster when the list of numbers is very large? Why?

   The faster algorithm would likely end up being pseudocode 1, as it utilizes a simpler, more straightforward code with fewer steps that pseudocode 2. Unlike the second pseudocode, the first pseudocode only goes through the list once. 


2. Readability

Which algorithm is easier to understand at first glance? What makes it clearer?

   At a glance, Pseudocode 1 is shorter in terms of text, and the variable names are considerably easier to understand and descriptive than Pseudocode 2. The logic is also simpler for pseudocode 1, it will sort through the given list of numbers in increasing order and stopping once there are no more higher numbers, all in a few lines of code, unlike the expanded Pseudocode 2.


3. Maintainability
If you had to add a new feature (like finding both max and min), which algorithm would be easier to update? Why?

   If I had to add a new feature, Pseudocode 1 would be easier to update. The structure is more straightforward, adding new steps won’t break the code easily, and there is less chance of errors when updating, proving that it is easier to update and maintain compared to Pseudocode 2 who does not really fulfill all those requirements.
   
4. Testability
Which algorithm is easier to test with different inputs? Why?

I can test Pseudocode 1 more easily, it has fewer conditions to check, and the output is more predictable and clearer, making Pseudocode 1 easier to test with different inputs compared to Pseudocode 2.

5. Security
Imagine the input list comes from a user. What should the algorithm check to avoid errors or misuse?

The algorithm should check that the input list is not empty and that all the inputs are valid numbers. It should also be able to handle unexpected inputs.
 

6. Final Answer
Based on your answers from 1 to 5, which one is the better algorithm that you will use to solve the problem of finding the highest number? Why? Summarize your answer

Pseudocode 1 is the better algorithm because it is faster and easier to understand. It only needs to go through the list once, making it more efficient.
