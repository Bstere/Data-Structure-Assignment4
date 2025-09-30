# Pick one question from timed_challenge.txt
# Paste the question as a comment below
# Set a timer for 30 minutes and complete the question!

# 3. Remove Duplicates (Keep Order)
 # Return the values in the order they first appeared, without duplicates.
 # Input: ["apple", "banana", "apple", "kiwi", "banana"]
 # Output: ["apple", "banana", "kiwi"]

def remove_duplicates_keep_order(values):
    seen = set()                              # to keep track of already seen values
    result = []                               # to store the output in original order

    for item in values:
        if item not in seen:
            seen.add(item)
            result.append(item)

    return result

# Test cases
print(remove_duplicates_keep_order(["apple", "banana", "apple", "kiwi", "banana"]))
# Expected: ['apple', 'banana', 'kiwi']

print(remove_duplicates_keep_order(["a", "b", "c", "a", "d", "c"]))
# Expected: ['a', 'b', 'c', 'd']

print(remove_duplicates_keep_order([]))
# Expected: []

print(remove_duplicates_keep_order(["x", "x", "x", "x"]))
# Expected: ['x']
