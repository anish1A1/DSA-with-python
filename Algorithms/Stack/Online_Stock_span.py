"""
901. Online Stock Span
Medium
Topics
premium lock icon
Companies
Design an algorithm that collects daily price quotes for some stock and returns the span of that stock's price for the current day.

The span of the stock's price in one day is the maximum number of consecutive days (starting from that day and going backward) for which the stock price was less than or equal to the price of that day.

For example, if the prices of the stock in the last four days are [7,2,1,2] and the price of the stock today is 2, then the span of today is 3 because starting from today, the price of the stock was less than or equal to 2 for 3 consecutive days.
Also, if the prices of the stock in the last four days is [7,34,1,2] and the price of the stock today is 8, then the span of today is 3 because starting from today, the price of the stock was less than or equal 8 for 3 consecutive days.
Implement the StockSpanner class:

StockSpanner() Initializes the object of the class.
int next(int price) Returns the span of the stock's price given that today's price is price.
 

Example 1:

Input
["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
[[], [100], [80], [60], [70], [60], [75], [85]]
Output
[null, 1, 1, 1, 2, 1, 4, 6]

Explanation
StockSpanner stockSpanner = new StockSpanner();
stockSpanner.next(100); // return 1
stockSpanner.next(80);  // return 1
stockSpanner.next(60);  // return 1
stockSpanner.next(70);  // return 2
stockSpanner.next(60);  // return 1
stockSpanner.next(75);  // return 4, because the last 4 prices (including today's price of 75) were less than or equal to today's price.
stockSpanner.next(85);  // return 6
 

Constraints:

1 <= price <= 105
At most 104 calls will be made to next.
"""


class StockSpanner:
    def __init__(self):
        self.stack = [] #stores List: (price, span)
        
    def next(self, price:int) -> int:
        span = 1
        
        while self.stack and price >= self.stack[-1][0]:
            
            span += self.stack[-1][1]
            self.stack.pop()
        
        self.stack.append((price, span))
        return span
    
    # If the prev element's price is greater than the current [-1], then the span will be 1. and will also be returned 1 too.

stockSpanner = StockSpanner()
print(stockSpanner.next(100)); # return 1
print(stockSpanner.next(80));  # return 1
print(stockSpanner.next(60));  # return 1
print(stockSpanner.next(70));  # return 2
print(stockSpanner.next(60));  # return 1
print(stockSpanner.next(75));  # return 4, because the last 4 prices (including today's price of 75) were less than or equal to today's price.

print(stockSpanner.next(85))     # return 6



"""
Step-by-Step Trace
Input sequence: [100, 80, 60, 70, 60, 75, 85]

Day 1: 100 → span=1 → stack=[(100,1)]

Day 2: 80 → span=1 → stack=[(100,1),(80,1)]

Day 3: 60 → span=1 → stack=[(100,1),(80,1),(60,1)]

Day 4: 70 → pop (60,1) → span=2 → stack=[(100,1),(80,1),(70,2)]

Day 5: 60 → span=1 → stack=[(100,1),(80,1),(70,2),(60,1)]

Day 6: 75 → pop (60,1),(70,2) → span=4 → stack=[(100,1),(80,1),(75,4)]

Day 7: 85 → pop (75,4),(80,1) → span=6 → stack=[(100,1),(85,6)]

Result: [1,1,1,2,1,4,6]



"""