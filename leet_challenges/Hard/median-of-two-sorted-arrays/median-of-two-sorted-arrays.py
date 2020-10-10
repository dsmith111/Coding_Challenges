class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        a1 = a2 = 0
        merged_array = []
        
        while a1 < len(nums1) and a2 < len(nums2):
            
            if nums1[a1] < nums2[a2]:
                merged_array.append(nums1[a1])
                a1 += 1
            
            else:
                merged_array.append(nums2[a2])
                a2 += 1
                
        while a1 < len(nums1):
            merged_array.append(nums1[a1])
            a1 += 1
            
        while a2 < len(nums2):
            merged_array.append(nums2[a2])
            a2 += 1
            
        middle = len(merged_array)//2
        
        if (len(merged_array)%2 == 0):
            left = merged_array[middle-1]
            right = merged_array[middle]
            final = (left + right)/2
            
        else:
            final = merged_array[middle]
            
        return final