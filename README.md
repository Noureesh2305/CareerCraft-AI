# CareerCraft AI

🎯 **CareerCraft AI** is an AI-powered career development assistant built with Streamlit. It helps users analyze their resumes, identify skill gaps, practice interviews, and visualize career paths.

## Features

- **Resume Upload & Analysis**: Upload PDF resumes for text extraction, skill identification (technical and soft skills), and scoring.
- **Skill Gap Analysis**: Compare extracted skills against selected job roles to highlight matched and missing skills.
- **Interview Practice**: Generate interview questions based on role, category, and difficulty. Analyze answers with sentiment analysis and provide personalized feedback.
- **Dashboard**: Visualize resume scores, skill gaps, and interview confidence with interactive charts.
- **Dashboard Enhancements**: Export feedback reports as text files.
- **User-Generated Content**: Contribute new interview questions to the database.
- **Learning Recommendations**: Get links to learning platforms like Coursera, Udemy, edX, Khan Academy, and LinkedIn Learning based on missing skills.
- **Career Path Visualization**: View a sample salary progression timeline for your selected job role.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/CareerCraft_AI.git
   cd CareerCraft_AI
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the app:
   ```bash
   streamlit run app.py
   ```

## Usage

1. Upload a PDF resume.
2. Select a job role from the dropdown.
3. View extracted skills, gap analysis, and resume score.
4. Practice interviews by selecting question types and difficulties.
5. Submit answers for sentiment analysis and feedback.
6. Explore the dashboard for visualizations.
7. Contribute questions, check learning links, and view career paths.

## Requirements

- Python 3.8+
- Libraries: See `requirements.txt`

## Data

- `data/job_roles.csv`: List of job roles.
- `data/interview_questions.csv`: Interview questions database.
- `data/sample_resumes.csv`: Sample resume data.

## Contributing

Feel free to contribute by submitting issues or pull requests. Add new features, improve models, or enhance the UI.

## License

MIT License