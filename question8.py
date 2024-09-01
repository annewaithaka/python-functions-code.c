def merge_dicts(dict1, dict2):
    """    
    :param dict1: First dictionary
    :param dict2: Second dictionary
    :return: Merged dictionary with summed values for common keys
    """
    # Create a new dictionary to hold the merged results
    merged_dict = {}
    
    # Add all items from the first dictionary to the merged dictionary
    for key, value in dict1.items():
        merged_dict[key] = value
    
    # Add items from the second dictionary to the merged dictionary
    for key, value in dict2.items():
        if key in merged_dict:
            # If key already exists, sum the values
            merged_dict[key] += value
        else:
            # Otherwise, add the key-value pair
            merged_dict[key] = value
    
    return merged_dict

# Example usage
dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 15, 'c': 25, 'd': 35, 'e': 38}

# Call the function to merge the dictionaries
merged_dict = merge_dicts(dict1, dict2)

# Print the merged dictionary
print(merged_dict)  # Output: {'a': 10, 'b': 35, 'c': 55, 'd': 35}
