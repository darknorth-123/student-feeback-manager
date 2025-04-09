def generate_report(feedback_list, filename="feedback_report.txt"):
    with open(filename, "w") as file:
        file.write("Student Feedback Report\n")
        for entry in feedback_list:
            file.write(f"Name: {entry['name']}\n")
            file.write(f"Score: {entry['score']}\n")
            file.write(f"Feedback: {entry['feedback']}\n")
    print(f"Report saved as '{filename}'")
