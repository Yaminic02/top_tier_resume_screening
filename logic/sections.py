import re

def extract_sections(text):
    sections = {"skills": "", "experience": "", "summary": ""}
    skills_match = re.search(r"skills(.*?)(experience|projects|education)", text, re.S)
    exp_match = re.search(r"experience(.*?)(projects|education)", text, re.S)
    summary_match = re.search(r"(summary|profile)(.*?)(skills|experience)", text, re.S)
    if skills_match:
        sections["skills"] = skills_match.group(1)
    if exp_match:
        sections["experience"] = exp_match.group(1)
    if summary_match:
        sections["summary"] = summary_match.group(2)
    return sections
