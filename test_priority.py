from priority_engine import calculate_priority
result = calculate_priority(
    severity=5,
    people_affected=500,
    safety_impact=5,
    category="Road Damage"
)

print("Priority:", result["priority"])
print("Score:", result["priority_score"])
