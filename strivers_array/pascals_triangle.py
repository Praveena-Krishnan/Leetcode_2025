class Solution:
    def generate_row(self,n):
        ans=1
        ans_row=[]
        ans_row.append(1)
        for i in range(1,n):
            ans=ans*(n-i)
            ans=ans//(i)
            ans_row.append(ans)
        return ans_row
    def generate(self, numRows: int) -> List[List[int]]:
        ans=[]
        for i in range(0,numRows):
            ans.append(self.generate_row(i+1))
        return ans
        

        