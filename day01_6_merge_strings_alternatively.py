class Solution(object):
    def mergeAlternately(self, word1, word2):
        word=""
        min_length=min(len(word1),len(word2))
        i=0
        
        for i in range(min_length):
            word+=word1[i]
            word+=word2[i]
        
        
        word+=word1[min_length:]
        
        word+=word2[min_length:]
        return word
        
            