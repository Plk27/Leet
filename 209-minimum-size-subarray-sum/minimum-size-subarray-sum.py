class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        low=0
        sum=0
        ans=float('inf')

        for high in range(len(nums)):
            sum+=nums[high]
            while sum>=target:
                ans= min(ans,high-low+1)
                sum-=nums[low]
                low+=1

        if ans==float('inf'):
            return 0
        
        return ans

        