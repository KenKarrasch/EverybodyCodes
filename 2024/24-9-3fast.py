# The slow version completed before I could complete this version.  It makes use Dymamic Programming to precompute a range of targets value.
# It is much faster than individually computing the 100 options.


def precompute_min_coins(coins, max_target):
    # Initialize dp array with infinity for all values up to max_target
    dp = [float('inf')] * (max_target + 1)
    dp[0] = 0  # No coins are needed to make the amount 0

    # Fill dp array with the minimum coins needed for each amount up to max_target
    for amount in range(1, max_target + 1):
        for coin in coins:
            if amount >= coin:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)
    
    return dp

# Example usage
coins = [2, 4, 6, 8]
coins = [1, 3, 5, 10, 15, 16, 20, 24, 25, 30, 37, 38, 49, 50, 74, 75, 100, 101]

bst = []
bt = [int(i) for i in open('24-9-3.txt').read().split('\n')]
bsp = []

for i in bt:  
    print(i)  
    mn = (int) (i/2)    
    csl = mn-50
    csh = mn+50
    
    targets = range(csl-10,csh+10)

    #targets = [50, 75, 100]  # Multiple target amounts
    max_target = max(targets)  # Find the largest target to compute up to that amount
    dp = precompute_min_coins(coins, max_target)  # Precompute minimum coins up to max_target
       
    bstt = []
    for tc in range(50):
        csl = mn-tc
        csh = mn+tc
        cd1 = dp[csl] # min_coins(coins, csl)
        cd2 = dp[csh] # min_coins(coins, csh)
        #print(csl, csh, cd1,cd2)

        if (csh - csl < 101):            
            bst.append([cd1,cd2])
            bstt.append(cd1+cd2)
    bsp.append(min(bstt))

print('part 3 -',sum(bsp))

# Retrieve the result for each target
#results = {target: dp[target] if dp[target] != float('inf') else -1 for target in targets}
#print("Minimum coins required for each target:", results)
