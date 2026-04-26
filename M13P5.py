students = {
    "Adams": [85, 90, 88],
    "Baker": [92, 88, 95],
    "Clark": [78, 82, 75],
    "Davis": [90, 85, 92],
    "Evans": [88, 91, 87],
    "Frank": [72, 68, 75],
    "Ghosh": [95, 98, 93],
    "Hills": [81, 79, 84],
    "Irwin": [77, 80, 76],
    "Jones": [89, 92, 86]
}

def display_students(student_dict):
    print(f"{'Name':<12}{'Grade1':>8}{'Grade2':>8}{'Grade3':>8}{'Average':>10}")
    print("-" * 46)

    total_g1 = 0
    total_g2 = 0
    total_g3 = 0
    count = 0

    for name in student_dict:
        grades = student_dict[name]
        avg = (grades[0] + grades[1] + grades[2]) / 3
        print(f"{name:<12}{grades[0]:>8}{grades[1]:>8}{grades[2]:>8}{avg:>10.1f}")
        total_g1 =  total_g1 + grades[0]
        total_g2  = total_g2 + grades[1]
        total_g3 = total_g3 + grades[2]
        count = count + 1

    print("-" * 46)
    avg_g1 = total_g1 / count
    avg_g2 = total_g2 / count
    avg_g3 = total_g3 / count
    print(f"{'Class Avg':<12}{avg_g1:>8.1f}{avg_g2:>8.1f} {avg_g3:>8.1f}")

display_students(students)