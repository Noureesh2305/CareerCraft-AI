def calculate_resume_score(matched_skills, missing_skills, soft_skills, resume_text):
    """
    Calculate resume score out of 100
    """

    score = 0

    # 1️⃣ Technical Skill Score (60%)
    total_skills = len(matched_skills) + len(missing_skills)

    if total_skills > 0:
        tech_score = (len(matched_skills) / total_skills) * 60
    else:
        tech_score = 0

    # 2️⃣ Soft Skills Score (20%)
    if len(soft_skills) >= 3:
        soft_score = 20
    elif len(soft_skills) == 2:
        soft_score = 15
    elif len(soft_skills) == 1:
        soft_score = 10
    else:
        soft_score = 0

    # 3️⃣ Resume Length Score (20%)
    word_count = len(resume_text.split())

    if word_count >= 300:
        length_score = 20
    elif word_count >= 200:
        length_score = 15
    elif word_count >= 100:
        length_score = 10
    else:
        length_score = 5

    # Final score
    score = int(tech_score + soft_score + length_score)

    return score
