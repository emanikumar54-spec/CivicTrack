
def calculate_priority(severity, people_affected, safety_impact, category):

    score = 0

    # Severity: 1 to 5
    score += severity * 10

    # People affected
    if people_affected >= 500:
        score += 25
    elif people_affected >= 100:
        score += 20
    elif people_affected >= 50:
        score += 15
    elif people_affected >= 10:
        score += 10
    else:
        score += 5

    # Public safety impact: 0 to 5
    score += safety_impact * 5

    # Category importance
    category_weights = {
        "Road Damage": 10,
        "Water Supply": 8,
        "Electricity": 10,
        "Sanitation": 7,
        "Street Lights": 6,
        "Drainage": 8,
        "Other": 3
    }

    score += category_weights.get(category, 3)

    # Priority classification
    if score >= 100:
        priority = "Critical"
    elif score >= 80:
        priority = "High"
    elif score >= 55:
        priority = "Medium"
    else:
        priority = "Low"

    return {
        "priority": priority,
        "priority_score": score
    }
