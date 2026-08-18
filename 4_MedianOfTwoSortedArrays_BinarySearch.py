class Solution:
    """
    Binary Search Approach
    O(log(m+n))
    Logic:
    In order to find the median we need to partition the combined array into 2 sections
    Each section has an total / 2 number of elements
    But how do we partition the array without merging A & B and in log(m+n) time?
    Using the binary search approach we find the mid of array A
    The number of elements = mid number of elements
    Now we need half-mid number of elements from array B to get the partition
    If A[mid] is less than or equal to B[half-mid+1] 
    and B[half-mid+1] <= A[mid+1] this means we paritioned the array correctly
    Else we need to find another element in A which satisfies the above conditions
    So if A[mid]>B[half-mid+1] we need to find a lesser element in A that satisfies the condition
    so r=mid-1
    Else if A[mid]<B[half-mid+1] we still need more elements to reach the partition count
    so we search for a higher element that satisfies the condition
    so l=mid+1
    """
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1)+len(nums2)
        half = total//2
        if len(A)>len(B):
            A, B = B, A
        l, r = 0, len(A)-1
        while True:
            i = (l+r)//2
            j = half - i - 2

            Aleft = A[i] if i>=0 else float('-infinity') # Edge case where we reach the end of the array if there are no longer any elements we set it to -ve infinity so the condition always satifies
            Aright = A[i+1] if i+1<len(A) else float('infinity') # When we reach the other end of the array, we set this to infinity so the condition always satifies & we take in more elements from B array
            Bleft = B[j] if j>=0 else float('-infinity')
            Bright = B[j+1] if j+1<len(B) else float('infinity')

            if Aleft<=Bright and Bleft<=Aright:
                if total%2:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft)+min(Aright, Bright))/2
            elif Aleft>Bright:
                r=i-1
            else:
                l=i+1