import re
from logic.skill_extractor import SKILLS

def remove_bias(text):
    text = re.sub(r"(Mr\.|Mrs\.|Ms\.|Dr\.)\s+\w+", "", text)
    text = re.sub(r"(gender|male|female)", "", text)
    text = re.sub(r"(college|university|location):.*", "", text)
    return text

def detect_buzzwords(text, skills_detected):
    buzzwords = []
    for skill in skills_detected:
        if skill in text:
            subskills = SKILLS[skill]
            if not any(sub in text for sub in subskills):
                buzzwords.append(skill)
    return buzzwords
