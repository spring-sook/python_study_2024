# 양의 정수 n을 입력 받아 n * n 크기의 행렬을 출력하는 프로그램 작성
# 이 때 행렬의 값은 1부터 시작하여 왼쪽에서 오른쪽으로, 위에서 아래 순서대로 채워 넣음.
'''
입력 : 3
1 2 3
4 5 6
7 8 9
'''
# 1. 입력 받은 값으로 실제 출력 범위를 정해야 함
# 2. 줄바꿈에 대한 처리 (나머지 연산자 사용)
# 3. 줄맞춤

# # 내 답 1
# num = int(input("양의 정수 입력 : "))
# length = len(str(num*num))
# for i in range(num*num):
#     print(' '*(length-len(str(i+1))), end="")
#     print(i+1, end=" ")
#     if i % num == (num - 1):
#         print()

# # 내 답 2
# num = int(input("양의 정수 입력 : "))
# rst = 0
# for i in range(num): # 0 1 2
#     for j in range(num): # 0 1 2
#         rst += 1
#         print(rst, end=" ")
#     print()

# # 강사님 답 *****************************
# n = int(input("정수 입력 : "))
# for i in range(1, n * n + 1):
#     print(f"{i:5}", end=" ")
#     # f-string  :<은 왼쪽정렬, :>는 오른쪽 정렬(default), :^는 가운데정렬
#     # :5는 공간을 5개 잡는거고 기본이 오른쪽이라 아무것도 안쓰면 오른쪽 정렬
#     if i % n == 0: print()
