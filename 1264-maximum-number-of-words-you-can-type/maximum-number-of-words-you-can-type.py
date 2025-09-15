class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        count=0
        words=text.split()
        for i in words:
            if not any(ch in i for ch in brokenLetters):
                count+=1
        return count
            
        