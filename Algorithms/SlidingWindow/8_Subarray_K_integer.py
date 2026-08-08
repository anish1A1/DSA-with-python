












from collections import defaultdict
from typing import List

def subarraysWithKDistinct(nums: List[int], k: int) -> int:
    left = 0
    count_dict = defaultdict(int)
    max_subarray_k = 0
    subarray_counts = 0

    for right in range(len(nums)):
        count_dict[nums[right]] += 1

        if len(count_dict) == k:
            subarray_counts += 1
            
        while len(count_dict) > k:
            count_dict[nums[left]] -= 1

            if count_dict[nums[left]] == 0:
                del count_dict[nums[left]]

            left += 1
    return subarray_counts
print(subarraysWithKDistinct(nums = [1,2,1,2,3], k = 2))