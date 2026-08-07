class Solution {
    public int maxProfit(int[] prices) {
        int buyPrice = prices[0];
        int profit = 0;

        for (int i=1; i<prices.length; i++){
            if (buyPrice > prices[i])
            {
                buyPrice = prices[i];
            }
            profit = Math.max(profit, prices[i]-buyPrice);
        }
        return profit;
        
    }
}

// class Solution:
//     def maxProfit(self, prices: List[int]) -> int:
//         buy_price = prices[0]
//         profit = 0

//         for p in prices[1:]:
//             if buy_price > p:
//                 buy_price = p
            
//             profit = max(profit, p - buy_price)
        
//         return profit