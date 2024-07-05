class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        final_array=[]
        zeros_count=0
        for i in nums:
            if i!=0:
                final_array.append(i)
            else:
                zeros_count+=1
        final_array.extend([0]*zeros_count)
        for i in range(len(nums)):
            nums[i] = final_array[i]
        return nums
        