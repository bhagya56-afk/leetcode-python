class Solution(object):
    def isIsomorphic(self, s, t):
        dicti={}
        ictdi={}
        
        if(len(s)==len(t)):
            for i in range(len(s)):
                if s[i] in dicti:
                    if dicti[s[i]]!=t[i]:
                        return False
                   
                else:
                    if t[i] in ictdi:
                        if ictdi[t[i]]!=s[i]:
                            return False
                        dicti[s[i]] = t[i]
                        ictdi[t[i]] = s[i]
                    else:
                        dicti[s[i]] = t[i]
                        ictdi[t[i]] = s[i]
            return True        
        return False
                        
            
                

            