# Function to calculate the total cost of a given tour
def calculate_cost(graph, tour):
    cost = 0
    # Add the distance from the last city to the first city to complete the loop
    for i in range(len(tour) - 1):
        cost += graph[tour[i]][tour[i + 1]]
    # Add distance from the last city to the first city (return to start)
    cost += graph[tour[-1]][tour[0]]  # Ensure it returns to city 0
    return cost

# Function to generate all permutations of cities
def generate_permutations(graph, n, tour, visited, index, best_tour, mincost):
    # If we have visited all cities, calculate the cost of the tour
    if index == n:
        cost = calculate_cost(graph, tour)
        if cost < mincost:
            mincost = cost
            # Manually copy tour[] to best_tour[]
            for i in range(len(tour)):
                best_tour[i] = tour[i]
            # No need to append tour[0] because it's already in the tour
        return mincost

    # Try all cities that have not been visited
    for i in range(n):
        if not visited[i]:
            # Mark the city as visited and add it to the current tour
            visited[i] = True
            tour[index] = i
            # Recurse to fill the next position in the tour
            mincost = generate_permutations(graph, n, tour, visited, index + 1, best_tour, mincost)
            # Backtrack: unmark the city and try the next one
            visited[i] = False

    return mincost

# Brute force solution for TSP using adjacency matrix
def traveling_salesman_bruteforce(graph):
    n = len(graph)  # Number of cities
    
    # Variables to keep track of the best tour and minimum cost
    mincost = float('inf')
    best_tour = [-1] * n  # Initialize with -1 to hold the best tour
    tour = [-1] * n  # Initialize tour array
    visited = [False] * n  # Initialize visited array
    
    # Start the recursive permutation generation from city 0
    visited[0] = True
    tour[0] = 0  # Starting city (city 0)
    mincost = generate_permutations(graph, n, tour, visited, 1, best_tour, mincost)
    
    # Add city 0 at the end of the best tour to complete the cycle
    best_tour.append(best_tour[0])  # Close the loop
    
    return best_tour, mincost


graph =  [[0, 1000, 5000], [5000, 0, 1000], [1000, 5000, 0]]

best_tour, mincost = traveling_salesman_bruteforce(graph)

print(f"Best tour: {best_tour}")
print(f"Minimum cost: {mincost}")
