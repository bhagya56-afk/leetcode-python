class Solution(object):
    def majorityElement(self, nums):
        
        n=len(nums)
        dicti={}
        for i in nums:
            if i in dicti:
                dicti[i]+=1
            else:
                dicti[i]=1
        for key in dicti:
            if n%2==0:
                if(dicti[key]>n/2):
                    return key
            else:
                if(dicti[key]>(n-1)/2):
                    return key

        