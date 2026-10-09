class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        # Bringign the smaller list as nums1
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        n1_len, n2_len = len(nums1), len(nums2)
        left_pointer, right_pointer = (0, n1_len)

        while left_pointer <= right_pointer:

            partition1 = (left_pointer + right_pointer) // 2
            partition2 = ((n1_len + n2_len + 1) // 2) - partition1

            max_left1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            min_right1 = float('inf') if partition1 == n1_len else nums1[partition1]

            max_left2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            min_right2 = float('inf') if partition2 == n2_len else nums2[partition2]

            # if partition if found correctly:
            if max_left1 <= min_right2 and max_left2 <= min_right1:
                if (n1_len + n2_len) % 2 == 1:
                    return float(max(max_left1, max_left2))
                return (
                    max(max_left1, max_left2) + 
                    min(min_right1, min_right2)
                ) / 2.0
            elif max_left1 > min_right2: right_pointer = partition1 - 1
            else: left_pointer = partition1 + 1