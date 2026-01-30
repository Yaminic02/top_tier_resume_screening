🏆 Top-Tier Resume Screening System  
Production-Grade Resume Intelligence with Deterministic Logic + NLP Scoring

---

🚀 Project Overview

Top-Tier Resume Screening System is a **production-oriented ATS-style AI system** designed to help recruiters screen resumes **fairly, explainably, and at scale**.

Unlike basic keyword-based screeners, this system **separates deterministic resume evaluation logic from NLP similarity scoring**, ensuring transparent and auditable hiring decisions.

The goal is not “AI magic” — but **reliable recruiter decision support**.

---

💡 Why This Project Stands Out

✔ Goes beyond keyword matching  
✔ Resume decisions are explainable and score-driven  
✔ Bias-aware preprocessing (buzzwords, filler terms)  
✔ Mirrors real recruiter / ATS workflows  
✔ Designed for clarity, fairness, and scalability  

---

🧠 Design Philosophy

This project follows a strict hiring-AI principle:

“AI should assist recruiters — not silently filter candidates.”

All resume scores are computed using **explicit, weighted logic**.  
NLP is used to **support relevance analysis**, not replace human judgment.

---

✨ Core Capabilities

• PDF & DOCX resume parsing  
• Resume section detection (Skills, Experience, Projects, Education)  
• Skill extraction from resumes and job descriptions  
• TF-IDF semantic similarity scoring  
• Skill gap analysis  
• Skill freshness (recent usage detection)  
• Resume quality scoring (structure, clarity, metrics)  
• Buzzword & low-signal resume detection  
• Final weighted ranking with explainable scores  
• Interactive Streamlit dashboard  

---

🏗️ System Architecture

Recruiter Input (Job Description + Resumes)  
↓  
Resume Parsing & Section Detection  
↓  
Skill Extraction + Bias Cleaning  
↓  
Semantic Similarity (TF-IDF)  
↓  
Deterministic Scoring Engine  
↓  
Ranked, Explainable Candidate Output  

---

📊 Scoring Strategy (High Level)

Skill Match → High impact  
Semantic Similarity → Medium impact  
Skill Freshness → Medium impact  
Resume Quality → Medium impact  
Buzzword Penalty → Low impact  

This ensures **balanced, fair, and recruiter-friendly rankings**.

---

📈 Recruiter Dashboard

• Ranked candidate table  
• Score distribution visualization  
• Resume quality indicators  
• Skill gap insights  
• Expandable candidate profiles  
• Score-based filtering slider  

---

🔐 Safety & Fairness Considerations

• No black-box filtering  
• No hidden rejection logic  
• Bias word detection & reduction  
• Explainable scoring components  
• Human-in-the-loop friendly design  

---

🧰 Technology Stack

Language: Python  
UI: Streamlit  
NLP: TF-IDF (scikit-learn)  
Text Processing: NLTK, Regex  
Visualization: Plotly  
Resume Parsing: PyPDF2, python-docx  

---

📂 Project Structure

```text
top_tier_resume_screening/
├── app.py                  # Streamlit application
├── requirements.txt
├── data/
│   ├── skills.json
│   └── job_description.txt
├── parser/
│   └── resume_parser.py
├── logic/
│   ├── skill_extractor.py
│   ├── semantic_match.py
│   ├── scoring.py
│   ├── resume_quality.py
│   ├── gap_analysis.py
│   ├── freshness.py
│   ├── sections.py
│   └── bias_utils.py
└── .gitignore

```
---

🌱 Future Enhancements

- Transformer-based embeddings (BERT / Sentence-Transformers)
- Resume feedback generation for candidates
- CSV / ATS export support
- Candidate shortlisting recommendations
- Resume anonymization for bias reduction

---

👩‍💻 Author

Yamini Chauhan
GitHub: @Yaminic02

This project demonstrates ATS-level thinking, fairness-aware NLP, and production-ready data pipelines.
