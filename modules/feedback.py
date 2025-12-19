def generate_feedback(resume_score, missing_skills, sentiment, sentiment_score):
    """
    Generate personalized feedback
    """

    feedback = []

    # Resume score feedback
    if resume_score >= 80:
        feedback.append("✅ Your resume is strong and well-aligned with the selected job role.")
    elif resume_score >= 60:
        feedback.append("⚠️ Your resume is decent but needs improvement in some areas.")
    else:
        feedback.append("❌ Your resume needs significant improvement to match the job role.")

    # Skill gap feedback
    if missing_skills:
        feedback.append(
            f"📌 Focus on improving these missing skills: {', '.join(missing_skills)}."
        )
    else:
        feedback.append("🎉 You already meet all required technical skills for this role.")

    # Sentiment feedback
    if sentiment == "POSITIVE":
        feedback.append("😊 Your interview answer sounds confident and positive.")
    elif sentiment == "NEGATIVE":
        feedback.append("😟 Your answer sounds slightly unsure. Try being more assertive.")
    else:
        feedback.append("😐 Your answer is neutral. Adding examples can improve it.")

    return feedback   # ✅ THIS LINE FIXES EVERYTHING
