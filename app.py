import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff

from parser.resume_parser import extract_text
from logic.skill_extractor import extract_skills
from logic.freshness import skill_freshness
from logic.gap_analysis import skill_gap
from logic.scoring import score_resume
from logic.semantic_match import weighted_tfidf
from logic.sections import extract_sections
from logic.bias_utils import remove_bias, detect_buzzwords
from logic.resume_quality import resume_quality

# -----------------------------
# Streamlit Config
# -----------------------------
st.set_page_config(
    page_title="🏆 Resume Screening System",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🏆 Resume Screening System")

# -----------------------------
# Job Description Input
# -----------------------------
jd_text = st.text_area("Paste Job Description here").lower()

# -----------------------------
# Resume Upload
# -----------------------------
uploaded_files = st.file_uploader(
    "Upload Resumes (PDF/DOCX)", 
    type=["pdf", "docx"], 
    accept_multiple_files=True
)

# -----------------------------
# Screen Resumes
# -----------------------------
if st.button("Screen Resumes") and jd_text and uploaded_files:
    results = []
    jd_skills = extract_skills(jd_text)

    for file in uploaded_files:
        # --- Extract & clean text ---
        text = extract_text(file)
        text = remove_bias(text)

        # --- Skill Extraction ---
        resume_skills = extract_skills(text)
        freshness = {s: skill_freshness(text, s) for s in resume_skills}

        # --- TF-IDF Semantic Matching ---
        sections = extract_sections(text)
        tfidf_score = weighted_tfidf(jd_text, sections)

        # --- Resume Scoring ---
        final_score, explanation = score_resume(resume_skills, jd_skills, freshness, tfidf_score)

        # --- Skill Gaps & Buzzwords ---
        gaps = skill_gap(jd_skills, resume_skills)
        buzzwords = detect_buzzwords(text, resume_skills)

        # --- Resume Quality ---
        quality_score, quality_issues = resume_quality(text)

        results.append({
            "Candidate": file.name,
            "Score": final_score,
            "TF-IDF": tfidf_score,
            "Resume Quality": quality_score,
            "Skill Gaps": gaps,
            "Buzzwords": buzzwords,
            "Quality Issues": quality_issues,
            "Explanation": explanation
        })

    df = pd.DataFrame(results).sort_values(by="Score", ascending=False)

    # -----------------------------
    # Slider Filter for Minimum Score
    # -----------------------------
    st.sidebar.markdown("### Filter Candidates by Minimum Score")
    min_score = st.sidebar.slider("Minimum Score", 0, 100, 0)
    filtered_df = df[df["Score"] >= min_score]

    if filtered_df.empty:
        st.warning("No candidates meet the minimum score threshold.")
    else:
        # -----------------------------
        # Metrics at Top
        # -----------------------------
        st.markdown("### 📊 Summary Metrics")
        col1, col2, col3 = st.columns(3)
        col1.metric("Top Score", filtered_df["Score"].max())
        col2.metric("Average Resume Quality", round(filtered_df["Resume Quality"].mean(),1))
        col3.metric("Candidates Screened", len(filtered_df))

        st.markdown("---")

        # -----------------------------
        # Tabs
        # -----------------------------
        tab1, tab2, tab3 = st.tabs(["Ranking Table", "Charts & Heatmaps", "Candidate Details"])

        # --- Tab 1: Ranking Table ---
        with tab1:
            st.subheader("Candidate Ranking")
            st.dataframe(filtered_df[["Candidate", "Score", "TF-IDF", "Resume Quality", "Buzzwords"]])

        # --- Tab 2: Charts & Heatmaps ---
        with tab2:
            # Score Distribution
            st.subheader("Score Distribution")
            fig_score = px.bar(
                filtered_df, x="Candidate", y="Score", text="Score",
                color="Score", color_continuous_scale='Viridis'
            )
            st.plotly_chart(fig_score, use_container_width=True)

            # Resume Quality
            st.subheader("Resume Quality Distribution")
            fig_quality = px.bar(
                filtered_df, x="Candidate", y="Resume Quality", text="Resume Quality",
                color="Resume Quality", color_continuous_scale='Blues'
            )
            st.plotly_chart(fig_quality, use_container_width=True)

            # TF-IDF
            st.subheader("TF-IDF Similarity")
            fig_tfidf = px.bar(
                filtered_df, x="Candidate", y="TF-IDF", text="TF-IDF",
                color="TF-IDF", color_continuous_scale='Oranges'
            )
            st.plotly_chart(fig_tfidf, use_container_width=True)

            # Skill Gap Heatmap
            st.subheader("Skill Gap Heatmap")
            skills = list(jd_skills.keys())
            candidates = filtered_df["Candidate"].tolist()

            heatmap_data = []
            for idx, row in filtered_df.iterrows():
                row_data = [1 if skill in row["Skill Gaps"] else 0 for skill in skills]
                heatmap_data.append(row_data)

            # Convert z to list of lists
            z = [list(map(int, r)) for r in heatmap_data]

            fig_heatmap = ff.create_annotated_heatmap(
                z=z,
                x=skills,
                y=candidates,
                colorscale='RdYlGn_r',  # red = missing, green = present
                showscale=True
            )
            st.plotly_chart(fig_heatmap, use_container_width=True)

        # --- Tab 3: Candidate Details ---
        with tab3:
            st.subheader("Candidate Analysis")
            for idx, row in filtered_df.iterrows():
                with st.expander(f"{row['Candidate']} Details"):
                    st.markdown(f"**Score:** {row['Score']}")
                    st.markdown(f"**TF-IDF:** {row['TF-IDF']}")
                    st.markdown(f"**Resume Quality:** {row['Resume Quality']}")
                    st.markdown(f"**Skill Gaps:** {row['Skill Gaps']}")
                    st.markdown(f"**Buzzwords:** {row['Buzzwords']}")
                    st.markdown(f"**Quality Issues:** {row['Quality Issues']}")
                    st.markdown("**Explanation:**")
                    for e in row["Explanation"]:
                        st.write("-", e)

            st.markdown("💡 Expand each candidate to see detailed gaps, evidence, and scoring.")
