print("Welcome to the WordCountTracker application")
sentence = input("Enter your text: ")

if sentence.strip():  # Check if the input sentence is not empty
    words = sentence.split()  # Split the input sentence into words
    num_words = len(words)  # Count the number of words
    print("Number of words:", num_words)
else:
    print("You did not enter any text. Please try again.")
  
