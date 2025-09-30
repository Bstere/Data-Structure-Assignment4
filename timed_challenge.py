# Pick one question from timed_challenge.txt
# Paste the question as a comment below
# Set a timer for 30 minutes and complete the question!

# 3. Remove Duplicates (Keep Order)
 # Return the values in the order they first appeared, without duplicates.
 # Input: ["apple", "banana", "apple", "kiwi", "banana"]
 # Output: ["apple", "banana", "kiwi"]

def remove_duplicates_keep_order(values):
    seen = set()                              # keep track of already stored values
    result = []                               # storing output in original order

    for item in values:
        if item not in seen:
            seen.add(item)
            result.append(item)

    return result

# Test cases
print(remove_duplicates_keep_order(["apple", "banana", "apple", "kiwi", "banana"]))
print(remove_duplicates_keep_order(["a", "b", "c", "a", "d", "c"]))
print(remove_duplicates_keep_order([]))
print(remove_duplicates_keep_order(["x", "x", "x", "x"]))


"""Reflection

I chose this timed challenge because it was the closest to what was in the practice problems and made sense to keep
in the same direction.
They are similar problems and they use sets which made me more comfortable.
To solve this it was important to a set to track that have already been seen. (same way we did in the practice problems)
Set are an amazing tool because the ignore duplicates automatically.
I used a list for keeping track of values in the right order as it loops through the input.

The test case:

The first test case i made contains an order and duplicates to make sure that the code removes duplicates without affecting order.
The second case is similar 
The third case is an empty list to see if in that case the function works.
The fourth case is only duplicates.

It was fun to create these test scenarios and I really enjoyed this weeks homework."""


