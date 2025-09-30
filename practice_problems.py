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
    # Your implementation here
    seen = set()                     # seen is the empty set with set not allowing duplicates
    for pid in product_ids:          # go through each pid in the product_ids list  
        if pid in seen:              # check if the pid is already in the seen list 
            return True            # if it is then return true, there is a duplicate
        seen.add(pid)                # if not in the seen, we add it there
    return False                     # we finish the loop with no duplicates we show false


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

class TaskQueue:
    def __init__(self):
        self.queue = []                  # the list keeps the order in the tasks

    def add_task(self, task):
        self.queue.append(task)          # add new task at the end

    def remove_oldest_task(self):
        if self.queue:
            return self.queue.pop(0)         # remove the oldest task which is the first one then
        return None                        # if queue is empty, return None



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
        self.values = set()               # the set will store unique values

    def add(self, value):
        self.values.add(value)           # add adds the value to the set while ignoring duplicates

    def get_unique_count(self):
        return len(self.values)            # return how many unique values are in the set

