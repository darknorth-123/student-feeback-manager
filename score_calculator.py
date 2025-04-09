def calculate_average(feedback_list):
    if not feedback_list:
        return 0
    total = sum(entry['score'] for entry in feedback_list)
    return total / len(feedback_list)

if _name_ == "_main_":
    example_data = [
        {"name": "A", "score": 90, "feedback": "Good"},
        {"name": "B", "score": 80, "feedback": "Nice work"}
    ]
    avg = calculate_average(example_data)
    print("Average score:", avg)
