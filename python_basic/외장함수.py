# 외장함수는 import 해서 사용하는 함수, 파이썬에서 기본적으로 제공하는 것
# 랜덤 함수 : 지정한 범위 내에서 임의의 숫자를 만들어내는 것
import random

# for i in range(10):
#     rand = random.randint(1, 10)  # 1 ~ 10 까지의 임의의 값을 생성
#     print(rand, end=" ")
# print()

################################ 실습~~  (근데 리스트 안배웠는데 실수로 실습문제로 내버렸네용. 그냥 같이 할게요~)
# 중복되지 않는 로또 번호 생성 : 1 ~ 45 사이의 임의의 수 6개
# 리스트를 사용, 리스트 내에 임의로 생성한 번호가 있으면 추가하면 안됨
# if rand not in list:
# 내 답
# nums = []
# while len(nums) < 6:
#     print(len(nums))
#     rand = random.randint(1, 45)
#     if rand not in nums:
#         nums.append(rand)
# print(sorted(nums))

# 강사님 답
# print("로또 번호 자동 생성 : ")
# lotto = []
# while True:
#     rand = random.randrange(1, 46)  # 1 ~ 45
#     if rand not in lotto:
#         lotto.append(rand)
#     if len(lotto) == 6: break
# print(lotto)

# print("로또 번호 자동 생성 : ")
# lotto = []
# while len(lotto) <= 6:
#     rand = random.randrange(1, 46)  # 1 ~ 45
#     if rand not in lotto:
#         lotto.append(rand)
# print(lotto)

lotto = set()
while len(lotto) <= 6:
    rand = random.randrange(1, 46)
    lotto.add(rand)
print(lotto)