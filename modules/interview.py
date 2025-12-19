import pandas as pd
import random

def get_interview_question(selected_role, category, difficulty):
    """
    Get a random interview question based on role, category, and difficulty
    """

    data = pd.read_csv("data/interview_questions.csv")

    filtered = data[
    (data["job_role"] == selected_role) &
    (data["category"] == category) &
    (data["difficulty"] == difficulty)
]


    if filtered.empty:
        return "No question available for this selection."

    return random.choice(filtered["question"].tolist())
