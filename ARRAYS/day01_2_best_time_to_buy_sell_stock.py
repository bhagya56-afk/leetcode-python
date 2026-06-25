class Solution(object):
    def maxProfit(self, prices):
        max_prof=0
        min_price=prices[0]
        for i in range(len(prices)):
            if (min_price>=prices[i]):
                min_price=prices[i]
            prof=prices[i]-min_price
                    
            if (prof>=max_prof):
                max_prof=prof
        return max_prof
        