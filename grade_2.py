# 입력 함수
def input_students():
    students = []
    for i in range(5):
        student_id = input("학번을 입력하세요: ")
        name = input("이름을 입력하세요: ")
        english_score = int(input("영어 점수를 입력하세요: "))
        c_score = int(input("C 언어 점수를 입력하세요: "))
        python_score = int(input("파이썬 점수를 입력하세요: "))
        total_score = english_score + c_score + python_score
        average_score = total_score / 3
        grade = calculate_grade(average_score)
        students.append((student_id, name, english_score, c_score, python_score, total_score, average_score, grade))
    return students

# 총점 및 평균 계산 함수
def calculate_total_and_average(students):
    total = 0
    for student in students:
        total += student[5]
    average = total / len(students)
    return total, average

# 학점 계산 함수
def calculate_grade(average_score):
    if average_score >= 90:
        return 'A'
    elif 80 <= average_score < 90:
        return 'B'
    elif 70 <= average_score < 80:
        return 'C'
    elif 60 <= average_score < 70:
        return 'D'
    else:
        return 'F'

# 등수 계산 함수
def calculate_ranking(students):
    students.sort(key=lambda x: x[5], reverse=True)
    for i, student in enumerate(students):
        students[i] = student + (i + 1,)

# 출력 함수
def print_students(students):
    print("학번\t이름\t영어\tC언어\t파이썬\t총점\t평균\t학점\t등수")
    for student in students:
        print(f"{student[0]}\t{student[1]}\t{student[2]}\t{student[3]}\t{student[4]}\t{student[5]}\t{student[6]:.2f}\t{student[7]}\t{student[8]}")

# 80점 이상 학생 수 카운트 함수
def count_students_above_80(students):
    count = 0
    for student in students:
        if student[5] >= 80:
            count += 1
    return count

# 메인 함수
def main():
    students = input_students()
    calculate_ranking(students)
    total, average = calculate_total_and_average(students)
    print_students(students)
    above_80_count = count_students_above_80(students)
    print(f"\n80점 이상 학생 수: {above_80_count}")
    print(f"전체 학생 수: {len(students)}")
    print(f"전체 학생 총점: {total}, 전체 학생 평균: {average:.2f}")

if __name__ == "__main__":
    main()