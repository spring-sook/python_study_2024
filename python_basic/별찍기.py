## 별찍기 1
'''
입력 : 5
*
**
***
****
*****
'''
# 2중 for문을 사용해서 풀어야 합니다.

# 내 답
# num = int(input("정수 입력 : "))
# for i in range(num):
#     print('*' * (i + 1))

# 강사님 답
n = int(input("입력 : "))
for i in range(n):  # 행의 개수
    for j in range(i+1):
        print("*", end="")
    print()

## 별찍기 2


## 별찍기 3