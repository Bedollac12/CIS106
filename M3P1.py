Exam_1_Score = float(input("Enter your exam 1 score: "))
Exam_2_Score = float(input("Enter your exam 2 score: "))
Exam_1_weighted = Exam_1_Score * 0.60
Exam_2_weighted = Exam_2_Score * 0.40
Total_Score = Exam_1_weighted + Exam_2_weighted
print(f"Total Score: {Total_Score:.2f}")