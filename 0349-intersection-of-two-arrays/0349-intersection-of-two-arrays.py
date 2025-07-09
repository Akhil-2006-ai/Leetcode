class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmapnums1 = {}
        hashmapnums2 = {}
        for i in range(len(nums1)):
            if nums1[i] in hashmapnums1:
                hashmapnums1[nums1[i]] += 1
            else:
                hashmapnums1[nums1[i]] = 1

        for i in range(len(nums2)):
            if nums2[i] in hashmapnums2:
                hashmapnums2[nums2[i]] += 1
            else:
                hashmapnums2[nums2[i]] = 1
        output = []
        for key in hashmapnums1:
            if key in hashmapnums2:
                output.append(key)
        return output
            
        
        

        