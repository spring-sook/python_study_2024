# # 제어문이란? 조건문과 반복문을 의미
# num = int(input("정수값 입력 : "))
#
# if num > 100:
#     print(f"{num}은 100보다 커요.")
# elif num < 100:
#     print(f"{num}은 100보다 작아요.")
# else:
#     print(f"{num}은 100과 같아요.")

######################### 실습문제~~
# 성적을 입력받아서 0 ~ 100 사이가 아니면 성적을 잘못 입력하였다고 표기
# 성적이 0 ~ 100이고
# 90점 이상이면 "A"
# 80점 이상이면 "B"
# 70점 이상이면 "C"
# 60점 이상이면 "D"
# 나머지는 "F"

# # 내 답
# score = int(input("성적을 입력해주세요. : "))
# #rst = ""
# if (score >= 0) and (score <= 100):
#     if score >= 90:
#         rst = "A"
#     elif score >= 80:
#         rst = "B"
#     elif score >= 70:
#         rst = "C"
#     elif score >= 60:
#         rst = "D"
#     else:
#         rst = "F"
#     print(f"성적 : {rst}")
# else:
#     print("성적을 잘못 입력하셨습니다.")

# 강사님 답
# score = int(input("성적 입력 : "))
# if 0 <= score <= 100:
#     if score >= 90 : print("A")
#     elif score >= 80 : print("B")
#     elif score >= 70 : print("C")
#     elif score >= 60 : print("D")
#     else: print("F")
# else:
#     print("성적을 잘못 입력하셨습니다.")

# if score < 0 or score > 100:
#     print("성적을 잘못 입력하셨습니다.")
#     exit(1)   ## 이런것도 있다고 그냥 이 방법도 써놈
# if score >= 90 : print("A")
# elif score >= 80 : print("B")
# elif score >= 70 : print("C")
# elif score >= 60 : print("D")
# else: print("F")

######################### 실습문제~~
# 세자리 정수를 입력받아 100의 자리, 10의 자리, 1의 자리로 나누어 담고
# 이 중 가장 큰 수 출력
# 몫과 나머지로 변수 할당
# if ~ else문으로 값 비교

# 내 답
# num = int(input("세자리 정수를 입력하세요. : "))
# a = num // 100
# b = (num % 100) // 10
# c = num % 10
# if a > b:
#     if a > c: print(a, "a임")
#     else: print(c, "c임")
# else:
#     if b > c: print(b, "b임")
#     else: print(c, "c임")

# 강사님 답
# num = int(input("정수 입력 : "))
# a = num // 100
# b = (num % 100) // 10
# c = num % 10
# if a > b:
#     if a > c: print(a)
#     else: print(c)
# else:
#     if b > c: print(b)
#     else: print(c)

while True:
    score = int(input("성적 입력 : "))
    if 0 <= score <= 100:
        if score >= 90 : print("A")
        elif score >= 80 : print("B")
        elif score >= 70 : print("C")
        elif score >= 60 : print("D")
        else: print("F")
        break

    print("성적을 잘못 입력하셨습니다.")

