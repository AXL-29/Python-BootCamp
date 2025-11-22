# 5. Use print() to check your values
# The print() function is very useful for debugging.
# In a for loop or any calculation, it can be hard to see the intermediate results.
# Using print() allows you to see what's happening step by step.

# Ask the user for the number of pages and words per page
pages = int(input("Enter the number of pages: "))
words_per_page = int(input("Enter the number of words per page: "))

# Calculate the total number of words
total_words = pages * words_per_page

# Print the input values and the total words for verification
print(f"Pages: {pages}, Words per page: {words_per_page}")
print(f"Total words: {total_words}")
