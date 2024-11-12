#Code  by Shouvik Barua Turjo, CSE 030 07820
class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.value_per_weight = value / weight  # profit-ratio


def fractional_knapsack(capacity, items):
    # Sort items based on profit ratio (descending order)
    items.sort(key=lambda x: x.value_per_weight, reverse=True)
    
    total_value = 0.0  # To store the total value accumulated in the knapsack
    for item in items:
        if capacity <= 0:
            break

        if item.weight <= capacity:
            # If the item can be fully taken
            taken_value = item.value
            total_value += taken_value
            taken_weight = item.weight
            capacity -= taken_weight
            print('taken_weight', taken_weight, 'from item having weight', item.weight)
            print('taken value', taken_value)

        else:
            # Take the fraction of the item that fits
            taken_value = item.value_per_weight * capacity
            total_value += item.value_per_weight * capacity
            taken_weight = capacity
            print('taken weight',taken_weight, 'from item having weight', item.weight)
            print('taken value', taken_value)
            capacity = 0  # Knapsack is full, no capacity left

    return total_value


if __name__ == "__main__":
    # List of items (weight, value)
    items = [
        Item(5, 12),  
        Item(10, 25), 
        Item(7, 19),
        Item(12, 13),

    ]
    knapsack_capacity = 18  # Knapsack capacity

    max_value = fractional_knapsack(knapsack_capacity, items)
    print(f"Maximum value that can be obtained: {max_value}")
