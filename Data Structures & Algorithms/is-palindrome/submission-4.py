class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = ""
        alphanum = set("qwertyuiopasdfghjklzxcvbnm0123456789")

        for c in s:
            if c.lower() in alphanum:
                cleaned_s += c.lower()

        return cleaned_s == cleaned_s[::-1]