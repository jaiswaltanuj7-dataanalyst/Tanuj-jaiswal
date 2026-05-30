def run_quiz():
    questions = [
        {
            "question": "What is the capital of India?",
            "options": ["A) Delhi", "B) Uttar pradesh", "C) Goa", "D) Kolkata"],
            "answer": "A) Delhi"
        },
        {
            "question": "What is 2 + 2?",
            "options": ["A) 3", "B) 4", "C) 5", "D) 6"],
            "answer": "B) 4"
        },
        {
            "question": "What is the largest planet in our solar system?",
            "options": ["A) Earth", "B) Jupiter", "C) Saturn", "D) Mars"],
            "answer": "B) Jupiter"
        },
        {
            "question": "Who is the 'Father of India'?",
            "options": ["A) Mahatma Gandhi", "B) Jawaharlal Nehru", "C) Rajendra prasad", "D) Bhagat singh"],
            "answer": "A)Mahatma Gandhi"
        }
    ]

    score = 0
 
    for index,q in enumerate(questions):  
        print(f"Q{index + 1}: {q['question']}")
        for option in q['options']:
            print(option)
        
        user_answer = input("Your answer(A/B/C/D): ") 
        if user_answer.strip().upper() == q['answer'][0]:
            print("Correct!\n")
            score += 1

    print(f"Your final score is {score}/{len(questions)}")

run_quiz()