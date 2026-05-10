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
   git clone https://github.com/Noureesh2305/CareerCraft-AI.git
   cd CareerCraft-AI
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

## Technologies Used

- **Python** - Core programming language
- **Streamlit** - Web application framework
- **Pandas, NumPy** - Data manipulation
- **NLTK** - VADER Sentiment Analysis
- **Plotly** - Data visualization
- **PyPDF2** - PDF text extraction
- **Transformers, Torch** - NLP models

## Data

- `data/job_roles.csv`: List of job roles.
- `data/interview_questions.csv`: Interview questions database.
- `data/sample_resumes.csv`: Sample resume data.

## Project Structure

```
CareerCraft-AI/
├── app.py
├── requirements.txt
├── README.md
├── data/
│   ├── interview_questions.csv
│   ├── job_roles.csv
│   └── sample_resumes.csv
├── modules/
│   ├── feedback.py
│   ├── gap_analysis.py
│   ├── interview.py
│   ├── resume_score.py
│   ├── resume_upload.py
│   ├── sentiment_analysis.py
│   └── skill_analysis.py
└── utils/
    ├── charts.py
    └── text_cleaner.py
```

## Contributing

Feel free to contribute by submitting issues or pull requests. Add new features, improve models, or enhance the UI.

## License

MIT License
