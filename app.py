import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from io import StringIO

# ===== IMPORT MODULES =====
from modules.resume_upload import extract_text_from_pdf
from utils.text_cleaner import clean_text
from modules.skill_analysis import extract_skills
from modules.gap_analysis import skill_gap_analysis
from modules.resume_score import calculate_resume_score
from modules.interview import get_interview_question
from modules.sentiment_analysis import analyze_sentiment
from modules.feedback import generate_feedback
from utils.charts import (
    resume_score_chart,
    skill_gap_chart,
    sentiment_confidence_chart
)

# ===== PAGE CONFIG =====
st.set_page_config(
    page_title="CareerCraft AI",
    layout="wide"
)

st.title("🎯 CareerCraft AI – Resume, Skill & Interview Assistant")

# ===== DEFAULT VARIABLES (VERY IMPORTANT) =====
resume_score = None
sentiment = None
confidence = None

# ===== LOAD JOB ROLES =====
job_data = pd.read_csv("data/job_roles.csv")
job_roles = job_data["job_role"].tolist()

# ===== RESUME UPLOAD =====
st.header("📄 Resume Upload")

uploaded_file = st.file_uploader(
    "Upload your resume (PDF only)",
    type=["pdf"]
)

if uploaded_file is not None:

    # ===== TEXT EXTRACTION & CLEANING =====
    raw_text = extract_text_from_pdf(uploaded_file)
    resume_text = clean_text(raw_text)

    st.subheader("📃 Extracted Resume Text")
    st.text_area("Resume Content", resume_text, height=200)

    # ===== SKILL EXTRACTION =====
    tech_skills, soft_skills = extract_skills(resume_text)

    st.subheader("🛠️ Extracted Skills")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Technical Skills")
        st.write(tech_skills if tech_skills else "No technical skills detected")

    with col2:
        st.markdown("### Soft Skills")
        st.write(soft_skills if soft_skills else "No soft skills detected")

    # ===== JOB ROLE SELECTION =====
    st.subheader("🎯 Select Job Role")
    selected_role = st.selectbox("Choose a role", job_roles)

    # ===== SKILL GAP ANALYSIS =====
    matched, missing = skill_gap_analysis(tech_skills, selected_role)

    st.subheader("📊 Skill Gap Analysis")
    col3, col4 = st.columns(2)

    with col3:
        st.markdown("### ✅ Matched Skills")
        st.write(matched if matched else "No matched skills")

    with col4:
        st.markdown("### ❌ Missing Skills")
        st.write(missing if missing else "No missing skills")

    # ===== RESUME SCORE (DEFINED BEFORE USE) =====
    resume_score = calculate_resume_score(
        matched,
        missing,
        soft_skills,
        resume_text
    )

    st.subheader("📈 Resume Score")
    st.metric("Resume Score (Out of 100)", resume_score)

    if resume_score >= 80:
        st.success("Excellent Resume! Ready for interviews 🎉")
    elif resume_score >= 60:
        st.warning("Good Resume. Needs improvement ⚡")
    else:
        st.error("Resume needs major improvement 🚧")

    # ===== INTERVIEW PRACTICE =====
    st.divider()
st.header("🗣️ Interview Practice")

st.subheader("🎯 Interview Settings")

col1, col2 = st.columns(2)

with col1:
    category = st.selectbox(
        "Select Question Type",
        ["Basic", "Technical", "Aptitude", "Hard", "Extreme"]
    )

with col2:
    difficulty = st.selectbox(
        "Select Difficulty Level",
        ["Easy", "Medium", "Hard"]
    )

if st.button("🎯 Get Interview Question"):
    st.session_state["question"] = get_interview_question(
        selected_role,
        category,
        difficulty
    )

if "question" in st.session_state:
    st.subheader("📌 Interview Question")
    st.write(st.session_state["question"])

    user_answer = st.text_area(
        "✍️ Type your answer here",
        height=150
    )

    if st.button("Submit Answer"):
        sentiment, confidence = analyze_sentiment(user_answer)

        st.subheader("🧠 Answer Tone Analysis")
        st.write(f"**Tone:** {sentiment}")
        st.write(f"**Confidence Score:** {round(confidence, 2)}")

        feedback = generate_feedback(
            resume_score,
            missing,
            sentiment,
            confidence
        )

        st.subheader("📝 Personalized Feedback")
        for point in feedback:
            st.write(point)

    # ===== DASHBOARD =====
    st.divider()
    st.header("📊 CareerCraft AI Dashboard")

    st.subheader("📈 Resume Score Overview")
    st.plotly_chart(
        resume_score_chart(resume_score),
        use_container_width=True
    )

    st.subheader("🛠️ Skill Gap Overview")
    st.plotly_chart(
        skill_gap_chart(matched, missing),
        use_container_width=True
    )

    if confidence is not None:
        st.subheader("🧠 Interview Confidence")
        st.plotly_chart(
            sentiment_confidence_chart(confidence),
            use_container_width=True
        )

    # ===== DASHBOARD ENHANCEMENTS =====
    st.subheader("📤 Export Report")
    if st.button("Download Feedback Report"):
        report = f"Resume Score: {resume_score}\nMatched Skills: {matched}\nMissing Skills: {missing}\nFeedback: {'; '.join(feedback)}"
        st.download_button("Download as Text", data=report, file_name="career_report.txt", mime="text/plain")

    # ===== USER GENERATED CONTENT =====
    st.divider()
    st.header("📝 Contribute Interview Questions")
    with st.form("question_form"):
        new_question = st.text_area("Submit a new interview question")
        q_category = st.selectbox("Category", ["Basic", "Technical", "Aptitude", "Hard", "Extreme"])
        q_difficulty = st.selectbox("Difficulty", ["Easy", "Medium", "Hard"])
        submitted = st.form_submit_button("Submit")
        if submitted and new_question:
            # Save to CSV
            new_data = pd.DataFrame([[new_question, q_category, q_difficulty]], columns=["question", "category", "difficulty"])
            try:
                existing = pd.read_csv("data/interview_questions.csv")
                updated = pd.concat([existing, new_data], ignore_index=True)
            except FileNotFoundError:
                updated = new_data
            updated.to_csv("data/interview_questions.csv", index=False)
            st.success("Question submitted! Thank you for contributing.")

    # ===== INTEGRATION WITH LEARNING PLATFORMS =====
    st.divider()
    st.header("📚 Learning Recommendations")
    if missing:
        st.write("Based on your missing skills, here are some recommended learning platforms:")
        platforms = {
            "Coursera": "https://www.coursera.org",
            "Udemy": "https://www.udemy.com",
            "edX": "https://www.edx.org",
            "Khan Academy": "https://www.khanacademy.org",
            "LinkedIn Learning": "https://www.linkedin.com/learning"
        }
        for name, url in platforms.items():
            st.markdown(f"- [{name}]({url}) - Search for courses on {', '.join(missing[:3])}")
    else:
        st.write("No missing skills detected. Great job!")

    # ===== CAREER PATH VISUALIZATION =====
    st.divider()
    st.header("🚀 Career Path Visualization")
    # Simple timeline chart
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=["Entry Level", "Mid Level", "Senior Level", "Expert"],
        y=[30, 60, 90, 120],  # Example salary progression
        mode='lines+markers',
        name='Salary Progression (k USD)'
    ))
    fig.update_layout(title="Sample Career Path for " + selected_role, xaxis_title="Career Stage", yaxis_title="Salary (k USD)")
    st.plotly_chart(fig, use_container_width=True)

else:
    st.info("👆 Please upload a resume PDF to begin.")
