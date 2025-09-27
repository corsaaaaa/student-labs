

math_scores = [80, 90, 75, 95, 70, 85, 92, 88, 79, 83]
russian_scores = [85, 75, 90, 92, 78, 85, 95, 87, 80, 86]
informatics_scores = [90, 85, 92, 88, 78, 80, 87, 91, 82, 89]
names = ["Иванов", "Петров", "Сидоров", "Кузнецов", "Смирнов", "Козлов", "Морозов", "Васильев", "Федоров", "Николаев"]

total_scores = [math_scores[i] + russian_scores[i] + informatics_scores[i] for i in range(len(names))]

students = [(i, names[i], total_scores[i]) for i in range(len(names))]

students_sorted = sorted(students, key=lambda x: x[2], reverse=True)

for i in range(10):
    print(f"{students_sorted[i][0]}: {students_sorted[i][1]}")

