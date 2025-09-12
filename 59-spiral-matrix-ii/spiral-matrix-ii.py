class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        num=1
        left=0
        right=n-1
        top=0
        bottom=n-1
        ans = [[0 for _ in range(n)] for _ in range(n)]
        while left<=right and top<=bottom and num<=n*n:
            for i in range(left,right+1):
                ans[top][i]=num
                num+=1
            top+=1

            for i in range(top , bottom+1):
                ans[i][right]=num
                num+=1
            right-=1

            if top<=bottom:
                for i in range(right,left-1,-1):
                    ans[bottom][i]=num
                    num+=1
            bottom-=1

            if left<=right:
                for i in range(bottom ,top-1,-1):
                    ans[i][left]=num
                    num+=1
            left+=1

            
        
            
            
        return ans
                
           
                

        