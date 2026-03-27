Last_Name= input("Enter your last name: ")
Midterm_score= float(input("Enter your midterm score: "))
Final_exam_score= float(input("Enter your final exam score: "))
Calculate_total_score= Midterm_score * 0.40 + Final_exam_score * 0.60
print(f"Last Name: {Last_Name}")
print(f"Total Exam Points: {Calculate_total_score:.2f}")