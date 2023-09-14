'''There are eight coins in general circulation: 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
How many different ways can £2 be made using any number of coins?'''

def dumb_method():
    ways = 0
    total = 200
    for a in range(1 + 1):
        remaining = total - a * 200
        for b in range(int(remaining / 100) + 1):
            remaining = total - a * 200 - b * 100
            for c in range(int(remaining / 50) + 1):
                remaining = total - a * 200 - b * 100 - c * 50
                for d in range(int(remaining / 20) + 1):
                    remaining = total - a * 200 - b * 100 - c * 50 - d * 20
                    for e in range(int(remaining / 10) + 1):
                        remaining = total - a * 200 - b * 100 - c * 50 - d * 20 - e * 10
                        for f in range(int(remaining / 5) + 1):
                            remaining = total - a * 200 - b * 100 - c * 50 - d * 20 - e * 10 - f * 5
                            for g in range(int(remaining / 2) + 1):
                                ways += 1
    print(ways)

def n_ways(total, coins):
    if not coins: 
        return 0
    c, coins = coins[0], coins[1:]
    count = 0
    if total % c == 0:
        count += 1
    for amount in range(0, total, c):
        count += n_ways(total - amount, coins)
    return count

if __name__ == '__main__':
    #dumb_method()
    #print(2 * 3 * 5 * 11 * 21 * 41 * 101 * 201)
    print(n_ways(200, [1, 2, 5, 10, 20, 50, 100, 200]))