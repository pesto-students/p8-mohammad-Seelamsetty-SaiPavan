"""Problem 6.6 :
 3 sumGiven an array S of n integers, find three integers in S such that the sum 
is closest to agiven number, target.Return the sum of the three integers.
Assume that there will only beone solutionExample: given array 
S = {-1 2 1 -4}, and target = 1. The sum that is closest to thetarget is 2. (-1 + 2 + 1 = 2)"""
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res=sum(nums[:3])
        for i in range(len(nums)-2):
            s=i+1
            e=len(nums)-1
            while s<e:
                sumhere=nums[i]+nums[s]+nums[e]
                if abs(sumhere-target)<abs(res-target):
                    res=sumhere
                if sumhere<target:
                    s+=1
                else:
                    e-=1
        return res                
