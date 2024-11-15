# Part 2 uses Dynamic Programming to quickly get a result.  Ranked 69 on the global leaderboard

def min_coins(coins, target):
    # Initialize a list to store the minimum number of coins needed for each amount up to target
    dp = [float('inf')] * (target + 1)
    dp[0] = 0  # Base case: No coins needed to make 0

    # Iterate over all amounts from 1 to target
    for amount in range(1, target + 1):
        for coin in coins:
            if amount >= coin:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[target] is still infinity, it means the target cannot be reached with the given coins
    return dp[target] if dp[target] != float('inf') else -1

# Example usage

bt = [int(i) for i in open('24-9-2.txt').read().split('\n')]


#coins = [2, 4, 6, 8]
coins = [1, 3, 5, 10, 15, 16, 20, 24, 25, 30]
tl = 0

for i in bt:
    tl += min_coins(coins, i)

print('part 2 -',tl)

#print("Minimum coins required:", min_coins(coins, target))
