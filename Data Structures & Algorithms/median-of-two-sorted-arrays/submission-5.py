class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
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

            if max_left1 <= min_right2 and max_left2 <= min_right1:
                if (n1_len + n2_len) % 2 == 1:
                    return float(max(max_left1, max_left2))
                return float((max(max_left1, max_left2) + min(min_right1, min_right2)) / 2)
            elif max_left1 > min_right2: right_pointer = partition1 - 1
            else: left_pointer = partition1 + 1

        # Always binary search on the smaller array
        # if len(nums1) > len(nums2):
        #     nums1, nums2 = nums2, nums1

        # n, m = len(nums1), len(nums2)
        # left, right = 0, n

        # while left <= right:
        #     partition1 = (left + right) // 2
        #     partition2 = (n + m + 1) // 2 - partition1

        #     maxLeft1 = float("-inf") if partition1 == 0 else nums1[partition1 - 1]
        #     minRight1 = float("inf") if partition1 == n else nums1[partition1]

        #     maxLeft2 = float("-inf") if partition2 == 0 else nums2[partition2 - 1]
        #     minRight2 = float("inf") if partition2 == m else nums2[partition2]

        #     # Correct partition found
        #     if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
        #         if (n + m) % 2 == 1:
        #             return float(max(maxLeft1, maxLeft2))

        #         return (
        #             max(maxLeft1, maxLeft2) +
        #             min(minRight1, minRight2)
        #         ) / 2.0

        #     elif maxLeft1 > minRight2:
        #         right = partition1 - 1

        #     else:
        #         left = partition1 + 1
