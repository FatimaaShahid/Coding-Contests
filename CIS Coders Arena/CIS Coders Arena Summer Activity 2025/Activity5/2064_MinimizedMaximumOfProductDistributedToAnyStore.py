class Solution:
    def minimizedMaximum( n, quantities) :
        def canDistribute(m):
            return sum((q+m-1)//m for q in quantities) <=n
        
        left = 1
        right = max(quantities)
        while left < right:
            mid = (left+right)//2
            if canDistribute(mid):
                right = mid
            else:
                left = mid + 1
        return left
            


        