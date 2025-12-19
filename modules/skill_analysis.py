def extract_skills(resume_text):
    """
    Extract skills from resume text using keyword matching
    """

    # Convert resume text to lowercase for uniform comparison
    resume_text = resume_text.lower()

    # Predefined skill lists (can be expanded)
    technical_skills = [
        "python", "java", "c", "c++", "sql", "machine learning",
        "deep learning", "nlp", "data analysis", "tensorflow",
        "pandas", "numpy", "scikit-learn", "streamlit"
    ]

    soft_skills = [
        "communication", "teamwork", "leadership",
        "problem solving", "time management",
        "critical thinking", "adaptability"
    ]

    found_technical_skills = []
    found_soft_skills = []

    # Check technical skills
    for skill in technical_skills:
        if skill in resume_text:
            found_technical_skills.append(skill)

    # Check soft skills
    for skill in soft_skills:
        if skill in resume_text:
            found_soft_skills.append(skill)

    return found_technical_skills, found_soft_skills
