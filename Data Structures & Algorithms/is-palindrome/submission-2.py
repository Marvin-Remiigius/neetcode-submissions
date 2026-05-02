class Solution:
    def isPalindrome(self, s: str) -> bool:
        res=""
        alphanum=set('abcdefghijklmnopqrstuvwxyz1234567890')
        for i in s:
            if i.lower() in alphanum:
                if not i.isdigit:
                    res+=i
                else:
                    res+=i
        res=res.lower()
        
        return res==res[::-1]