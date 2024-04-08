questions = [
    {
        "question": "What is the capital of Australia?",
        "options": ["A: Sydney", "B: Canberra", "C: Melbourne", "D: Brisbane" ],
        "answer": "B"
    },
    
    {
        "question": "Which ocean is largest by area?",
        "options": ["A: Atlantic Ocean", "B: Indian Ocean", "C: Pacific Ocean", "D: Arctic Ocean" ],
        "answer": "C"
    },

        {
        "question": "Which river is the longest in the world?",
        "options": ["A: Nile", "B: Amazon", "C: Mississippi", "D: Congo River" ],
        "answer": "A"
    },

        {
        "question": "What country is both an island and a continent?",
        "options": ["A: Japan", "B: Australia", "C: Indonesia", "D: Greenland" ],
        "answer": "B"
    },

        {
        "question": "What is the smallest country in the world by land area?",
        "options": ["A: Monaco", "B: Luxemburg", "C: Vatican City", "D: San Marino" ],
        "answer": "C"
    },

        {
        "question": "What is the capital of the United States?",
        "options": ["A: New York City", "B: Washington D.C.", "C: Los Angeles", "D: Las Vegas" ],
        "answer": "B"
    },

        {
        "question": "What is the largest country by land area?",
        "options": ["A: United States", "B: China", "C: Brazil", "D: Russia" ],
        "answer": "D"
    },

        {
        "question": "Which continent is home to the Amazon Rainforest?",
        "options": ["A: South America", "B: Africa", "C: Europe", "D: Asia" ],
        "answer": "A"
    },

    {
        "question": "What is the most populated country?",
        "options": ["A: India", "B: China", "C: United States", "D: Russia" ],
        "answer": "A"
    },

        {
        "question": "What is the capital of Spain?",
        "options": ["A: Barcelona", "B: Madrid", "C: Seville", "D: Málaga" ],
        "answer": "B"
    },
]

# This function will define the quiz code on launch
def run_quiz(questions):
    score = 0  # Initialize score to 0 and create a variable "score" to store the value of correct answers

    # Loop through all the questions. This will follow all the questions above until finished
    for question in questions:
        print("\n" + question["question"])  # Print the question
        for option in question["options"]:
            print(option)  # Print all the answer options

        # Get the user's answer
        user_answer = input("Enter your answer (A, B, C, or D): ").strip().upper()

        # Check if the user's answer is correct
        if user_answer == question["answer"]:
            print("Correct!")
            score += 1  # Increment score if correct
        else:
            print("Wrong answer.")

    # Print the final score from the stored variable
    print(f"\nYou got {score} out of {len(questions)} questions correct!")

run_quiz(questions)