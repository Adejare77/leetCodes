#!/usr/bin/env python3
from typing import List

class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(len(nums)):
            if nums[i] == 0:
                continue

            direction = affirm_dir = nums[i] > 0 # checks current index direction
            checked = True

            def next_index(index): # finds the next index
                nonlocal affirm_dir, checked, direction
                if checked and ((nums[index] > 0) != direction): # change in sign
                    affirm_dir = not affirm_dir
                    checked = False

                return (index + nums[index]) % n


            slow_ptr = fast_ptr = i
            while True:
                slow_ptr = next_index(slow_ptr)
                fast_ptr = next_index(next_index(fast_ptr))

                if affirm_dir != direction:
                    break

                if slow_ptr == fast_ptr: # Circular Array confirmed
                    if slow_ptr == next_index(slow_ptr):
                        break
                    return True

            slow = i
            while (nums[slow] > 0) == direction and nums[slow] != 0:
                next_slow = next_index(slow)
                nums[slow] = 0
                slow = next_slow

        return False

nums = [1,-1,5,1,4]
print(Solution().circularArrayLoop(nums))
nums = [1, 2, 3, 4, 5]
print(Solution().circularArrayLoop(nums))
nums = [-1,2,1,2]
print(Solution().circularArrayLoop(nums))
nums = [1,1,1,1,1,1,1,1,1,-5]
print(Solution().circularArrayLoop(nums))
