class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        ct = 0
        set_arr2 = set(arr2)

        for i in arr1:
            ct2 = sum(abs(i - j) > d for j in set_arr2)
            if ct2 == len(set_arr2):
                ct += 1

        return ct
