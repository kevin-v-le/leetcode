class Solution:
    def isPalindrome(self, s: str) -> bool:
        #transform string into all lowercase
        #remove nonalphanumeric
        #reverse [::-1]
        
        
        #2 pointers
        #while exits when l>r
        l, r = 0, len(s)-1
        while l<r:
            while l < r and not s[l].isalnum():
                l+=1
            while r > l and not s[r].isalnum():
                r-=1
            if s[l].lower() != s[r].lower():
                return False
            l+=1
            r-=1
        return True
            
            
            