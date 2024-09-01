def vowel_count(text):
    # Creating a string of vowels (both lowercase and uppercase)
    vowels = "aeiouAEIOU"
     
    # Using list comprehension to count the number of vowels in the string
    count = len([char for char in text if char in vowels])
     
    # Printing the count of vowels in the string
    print("No. of vowels:", count)

def get_text_only():
    while True:
        text = input("Enter a text: ")
        if text.isalpha():
            return text
        else:
            print("Invalid input. Please enter text only (no numbers or special characters).")

# Initialize a string variable
text = get_text_only()

# Function Call
vowel_count(text)
