def find_and_replace(lst, find_val, replace_val):
    """
    Task 1
    - Create a function that searches for all occurrences of a value (find_val) in a given list (lst) and replaces them with another value (replace_val).
    - lst must be a list.
    - Return the modified list.
    """

    # Using map() to iterate over the list without any loop statement
    if isinstance(lst, list):
        new_lst = list(map(lambda x: replace_val if x == find_val else x, lst))
    return new_lst



# Task 2
# Invoke the function "find_and_replace" using the following scenarios:
# - [1, 2, 3, 4, 2, 2], 2, 5
# - ["apple", "banana", "apple"], "apple", "orange"
old_list = [1, 2, 3, 4, 2, 2]
new_list = find_and_replace(old_list, 2, 5)
print(new_list)
old_list = ["apple", "banana", "apple"]
new_list = find_and_replace(old_list, "apple", "orange")
print(new_list)