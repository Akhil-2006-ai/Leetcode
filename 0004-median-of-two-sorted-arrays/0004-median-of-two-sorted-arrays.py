class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sortedarray = nums1 + nums2
        sortedarray.sort()
        n = len(sortedarray)
        if n % 2 == 1:
            return float(sortedarray[n // 2])
        else:
            Mid = (n // 2)
            return(sortedarray[Mid] + sortedarray[Mid - 1]) / 2