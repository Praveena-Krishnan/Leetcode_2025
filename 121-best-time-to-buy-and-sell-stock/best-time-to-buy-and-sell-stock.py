class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        buy_price=prices[0]
        for i in range(1,len(prices)):
            profit=prices[i]-buy_price
            max_profit=max(max_profit,profit)
            buy_price=min(buy_price,prices[i])
        return max_profit