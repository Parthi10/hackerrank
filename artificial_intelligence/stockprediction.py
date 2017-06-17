temp = input().strip().split(' ')
total_money, k, d = float(temp[0]), int(temp[1]), int(temp[2])
stock_prices = []
name=[]
owned = []
for _ in range(k):
    temp = input().strip().split(' ')
    name.append(temp[0])
    owned.append(int(temp[1]))
    stock_prices.append(list(map(float, temp[2:])))

def printTransactions(total_money, k,d, name, owned, stock_prices):
    ans = []
    for i in range(len(stock_prices)):
        price_of_stock = stock_prices[i][-1]
        diff = price_of_stock - stock_prices[i][-2]
        if owned[i] > 0:# you have some stock of this comp
            if diff > 0:# today it's value is higher than yesterday
                #sell it.
                total_money += stock_prices[i][-1] * owned[i]
                ans.append([name[i], "SELL", owned[i]])
                owned[i] = 0
        else:
            if diff < 0: # dipped price of stock
                no_of_stocks = total_money // price_of_stock
                if no_of_stocks:
                    #buy no_of_stocks
                    total_money -= no_of_stocks * price_of_stock
                    owned[i] += int(no_of_stocks)
                    ans.append([name[i], "BUY", owned[i]])

    if len(ans):
        print(len(ans))
        for i in ans:
            print(" ".join(map(str, i)))
    else:
        print(0)

printTransactions(total_money, k,d, name, owned, stock_prices)
