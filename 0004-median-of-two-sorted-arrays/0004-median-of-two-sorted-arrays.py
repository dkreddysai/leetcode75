class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged_array=nums1+nums2
        merged_array.sort()
        n=len(merged_array)
        def is_even(n):
            return n%2==0
        def is_odd(n):
            return n%2!=0
        if is_even(n):
            median=(merged_array[n//2]+ merged_array[(n//2)-1])/2.0
        else:
            median=merged_array[(n-1)//2]
    
        return median
        