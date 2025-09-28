"""
Problem 1: Duplicate Tracker

You are given a collection of product IDs. Some IDs may appear more than once.
Write a function that returns True if any duplicates are found, and False otherwise.

Example:
Input: [10, 20, 30, 20, 40]
Output: True

Input: [1, 2, 3, 4, 5]
Output: False
"""

def has_duplicates(product_ids):
    set(product_ids) 
    seen = set() 
    for prod in product_ids:
        if prod in seen:
            return True
        seen.add(prod)
    return False
    pass

# (1) Why this data structure fits the task  
# A set is the best option here because all we want to do it check if there are mutiple of the same value, location and referencing does not matter for this
# (2) what operations are performed and their expected runtime
# The operations performed are adding to the set and checking if an item is in the set. Both of these operations are O(1) on average.

"""
Problem 2: Order Manager

You need to maintain a list of tasks in the order they were added, and support removing tasks from the front.
Implement a class that supports add_task(task) and remove_oldest_task().

Example:
task_queue = TaskQueue()
task_queue.add_task("Email follow-up")
task_queue.add_task("Code review")
task_queue.remove_oldest_task() → "Email follow-up"
"""

from collections import deque

class TaskQueue:
    def __init__(self):
        self._dq = deque()

    def add_task(self, task):
        self._dq.append(task)

    def remove_oldest_task(self):
        return self._dq.popleft() if self._dq else None

# (1) Why this data structure fits the task 
# A deque is the best option here because we need to maintain order and be able to efficiently add to the end and remove from the front
# (2) what operations are performed and their expected runtime 
# The operations performed are appending to the end and popping from the front. Both of these operations are O(1).

"""
Problem 3: Unique Value Counter

You receive a stream of integer values. At any point, you should be able to return the number of unique values seen so far.

Example:
tracker = UniqueTracker()
tracker.add(10)
tracker.add(20)
tracker.add(10)
tracker.get_unique_count() → 2
"""

class UniqueTracker:
    def __init__(self):
        self.unique = set()

    def add(self, value):
        self.unique.add(value)

    def get_unique_count(self):
        return len(self.unique)

# (1) Why this data structure fits the task 
# A set is the best option here because we need to maintain a collection of unique items and sets inherently do not allow duplicates
# (2) what operations are performed and their expected runtime 
# The operations performed are adding to the set and getting the length of the set. Adding is O(1) on average and getting the length is O(1).