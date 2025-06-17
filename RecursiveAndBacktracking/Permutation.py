class Solution(object):
    def permute(self, nums):
        
        result = []
        path = []
        used = [False] * len(nums)    # This will check if the number is used or not
        
       
        # result → stores all valid permutations

        # used → keeps track of which elements are already used in current permutation

        # path → current building permutation

        def backtrack():
            if len(path) == len(nums):   # if the [ , , ] 3 value if filled then return result
                # When the path becomes the same length as the input — we found a valid permutation.
                result.append(list(path[:]))
                return
            
            for i in range(len(nums)):
            # Skip numbers already in current path (marked used[i]).
                if used[i]:
                    continue
                
                # Try a number → go deeper → then remove it and try next one.

                # Choose
                path.append(nums[i])
                used[i] = True
                
                # Explore
                backtrack()
                
                # Unchoose
                path.pop()
                used[i] = False

        backtrack()
        return result


if __name__ == '__main__':
    sol =Solution()
    ans = sol.permute([1,2,3])
    print(f"\n{ans}\n")



""" Visual Representation

START backtrack()
    try 1 ➜ path = [1]
        backtrack()
            try 2 ➜ path = [1, 2]
                backtrack()
                    try 3 ➜ path = [1, 2, 3]
                        ✅ append [1, 2, 3]
                    backtrack ➜ remove 3 ➜ path = [1, 2]
                backtrack ➜ remove 2 ➜ path = [1]
            try 3 ➜ path = [1, 3]
                backtrack()
                    try 2 ➜ path = [1, 3, 2]
                        ✅ append [1, 3, 2]
                    backtrack ➜ remove 2 ➜ path = [1, 3]
                backtrack ➜ remove 3 ➜ path = [1]
        backtrack ➜ remove 1 ➜ path = []

    try 2 ➜ path = [2]
        backtrack()
            try 1 ➜ path = [2, 1]
                backtrack()
                    try 3 ➜ path = [2, 1, 3]
                        ✅ append [2, 1, 3]
                    backtrack ➜ remove 3 ➜ path = [2, 1]
                backtrack ➜ remove 1 ➜ path = [2]
            try 3 ➜ path = [2, 3]
                backtrack()
                    try 1 ➜ path = [2, 3, 1]
                        ✅ append [2, 3, 1]
                    backtrack ➜ remove 1 ➜ path = [2, 3]
                backtrack ➜ remove 3 ➜ path = [2]
        backtrack ➜ remove 2 ➜ path = []

    try 3 ➜ path = [3]
        backtrack()
            try 1 ➜ path = [3, 1]
                backtrack()
                    try 2 ➜ path = [3, 1, 2]
                        ✅ append [3, 1, 2]
                    backtrack ➜ remove 2 ➜ path = [3, 1]
                backtrack ➜ remove 1 ➜ path = [3]
            try 2 ➜ path = [3, 2]
                backtrack()
                    try 1 ➜ path = [3, 2, 1]
                        ✅ append [3, 2, 1]
                    backtrack ➜ remove 1 ➜ path = [3, 2]
                backtrack ➜ remove 2 ➜ path = [3]
        backtrack ➜ remove 3 ➜ path = []

END

"""


"""

🚀 Step-by-Step Execution for nums = [1, 2, 3]
We start with:


result = []
path = []
used = [False, False, False]
🔁 First Layer: i = 0 → choose 1

path = [1]
used = [True, False, False]
➡ Second Layer: i = 1 → choose 2

path = [1, 2]
used = [True, True, False]
➡ Third Layer: i = 2 → choose 3

path = [1, 2, 3]
used = [True, True, True]
✅ length(path) == 3 → result.append([1, 2, 3])
↩️ Backtrack:


pop 3 → path = [1, 2], used = [True, True, False]
pop 2 → path = [1], used = [True, False, False]
🔁 Second Layer: i = 2 → choose 3

path = [1, 3]
used = [True, False, True]
➡ Third Layer: i = 1 → choose 2

path = [1, 3, 2]
used = [True, True, True]
✅ result.append([1, 3, 2])
↩️ Backtrack:


pop 2 → path = [1, 3], used = [True, False, True]
pop 3 → path = [1], used = [True, False, False]
pop 1 → path = [], used = [False, False, False]
🔁 First Layer: i = 1 → choose 2

path = [2]
used = [False, True, False]
➡ Second Layer: i = 0 → choose 1

path = [2, 1]
used = [True, True, False]
➡ Third Layer: i = 2 → choose 3

path = [2, 1, 3]
used = [True, True, True]
✅ result.append([2, 1, 3])
↩️ Backtrack:


pop 3 → path = [2, 1], used = [True, True, False]
pop 1 → path = [2], used = [False, True, False]
➡ Second Layer: i = 2 → choose 3

path = [2, 3]
used = [False, True, True]
➡ Third Layer: i = 0 → choose 1

path = [2, 3, 1]
used = [True, True, True]
✅ result.append([2, 3, 1])
↩️ Backtrack:


pop 1 → path = [2, 3], used = [False, True, True]
pop 3 → path = [2], used = [False, True, False]
pop 2 → path = [], used = [False, False, False]
🔁 First Layer: i = 2 → choose 3

path = [3]
used = [False, False, True]
➡ Second Layer: i = 0 → choose 1

path = [3, 1]
used = [True, False, True]
➡ Third Layer: i = 1 → choose 2

path = [3, 1, 2]
used = [True, True, True]
✅ result.append([3, 1, 2])
↩️ Backtrack:


pop 2 → path = [3, 1], used = [True, False, True]
pop 1 → path = [3], used = [False, False, True]
➡ Second Layer: i = 1 → choose 2

path = [3, 2]
used = [False, True, True]
➡ Third Layer: i = 0 → choose 1

path = [3, 2, 1]
used = [True, True, True]
✅ result.append([3, 2, 1])
↩️ Backtrack:


pop 1 → path = [3, 2], used = [False, True, True]
pop 2 → path = [3], used = [False, False, True]
pop 3 → path = [], used = [False, False, False]
✅ Final Result:

[
 [1, 2, 3],
 [1, 3, 2],
 [2, 1, 3],
 [2, 3, 1],
 [3, 1, 2],
 [3, 2, 1]
]
"""