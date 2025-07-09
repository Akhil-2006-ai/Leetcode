class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sortedarray = nums1 + nums2
        sortedarray.sort()
        N = len(sortedarray)

        if N % 2 == 1:
            return float(sortedarray[N // 2])
        else:
            return (sortedarray[N // 2] + sortedarray[N // 2 - 1]) / 2
        