#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) O(n^3)

- input size was multiplied 3 times. Even though there's only one loop, the loop will run n ^ 3 times because of the condition at worst case

b) O(n^2)

- because of nested while loop, wwhil loop will perform operation for each `i` until while loop condition is met

c) O(n)

- function will repeatedly be called until n is 0 meaning number of calls depend on number of inputs

## Exercise II

1. I will find the midpoint n//2 and start dropping eggs from their
2. If eggs break from midpoint it means I'm too high and need to go down
3. if not, I can still go up one floor

- time complexity will be O(logn) since I'm halving the number of stories
