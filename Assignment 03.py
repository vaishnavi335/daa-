# Structure for an item which stores weight and corresponding value of Item
class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

# Main greedy function to solve the problem
def fractionalKnapsack(W, arr):
    # Sorting Item on the basis of the ratio
    arr.sort(key=lambda x: (x.value / x.weight), reverse=True)

    # Uncomment to see the new order of Items with their ratio
    for item in arr:
        print(item.value, item.weight, round(item.value / item.weight, 3))

    # Result (value in Knapsack)
    finalvalue = 0.0

    # Looping through all Items
    for item in arr:
        # If adding Item won't overflow, add it completely
        if item.weight <= W:
            W -= item.weight
            finalvalue += item.value
        else:
            # If we can't add the current Item, add the fractional part of it
            finalvalue += item.value * W / item.weight
            break

    # Returning the final value
    return finalvalue

# Driver's Code
if __name__ == "__main__":
    # Weight of Knapsack W = 100
    W = 100
    arr = [Item(10, 20), Item(20, 30), Item(30, 66), Item(40, 40), Item(50, 60)]

    # Function call
    print("Knapsack Capacity:", W)
    print("Maximum Profit:", fractionalKnapsack(W, arr))
