def main():
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    if query_name in student_marks:
        average_score = sum(student_marks[query_name]) / len(student_marks[query_name])
        print(f"{average_score:.2f}")
    else:
        print("Student not found")

if __name__ == "__main__":
    main()