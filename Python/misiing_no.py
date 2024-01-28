def missing_numbers(set_nums1, set_nums2):
    return set(set_nums1) - set(set_nums2),set(set_nums2) - set(set_nums1) 

set_nums1 = {1, 2, 3, 4, 5, 6}
set_nums2 = {3, 4, 5, 6, 7, 8}
result = missing_numbers(set_nums1, set_nums2)
print("Original sets:")
print(set_nums1)
print(set_nums2)
print("Missing numbers in the second set as compared to the first:")
print(result[0])
print("Missing numbers in the first set as compared to the second:")
print(result[1])
set_nums1 = {1, 2, 3, 4, 5}
set_nums2 = {6, 7, 8}
result = missing_numbers(set_nums1, set_nums2)
print("\nOriginal sets:")
print(set_nums1)
print(set_nums2)
print("Missing numbers in the second set as compared to the first:")
print(result[0])
print("Missing numbers in the first set as compared to the second:")
print(result[1]) 
