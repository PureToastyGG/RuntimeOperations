'''2. Running Total with Reset
Track a running total of values. If a negative number is added, reset the total to 0.
Input: [5, 7, -1, 3, 2]
Output: [5, 12, 0, 3, 5]'''

class RunningTotal:
    def __init__(self, list):
        self.previous = 0
        self.list = list  
        self.totals = []
    def __str__(self):
        for value in self.list: 
            if type(value) != int:
                continue
            if value < 0:
                self.previous = 0 
                self.totals.append(self.previous)
            else:
                self.previous += value
                self.totals.append(self.previous)
        return str(self.totals)
runninglist = RunningTotal([5, 7, -1, 3, 2]) 
print(runninglist)

#What structure you chose and why?
#I used a basic list to store the totals because it is simple and allows for easy appending of new totals. Also the input being a list made it easier to just create a duplicated list with the updated 
#output values.

#How the time limit shaped your decision?
#I chose a simple approach that is easy to implement quickly, focusing on clarity and correctness over optimization. I briefly considered the other options but none of them seemed like obvious answers for me. 
#so I went with a straightforward approach that I could implement quickly.

#What trade-offs or compromises you made under time pressure? 
#I did not implement error handling for non-integer inputs, assuming the input list would only contain integers. I also did not optimize for space or time complexity beyond the basic requirements. 
# I didn't know how any of the different data structures would have been better or worse than the solution that initially came to mind, it didn't inherently seem like queues, stacks, or sets, would help with this problem.