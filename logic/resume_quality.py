import re

def resume_quality(text):
    score = 0
    reasons = []

    # 1. Text length (ideal 200–2000 words)
    word_count = len(text.split())
    if 200 <= word_count <= 2000:
        score += 2
    else:
        reasons.append(f"Text length {word_count} words suboptimal")

    # 2. Section presence
    sections = ['skills', 'experience', 'education', 'projects']
    section_count = sum(1 for s in sections if s in text.lower())
    score += (section_count / len(sections)) * 2

    # 3. Bullet points
    bullets = len(re.findall(r"[\u2022•\-]", text))
    if bullets >= 5:
        score += 2
    else:
        reasons.append(f"Few bullet points ({bullets})")

    # 4. Keyword density (non-stopword meaningful words)
    words = [w for w in text.split() if len(w) > 2]
    unique_words = len(set(words))
    if unique_words / max(word_count,1) > 0.3:
        score += 2
    else:
        reasons.append("Low keyword diversity")

    # 5. Formatting / cleanliness (no excessive caps)
    caps_ratio = sum(1 for c in text if c.isupper()) / max(len(text),1)
    if caps_ratio < 0.05:
        score += 2
    else:
        reasons.append("Too many uppercase letters")

    return round(score,1), reasons
