def sort_by_age(tuples_list):
    """
    :param tuples_list: List of tuples, where each tuple is (name, age)
    :return: Sorted list of tuples by age
    """
    return sorted(tuples_list, key=lambda x: x[1])

# Example list of tuples
people = [("Eve", 32), ("Garvin", 8), ("Steve", 24), ("Esther", 54)]

# Call the function to sort by age
sorted_people = sort_by_age(people)

# Print the sorted list
print("Sorted list by age:", sorted_people)
