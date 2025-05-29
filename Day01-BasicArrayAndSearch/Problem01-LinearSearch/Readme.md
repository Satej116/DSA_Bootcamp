Problem Statement
Given a list of n integers entered by the user, the goal is to search for a specific target number in the array. If the number is present, print its index (first occurrence). If not, print -1.

Approach:

Input Handling:

Ask the user for the length of the array.

Take n numerical inputs from the user to populate the array.

Ask for the target value to search.

Searching Logic:

Loop through each element of the array.

Compare the current element with the target.

If a match is found, print the index and exit.

If the loop ends without finding the target, print -1.

Bug Note:

The original logic sets count = j in every iteration, which may incorrectly print -1 even if the element is found.

Fix: Use a flag or break once the element is found.

Time & Space Complexity:

Time Complexity: Worst-case: O(n) (if the target is not found or is at the end).

Space Complexity: O(n) for storing the array.

Sample Inputs / Edge Cases
Sample Input 1:
Enter the Length of Array = 5
Enter only numerical values
Input: 10 20 30 40 50
Enter the Target Value = 30
Output:
Index = 2

Sample Input 2 (Target not found):
Input: 5 elements: 1 3 5 7 9
Target = 8

Output:
-1
