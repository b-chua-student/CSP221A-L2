from abc import abstractmethod

class Student: # Student entity representing a Student
    def __init__(self, student_name: str, fav_subjects: list[str], grades: list[int]):
        self.name = student_name
        self.fav_subjects = fav_subjects
        self.grades = [grade for grade in grades if 60 <= grade <= 100]

class ProductRepository:
    @abstractmethod
    def add_student(self, student: Student):
        pass

    @abstractmethod
    def get_student_by_name(self, student_name: str):
        pass

    @abstractmethod
    def update_student(self, student: Student):
        pass

    @abstractmethod
    def delete_student(self, student_name: str):
        pass

class DictionaryStudentRepository:
    def __init__(self):
        self.roster = {
            "Amara": [92, 88, 95],
            "Leo": [70, 65, 80]
        }

    def add_student(self, student: Student):
        self.roster[student.name] = { 
            "fav_subjects": student.fav_subjects, 
            "grades": student.grades 
        }

    def get_student_by_name(self, student_name: str) -> str:
            return (student_name, self.roster[student_name]) if student_name in self.roster else "Student Not Found" 

    def update_student(self, student: Student):
        if student.name in self.roster:
            self.roster.get(student.name).update({
                "fav_subjects": student.fav_subjects, 
                "grades": student.grades 
            })

    def delete_student(self, student_name: str):
        self.roster.pop(student_name)

def main():
    student_repository = DictionaryStudentRepository()

    student_repository.add_student(Student("John", ["PE", "Math", "Geometry"], [90, 87, 99]))

    print(student_repository.get_student_by_name("John"))

    student_repository.update_student(Student("John", ["Biology", "Science", "IRS"], [78, 67, 79]))

    print(student_repository.get_student_by_name("John"))

    student_repository.delete_student("John")

    print(student_repository.get_student_by_name("John"))

if __name__ == "__main__": # if script is run directly, execute main()
    main()
