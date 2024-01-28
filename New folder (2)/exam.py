#Write a Python function that takes two lists of integers as input and returns a new list 
containing the elements that appear more than once across both lists. The result should 
be in ascending order, and each repeated element should appear only once in the output 
list.
For example, given the input lists [3, 1, 4, 4, 5, 6] and [2, 4, 6, 8, 4, 9], the function 
should return [4, 6].


def find_duplicates(list1, list2):
    combined_set = set(list1) & set(list2)
    return sorted(list(set(combined_set)))

# Example usage:
list1 = [3, 1, 4, 4, 5, 6]
list2 = [2, 4, 6, 8, 4, 9]
result = find_duplicates(list1, list2)
print(result)
