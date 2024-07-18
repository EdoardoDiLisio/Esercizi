'''
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively. Write a function to merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
'''
    


def merge(nums1, m, nums2, n):
    # cancella pass e scrivi il tuo codice
    nums1_tmp = nums1.copy()
    i = 0 
    j = 0
    k = 0
    while i < m and j < n:
        if nums1_tmp[i] <= nums2[j]:
            nums1[k] = nums1_tmp[i]
            i += 1
        else:
            nums1[k] = nums2[j]
            j += 1
        k += 1

    while j < n:
        nums1[k] = nums2[j]
        j += 1
        k += 1

    while i < m:
        nums1[k] = nums1_tmp[i]
        i += 1
        k += 1



# Test case 1
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
merge(nums1, m, nums2, n)
print(nums1)  



# Test case 2
nums1 = [1]
m = 1
nums2 = []
n = 0
merge(nums1, m, nums2, n)
print(nums1)  


# Test case 3
nums1 = [0]
m = 0
nums2 = [1]
n = 1
merge(nums1, m, nums2, n)
print(nums1)