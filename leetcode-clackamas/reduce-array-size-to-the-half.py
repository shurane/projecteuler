from typing import List

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        # this is O(n log n) because of the sort. There's also a priority queue version, which is still O(n log n).
        # for an O(n) solution, try using bucket sort.
        # - https://leetcode.com/problems/reduce-array-size-to-the-half/discuss/1319437/Simple-Solution-w-Explanation-or-Delete-Elements-by-Max-Frequency-or-O(N)-Beats-100
        # - https://leetcode.com/problems/reduce-array-size-to-the-half/discuss/1319416/C%2B%2BJavaPython-HashMap-and-Sort-then-Bucket-Sort-O(N)-Clean-and-Concise

        s = dict()
        for elem in arr:
            if elem not in s:
                s[elem] = 0
            s[elem] += 1

        counts = sorted(s.values(), reverse=True)
        total = 0
        i = 0
        l = len(arr) // 2
        while total < l and i < len(counts):
            total += counts[i]
            i += 1

        # print(counts, total, l, i)

        return i


s = Solution()
assert s.minSetSize([1,9]) == 1
assert s.minSetSize([1000,1000,3,7]) == 1
assert s.minSetSize([1000,2,3,7]) == 2
assert s.minSetSize([3,3,3,3,5,5,5,2,2,7]) == 2
assert s.minSetSize([7,7,7,7,7,7]) == 1
assert s.minSetSize([1,2,3,4,5,6,7,8,9,10]) == 5
assert s.minSetSize([1,1,3,4,5,6,7,8,9,10]) == 4
assert s.minSetSize([1,1,1,4,5,6,7,8,9,10]) == 3
assert s.minSetSize([1,1,1,1,5,6,7,8,9,10]) == 2
assert s.minSetSize([1,1,1,1,1,6,7,8,9,10]) == 1

assert s.minSetSize([1,1,2,2,5,6,7,8,9,10]) == 3
assert s.minSetSize([1,1,2,2,2,6,7,8,9,10]) == 2