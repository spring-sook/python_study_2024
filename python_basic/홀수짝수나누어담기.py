# 무작위 수를 공백 기준으로 입력받아 홀수와 짝수로 리스트에 나누어 담아 출력하는 문제

# 내 답
# nums = list(map(int, input("정수를 입력해주세요 : ").split()))
# odd = []
# even = []
# for n in nums:
#     if n % 2 == 0:
#         even.append(n)
#     else:
#         odd.append(n)
# print(f"홀수 : {odd}, 짝수 : {even}")

# 강사님 답1
# number = list(map(int, input("입력 : ").split()))
# even = []
# odd = []
# for e in number:
#     if e % 2 == 0: even.append(e)
#     else: odd.append(e)
# print(f"홀수 : {odd}")
# print(f"짝수 : {even}")

# 강사님 답2
number = list(map(int, input("입력 : ").split()))
odd = list(filter(lambda x: x % 2 == 1, number))
even = list(filter(lambda x: x % 2 == 0, number))
print(f"홀수 : {odd}")
print(f"짝수 : {even}")