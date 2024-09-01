# Define a function named 'reverse' that takes an iterable 'text' as input and returns its reverse
def reverse(text):
    # Using slicing with [::-1] reverses the input 'text' and returns the reversed version
    return text[::-1]

def get_text_only():
    while True:
        text = input("Enter the text: ")
        if text.isalpha():
            return text
        else:
            print("Invalid input. Please enter text only (no numbers or special characters).")

# Initialize a string variable
text = get_text_only()

# Print the original string
print("Original string:", text)

# Print the reversed string
print("Reversed string:", reverse(text))
