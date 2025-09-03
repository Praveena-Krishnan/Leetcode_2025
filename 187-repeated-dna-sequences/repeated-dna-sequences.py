class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        ans=set()
        seen=set()
        j=0
        n=len(s)
        while j<(n-9):
            s1=s[j:j+10]
            if s1 in seen:
                ans.add(s1)
            else:
                seen.add(s1)
            j+=1
        return list(ans)

            
        return ans


        