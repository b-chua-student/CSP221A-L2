# Replicate database SQL structure

student_records = {
    1: {
        "name": "Amara",
        "favorite_subjects": ["Geometry", "Math", "Science"],
        "grades": [92, 88, 95]
    },
    2: {
        "name": "Leo",
        "favorite_subjects": ["PE", "Geology", "AI"],
        "grades": [70, 65, 80]
    },
}

# Used type hints to show required data type for function parameters

def add_students(name: str, favorite_subjects: list[str], grades: list[float]):
    student_records[len(student_records) + 1] = {
        "name": name,
        "favorite_subjects": favorite_subjects,
        "grades": grades,
    }

add_students("John", ["Physics", "History", "PE"], [98, 77, 88])
add_students("Jacob", ["Foodtech", "ML", "Java"], [91, 98, 67])

def print_formatted_student_records():
    for student_id, data in student_records.items():
        subjects = ", ".join(data["favorite_subjects"])
        grades = ", ".join(map(str, data["grades"]))
        
        print(f"Name: {data['name']}\nSubjects: {subjects}\nGrades: {grades}\n") # Used F-string to make it easier
        
print_formatted_student_records()

def filter_averages(threshold_value: int, dictionary: dict):
    filtered_student_records = {
        data["name"]: sum(data["grades"]) / len(data["grades"])
        for student_id, data in student_records.items()
        if sum(data["grades"]) / len(data["grades"]) >= threshold_value
    }

    return filtered_student_records # why cant i assign variable in return statement bruh

print(filter_averages(80, student_records))
