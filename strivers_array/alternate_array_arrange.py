"""You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.
You should return the array of nums such that the the array follows the given conditions:
Every consecutive pair of integers have opposite signs.
For all integers with the same sign, the order in which they were present in nums is preserved.
The rearranged array begins with a positive integer.
Return the modified array after rearranging the elements to satisfy the aforementioned conditions.
"""
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive=[]
        negative=[]
        new_array=[]
        for i in nums:
            if i>0:
                positive.append(i)
            else:
                negative.append(i)
        
        min_len = min(len(positive), len(negative))

        # Append alternately from both arrays
        for i in range(min_len):
            new_array.append(positive[i])
            new_array.append(negative[i])

        # Append remaining elements (if any)
        new_array += positive[min_len:]
        new_array += negative[min_len:]

        return new_array
        
        
        