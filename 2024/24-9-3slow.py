# Made it on the global leaderboard, rank 55.  This was my first attempt, it is slow, however, it produced a result before my fast version was complete
# Uses Dymamic Programming (Memoisation). 

def min_coins(coins, target):
    # Initialize a list to store the minimum number of coins needed for each amount up to target
    dp = [float('inf')] * (target + 1)
    dp[0] = 0  # Base case: No coins needed to make 0

    # Iterate over all amounts from 1 to target
    for amount in range(1, target + 1):
        for coin in coins[::-1]:
            if amount >= coin:                
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[target] is still infinity, it means the target cannot be reached with the given coins
    return dp[target] if dp[target] != float('inf') else -1

# Example usage

bt = [int(i) for i in open('24-9-3.txt').read().split('\n')]


#coins = [2, 4, 6, 8]
coins = [1, 3, 5, 10, 15, 16, 20, 24, 25, 30, 37, 38, 49, 50, 74, 75, 100, 101]
tl = 0

bst = []
bstt = []
bsp = []

for i in [bt[2]]:
    mn = (int) (i/2)
    print(mn)    
    bstt = []
    for tc in range(50):
        csl = mn-tc
        csh = mn+tc
        cd1 = min_coins(coins, csl)
        cd2 = min_coins(coins, csh)
        print(csl, csh, cd1,cd2)
        if (csh - csl < 101):            
            bst.append([cd1,cd2])
            bstt.append(cd1+cd2)
    bsp.append(min(bstt))
    #tl += min_coins(coins, i)

print(bst)
print(bsp, sum(bsp))

#print(tl)

#print("Minimum coins required:", min_coins(coins, target))
