class GradingSystem:
    def __init__(self):
        self.students = {}

    def add_grade(self, student_name, subject, grade):
        if student_name not in self.students:
            self.students[student_name] = {}

        if subject not in self.students[student_name]:
            self.students[student_name][subject] = []

        self.students[student_name][subject].append(grade)

    def calculate_average(self, student_name):
        if student_name in self.students:
            student_grades = self.students[student_name]
            subject_averages = {}

            for subject, grades in student_grades.items():
                subject_average = sum(grades) / len(grades)
                subject_averages[subject] = round(subject_average, 2)

            return subject_averages

    def calculate_overall_grade(self, student_name):
        averages = self.calculate_average(student_name)
        if averages:
            overall_average = sum(averages.values()) / len(averages)
            return round(overall_average, 2)

    def display_grades(self, student_name):
        averages = self.calculate_average(student_name)
        overall_grade = self.calculate_overall_grade(student_name)

        if averages:
            print(f"Grades for {student_name}:")
            for subject, average in averages.items():
                print(f"{subject}: {average}")
            print(f"Overall Grade: {overall_grade}")
        else:
            print(f"No grades found for {student_name}.")

# Example usage:
grading_system = GradingSystem()

grading_system.add_grade("Alice", "Math", 90)
grading_system.add_grade("Alice", "English", 85)
grading_system.add_grade("Bob", "Math", 78)
grading_system.add_grade("Bob", "English", 92)

grading_system.display_grades("Alice")
grading_system.display_grades("Bob")
grading_system.display_grades("Charlie")  # Nonexistent student
