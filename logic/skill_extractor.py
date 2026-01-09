import json

with open("data/skills.json") as f:
    SKILLS = json.load(f)

def extract_skills(text):
    found = {}
    for skill, subskills in SKILLS.items():
        if skill in text:
            found[skill] = []
            for sub in subskills:
                if sub in text:
                    found[skill].append(sub)
    return found
