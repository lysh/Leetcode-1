# class Solution(object):
#     def combinationSum4(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#         if target == 0:
#         	return 1
#         ans=0
#         for i in range(len(nums)):
#         	if nums[i]<=target:
#         		ans+=self.combinationSum4(nums,target-nums[i])
#         return ans
#   上述解法超时

class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp=[0]*(target+1)
        dp[0]=1
        for i in range(1,target+1):
        	for num in nums:
        		if num<=i:
        			dp[i]+=dp[i-num]
        return dp[target]


print(Solution().combinationSum4([1,2,3],4))