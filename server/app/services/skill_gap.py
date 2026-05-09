def calculate_skill_gap(user_skills: str, required_skills: str):

    # User skills → split by comma OR space
    user_set = set(s.strip().lower() for s in user_skills.replace(",", " ").split())

    # Required skills → KEEP phrases (split only by comma)
    required_list = [s.strip().lower() for s in required_skills.split(",")]

    missing_skills = []

    for skill in required_list:
        words = skill.split()

        # Check if ALL words of skill are present
        if not all(word in user_set for word in words):
            missing_skills.append(skill)

    return missing_skills