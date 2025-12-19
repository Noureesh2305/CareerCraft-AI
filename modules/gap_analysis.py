import pandas as pd

def skill_gap_analysis(resume_skills, selected_role):
    """
    Compare resume skills with job role required skills
    """

    # Load job role data
    job_data = pd.read_csv("data/job_roles.csv")

    # Get required skills for selected role
    role_skills = job_data[job_data["job_role"] == selected_role]["required_skills"].values

    if len(role_skills) == 0:
        return [], []

    # Convert string skills to list
    required_skills = [skill.strip().lower() for skill in role_skills[0].split(",")]

    resume_skills = [skill.lower() for skill in resume_skills]

    matched_skills = []
    missing_skills = []

    for skill in required_skills:
        if skill in resume_skills:
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)

    return matched_skills, missing_skills
