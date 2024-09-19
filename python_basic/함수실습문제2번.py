# 두번째 수 찾기
# 입력 : 1 2 3 4 5 6 7 8 3 4 5 6 7 8
# 찾을 수 : 3
# 해당 수의 위치를 반환 : 인덱스가 아님, 9번째
# 찾지 못하면 -1을 반환
'''
def second_find(ls, n):
    pass
# 정수값에 대한 리스트 입력 생성
# 찾을 수 입력 받기
# 결과 출력하기
'''

# 내 답
# def second_find(ls, n):
#     index = []
#     for i, e in enumerate(ls):
#         if n in e:
#             index.append(i)
#     return index
#
# nums = input("정수들을 입력해주세요 : ").split()
# fnum = input("찾을 수 입력 : ")
# indexes = second_find(nums, fnum)
# if len(indexes) >= 2:
#     print(int(indexes[1]) + 1)
# else:
#     print(-1)

# 강사님 답
# def second_find(l, n):
#     cnt = 0
#     for i in range(len(l)):
#         if l[i] == n:
#             if cnt > 0: return i + 1
#             else: cnt += 1
#     return -1
# # 정수값에 대한 리스트 입력 생성
# ls = list(map(int, input("입력 : ").split()))
# # 찾을 수 입력 받기
# find_num = int(input("찾을 수 : "))
# # 결과 출력하기
# print(f"결과 : {second_find(ls, find_num)}")