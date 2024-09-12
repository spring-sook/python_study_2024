"""
2개의 문자열을 포인터 변수 s와 k에, 양의 정수를 정수형 변수 n에
각각 전달 받아 s 문자열의 뒤 부분의 n개 문자를 k문자열 앞에 끼워넣는 코드 작성
예) s : seoul
   k : korea
   n : 2
   result : ulkorea
"""
## 내 답
# s = input("문자열을 입력해주세요 : ")
# k = input("문자열을 입력해주세요 : ")
# n = input("양의 정수를 입력해주세요 : ")
# result = s[-int(n):] + k
# print(result)

## 강사님 답
s = input("s : ")
k = input("k : ")
n = int(input("n : "))
print(s[-n:] + k)
pos = len(s) - n
print(s[pos:] + k)