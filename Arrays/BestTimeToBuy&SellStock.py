def BestTimeToBuyAndSellStock(arr):
    max_profit = 0
    p1 = 0
    p2 = 0
    while p2 < len(arr):
        if(arr[p1]>arr[p2]):
            p1 = p2
        else:
            current_profit = arr[p2] - arr[p1]
            if(max_profit < current_profit):
                max_profit = current_profit
        p2+=1
    return f"Maximu Profit Is {max_profit}"

arr = [7,1,5,3,6,4]
print(BestTimeToBuyAndSellStock(arr))