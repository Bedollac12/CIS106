students = {
    "Adams": 85.5,
    "Baker": 92.0,
    "Clark": 78.3,
    "Davis": 90.1,
    "Evans": 88.7,
    "Frank": 72.4,
    "Ghosh": 95.0,
    "Hills": 81.6,
    "Irwin": 77.9,
    "Jones": 89.2
}

def display_students(student_dict):
    print(f"{'Name':<15}{'Grade':>10}")
    print("-" * 25)
    total = 0
    count = 0
    for name in student_dict:
        grade = student_dict[name]
        print(f"{name:<15}{grade:>10.1f}")
        total = total + grade
        count = count + 1
    average = total / count
    print("-" * 25)
    print(f"{'Class Average':<15}{average:>10.1f}")

display_students(students)