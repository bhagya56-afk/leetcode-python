class Solution(object):
    def wordPattern(self, pattern, s):
        p={}
        t={}
        
        words = s.split()
        if(len(words)==len(pattern)):
            for i in range(len(pattern)):
                
                if pattern[i] in p:
                    if p[pattern[i]]!=words[i]:
                        return False
                else:
                    if words[i] in t:
                        if t[words[i]]!=pattern[i]:
                            return False
                        t[words[i]]=pattern[i]
                        p[pattern[i]]=words[i]
                    else:
                        t[words[i]]=pattern[i]
                        p[pattern[i]]=words[i]           
        else:
            return False
        return True
