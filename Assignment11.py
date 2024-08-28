# Task 1: Flight Route Comparison

def compare_flight_routes(our_routes, competitor_routes):
    # 1. Destinations that both airlines fly to
    common_routes = our_routes.intersection(competitor_routes)
    
    # 2. Destinations unique to our airline
    unique_to_our_airline = our_routes.difference(competitor_routes)
    
    # 3. Destinations that neither airline shares
    all_routes = our_routes.union(competitor_routes)
    neither_shared = all_routes.difference(common_routes)

    return common_routes, unique_to_our_airline, neither_shared

# Example sets of flight destinations
our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

# Compare routes and print results
common_routes, unique_to_our_airline, neither_shared = compare_flight_routes(our_routes, competitor_routes)

print("Destinations both airlines fly to:", common_routes)
print("Destinations unique to our airline:", unique_to_our_airline)
print("Destinations that neither airline shares:", neither_shared)
print()  # Blank line for readability

# Task 2: Duplicate Entries Cleanup

def remove_duplicates(customer_ids):
    # Convert the list to a set to remove duplicates
    unique_customer_ids = set(customer_ids)
    return unique_customer_ids

# Example list of customer IDs
customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]

# Remove duplicates and print the result
unique_customer_ids = remove_duplicates(customer_ids)
print("Unique customer IDs:", unique_customer_ids)
