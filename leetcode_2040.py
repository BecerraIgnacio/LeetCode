import bisect
import math
nums1 = [-10,-10,-5,-4,-3,-1]
nums2 = [1,6]
k = 9
def ejercicio(nums1, nums2, k):

        candidates = [
            nums1[0] * nums2[0],
            nums1[0] * nums2[-1],
            nums1[-1] * nums2[0],
            nums1[-1] * nums2[-1],
        ]
        min_prod = min(candidates)
        max_prod = max(candidates)

        def count_le(val):
            cnt = 0
            for x in nums1:
                if x > 0:
                    cnt += bisect.bisect_right(nums2, val // x)
                elif x == 0:
                    if val >= 0:
                        cnt += len(nums2)
                else:
                    thresh = math.ceil(val / x)
                    idx = bisect.bisect_left(nums2, thresh)
                    cnt += len(nums2) - idx
            return cnt

        lo, hi = min_prod, max_prod
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if count_le(mid) < k:
                lo = mid + 1
            else:
                hi = mid
        return lo
print(ejercicio(nums1, nums2, k))