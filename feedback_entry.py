def collect_feedback():
    name = input("Enter student name: ")
    score = int(input("Enter score (0-100): "))
    feedback = input("Enter feedback: ")
    return {"name": name, "score": score, "feedback": feedback}

if _name_ == "_main_":
    data = collect_feedback()
    print(data)
