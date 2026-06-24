class Solution(object):
    def sortedSquares(self, nums):
        num=[]
        i=0
        for j in nums:
            num.append(j*j)
            i+=1
        num.sort()
        return num
        