import random  # Importing the random module

# Ask for the user's name
name = input("What Is Your Name? : ")

# Display a greeting with a divider
print("=" * 40)
print(f"Hello {name}, welcome to the Magic 8 Ball!")
print("=" * 40)

# Loop to keep asking questions
while True:
    question = input("Ask the Magic 8 Ball a yes/no question (or type 'exit' to quit): ")

    # Exit condition
    if question.lower() == 'exit':
        print("=" * 40)
        print("Thanks for using the Magic 8 Ball. Goodbye!")
        print("=" * 40)
        break

    # List of possible answers
    answers = [
        "Yes, definitely!",
        "No, not at all.",
        "Maybe, try again later.",
        "I don't think so.",
        "It is certain.",
        "Cannot predict now.",
        "Ask again later.",
        "Very doubtful."
    ]

    # Randomly select an answer and display it
    response = random.choice(answers)
    
    # Display the response with a divider
    print("=" * 40)
    print(f"The Magic 8 Ball says: {response}")
    print("=" * 40)

    # Ask if the user wants to ask another question
    continue_prompt = input("Do you want to ask another question? (yes/no): ")
    if continue_prompt.lower() != 'yes':
        print("=" * 40)
        print("Thanks for using the Magic 8 Ball. Goodbye!")
        print("=" * 40)
        break
