# exceptions(예외 상황) : 프로그램 작성 후 실행 도중에 발생하는 여러가지 상황에 대한 것
# 예외 처리란? 예외 상황이 발생할 가능성이 높은 코드에서 try ~ exception을 통해 흐름을 변경하는 것
from multiprocessing.managers import Value

# while True:
#     try:
#         file_name = input("파일 이름 입력 : ")
#         score_file = open(file_name, "r", encoding='utf-8')
#         print(score_file.read())
#         score_file.close()
#         break
#     except FileNotFoundError:
#         print("파일이 없습니다. 파일 확인 후 다시 진행하세요.")

# try:
#     print("나눗셈 계산기")
#     num1 = int(input("첫 번째 숫자 입력 : "))
#     num2 = int(input("두 번째 숫자 입력 : "))
#     print(f"{num1} / {num2} = {(num1 / num2):.2f}")
# except ValueError:  # 잘못된 입력이 들어왔을 때
#     print("숫자만 입력 하세요.")
# except ZeroDivisionError:
#     print("나눗셈은 0으로 나눌 수 없습니다.")
# else:  # 예외가 발생하지 않았을 때 불려짐
#     print("정상적으로 처리 되었습니다.")
# finally:  # 예외 여부에 상관없이 호출
#     print("프로그램 종료.")

while True:
    try:
        print("나눗셈 계산기")
        num1 = int(input("첫 번째 숫자 입력 : "))
        num2 = int(input("두 번째 숫자 입력 : "))
        print(f"{num1} / {num2} = {(num1 / num2):.2f}")
        break
    except ValueError:  # 잘못된 입력이 들어왔을 때
        print("숫자만 입력 하세요.")
    except ZeroDivisionError:
        print("나눗셈은 0으로 나눌 수 없습니다.")
print("프로그램 종료")