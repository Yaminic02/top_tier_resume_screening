def skill_gap(jd_skills, resume_skills):
    missing = {}
    for skill, subskills in jd_skills.items():
        if skill not in resume_skills:
            missing[skill] = subskills
        else:
            gap = set(subskills) - set(resume_skills[skill])
            if gap:
                missing[skill] = list(gap)
    return missing
