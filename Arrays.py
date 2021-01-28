"""
Writing programming interview questions hasn't made me rich yet ... so I might give up and start trading Apple stocks all day instead.

First, I wanna know how much money I could have made yesterday if I'd been trading Apple stocks all day.

So I grabbed Apple's stock prices from yesterday and put them in a list called stock_prices, where:

The indices are the time (in minutes) past trade opening time, which was 9:30am local time.
The values are the price (in US dollars) of one share of Apple stock at that time.
So if the stock cost $500 at 10:30am, that means stock_prices[60] = 500.

Write an efficient function that takes stock_prices and returns the best profit I could have made from one purchase and one sale of one share of Apple stock yesterday.
"""
# Greedy solution
# O(n) time complexity O(1) space
def get_max_profit(stock_prices):

    # Calculate the max profit
    if not stock_prices:
        raise Exception("Error")
    if len(stock_prices) == 1:
        raise Exception("cant have one price")
    max_profit = stock_prices[1] - stock_prices[0]
    min_price = stock_prices[0]
    for price in range(1, len(stock_prices)):
        profit = stock_prices[price]-min_price
        max_profit = max(profit, max_profit)
        min_price = min(stock_prices[price], min_price)

    return max_profit

# Merge sorted arrays
def merge_lists(my_list, alices_list):

    # Set up our merged_list
    merged_list_size = len(my_list) + len(alices_list)
    merged_list = [None] * merged_list_size

    current_index_alices = 0
    current_index_mine = 0
    current_index_merged = 0
    while current_index_merged < merged_list_size:
        is_my_list_exhausted = current_index_mine >= len(my_list)
        is_alices_list_exhausted = current_index_alices >= len(alices_list)
        if (not is_my_list_exhausted and (is_alices_list_exhausted or 
            my_list[current_index_mine] < alices_list[current_index_alices])):
            # Case: next comes from my list
            # My list must not be exhausted, and EITHER:
            # 1) Alice's list IS exhausted, or
            # 2) the current element in my list is less
            #    than the current element in Alice's list
            merged_list[current_index_merged] = my_list[current_index_mine]
            current_index_mine += 1
        else:
            # Case: next comes from Alice's list
            merged_list[current_index_merged] = alices_list[current_index_alices]
            current_index_alices += 1

        current_index_merged += 1

    return merged_list
    return ans


# Kadane's algorithm
# max sum subarray
def maxSubarray(nums):
    maxCurrent = nums[0]
    maxGlobal = nums[0]

    for i in range(1, len(nums)):
        maxCurrent = max(nums[i], maxCurrent + nums[i])
        # maxGlobal = max(maxGlobal, maxCurrent)
        if maxCurrent > maxGlobal:
            maxGlobal = maxCurrent
    return maxGlobal



# maximum product subarray
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        B = nums[::-1]
        for x in range(1, len(nums)):
            if nums[x-1] != 0:
                nums[x] = nums[x] * nums[x-1]
            if B[x-1] != 0:
                B[x] = B[x] * B[x-1]
        A = max(nums)
        B = max(B)
        return max(A, B)