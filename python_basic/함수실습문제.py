# 입력 받은 수 미만의 소수의 합 구하기
# 소수 : 1과 자기 자신을 제외하고 나누어지지 않는 수
# 입력 : 12  (2 + 3 + 5 + 7 + 11) = 28

# 내가 풀다 만 거 >>>>>>> 아직 다 못함...
def prime_func(n):
    nums = [x for x in range(2, n)]  # [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    print(nums)
    for e in nums:
        for j in range(2, e):
            print(f"eeeeeeeee{e}")
            print(f"e : {e}  j : {j}")
            if e % j == 0:
                print(f"이놈 지운다 {e}")
                nums.remove(e)
                break
        print(nums)
    return nums

num = int(input("정수 입력 : "))
nums = prime_func(num)
print(">>>>>>>>>", nums)

# 강사님 답
# def prime_func(n):
#     is_prime = True
#     for i in range(2, n):  # 1과 자기자신을 제외
#         if n % i == 0: is_prime = False
#     if is_prime: return n
#     else: return 0
#
# num = int(input("정수 입력 : "))
# prime_sum = 0
# for i in range(2, num):
#     prime_sum += prime_func(i)
# print(prime_sum)