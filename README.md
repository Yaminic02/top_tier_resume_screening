🏆 Top-Tier Resume Screening System

An AI-powered resume screening system built with Python, NLP, and Streamlit that automatically ranks resumes against a job description using semantic similarity, skill extraction, resume quality analysis, and interactive dashboards.

This project is designed to simulate a real-world recruiter/ATS workflow and goes beyond basic keyword matching.

🚀 Features
🔍 Resume Analysis

PDF & DOCX resume parsing

Bias word removal (gendered / filler terms)

Resume section detection (Skills, Experience, Projects, Education)

🧠 Intelligent Matching

TF-IDF semantic similarity between resume sections and job description

Skill extraction from resumes & job descriptions

Skill gap analysis

Skill freshness detection (recent usage)

📊 Scoring & Ranking

Final weighted resume score

Resume quality score (structure, clarity, length, metrics)

Buzzword detection (flags low-signal resumes)

📈 Interactive Dashboard

Candidate ranking table

Score distribution charts

Resume quality visualization

Skill-gap heatmap

Expandable candidate insights

Score-based filtering (slider)

🧩 Project Architecture
top_tier_resume_screening/
│
├── app.py                     # Streamlit dashboard
├── requirements.txt           # Dependencies
├── data/
│   ├── skills.json            # Skill taxonomy
│   └── job_description.txt
│
├── parser/
│   └── resume_parser.py       # PDF/DOCX text extraction
│
├── logic/
│   ├── skill_extractor.py     # Skill extraction
│   ├── semantic_match.py      # TF-IDF semantic matching
│   ├── scoring.py             # Resume scoring logic
│   ├── resume_quality.py      # Resume quality scoring
│   ├── gap_analysis.py        # Skill gap detection
│   ├── freshness.py           # Skill recency analysis
│   ├── sections.py            # Resume section parsing
│   └── bias_utils.py          # Bias & buzzword detection
│
└── .gitignore

⚙️ Tech Stack

Python 3.10+

Streamlit – UI & dashboard

scikit-learn – TF-IDF vectorization

NLTK / Regex – NLP processing

Plotly – Interactive charts

PyPDF2 / python-docx – Resume parsing

▶️ How to Run Locally
1️⃣ Clone the Repository
git clone https://github.com/Yaminic02/top_tier_resume_screening.git
cd top_tier_resume_screening

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run the Application
streamlit run app.py

📌 Example Workflow

Paste a Job Description

Upload multiple resumes (PDF / DOCX)

Click Screen Resumes

View:

Ranked candidates

Skill gaps

Resume quality

TF-IDF similarity

Filter candidates using score slider

📊 Scoring Logic (High Level)
Component	Weight
Skill Match	High
TF-IDF Similarity	Medium
Skill Freshness	Medium
Resume Quality	Medium
Buzzword Penalty	Low

This ensures fair, explainable, and balanced scoring.

🎯 Why This Project Is Unique

✅ Not just keyword matching
✅ Recruiter-focused explanations
✅ Bias-aware resume processing
✅ Visual skill-gap analysis
✅ End-to-end ATS-style pipeline

This is a portfolio-grade project suitable for:

Data Analyst roles

ML / AI Internships

Applied NLP positions

🔮 Future Enhancements

Sentence-transformer embeddings (BERT)

Resume feedback generation

Export results to CSV

Candidate shortlisting recommendations

Resume anonymization

👤 Author

Yamini Chauhan
GitHub: @Yaminic02

⭐ If you like this project

Give it a ⭐ on GitHub — it helps a lot!