def score_resume(resume_skills, jd_skills, freshness_scores, tfidf_score):
    explanation = []
    score = 0
    for skill in jd_skills:
        if skill in resume_skills:
            freshness = freshness_scores.get(skill, 0.5)
            skill_score = 20 * freshness
            score += skill_score
            explanation.append(f"+ {skill.title()} ({int(skill_score)})")
        else:
            explanation.append(f"- Missing {skill.title()} (-15)")
            score -= 15

    tfidf_points = tfidf_score * 20
    score += tfidf_points
    explanation.append(f"+ Contextual Match (TF-IDF): {round(tfidf_score*100)}% (+{int(tfidf_points)})")

    return round(score, 2), explanation
