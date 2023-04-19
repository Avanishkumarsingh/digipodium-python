import streamlit as st

# Define the quiz question and answer
quiz_data = {
    "What is the currency of japan?": ["Yen", "Dollar", "Pound", "Euro"],
    "What is the capital of Australia?": ["Canberra", "Sydney", "Melbourne", "Rome"],
    "Where is the centre for cellular and molecular biology situated?": ["Hyderabad", "Patna", "Jaipur", "New Delhi"],
    "Where is the railway staff college located?": ["Vadodara", "Pune", "Allahabad", "New Delhi"],
    "January 15 is celebrated as at?": ["Army Day", "Republic Day", "Teacher's Day", "Earth Day"]
}

# Function to display quiz question and get the answers

def display_quiz_questions(quiz_data):
    num_questions = len(quiz_data)
    num_correct = 0
    num_incorrect = 0

    for question, options in quiz_data.items():
        st.write(question)
        user_answer = st.selectbox("Select your answer:", options)
        correct_answer = options[0]
        if user_answer == correct_answer:
            num_correct += 1
        else:
            num_incorrect += 1
    
    return num_correct, num_incorrect

# Streamlit app

def main():
    st.title("Quiz Game")
    st.write("Select your answers:")

    num_correct, num_incorrect = display_quiz_questions(quiz_data)

    st.write(f"Number of correct answers: {num_correct}")
    st.write(f"Number of incorrect answers: {num_incorrect}")

if __name__ == "__main__":
    main()