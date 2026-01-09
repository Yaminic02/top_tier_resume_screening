import re
from datetime import datetime

CURRENT_YEAR = datetime.now().year

def skill_freshness(text, skill):
    pattern = rf"{skill}.*?(20\d{{2}})"
    match = re.search(pattern, text.lower())
    if not match:
        return 0.5  # unknown freshness
    year = int(match.group(1))
    age = CURRENT_YEAR - year
    if age <= 1:
        return 1.0
    elif age <= 3:
        return 0.7
    else:
        return 0.4
