########## 저항 실습 예제 (알고리즘 3단계 중급)
# color1 = int(input("[0]black [1]brown [2]red [3]orange "
#                    "[4]yellow [5]green [6]blue [7]violet [8]grey [9]white\n"
#                    "첫번째 색 선택 : "))
# color2 = int(input("[0]black [1]brown [2]red [3]orange "
#                    "[4]yellow [5]green [6]blue [7]violet [8]grey [9]white\n"
#                    "두번째 색 선택 : "))
# color3 = int(input("[0]black [1]brown [2]red [3]orange "
#                    "[4]yellow [5]green [6]blue [7]violet [8]grey [9]white\n"
#                    "세번째 색 선택 : "))
#
# print((color1*10 + color2) * (10**color3))

## 내 답
# colors = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
# sel = []
# while True:
#     try:
#         if len(sel) < 3:
#             select = input(f"black, brown, red, orange, yellow, green,"
#                            f" blue, violet, grey, white\n색 입력 : ")
#             sel.append(colors.index(select))
#         else:
#             break
#     except:
#         print("색상을 다시 입력해 주세요.")
#
# print((sel[0]*10 + sel[1]) * (10**sel[2]))

## 강사님 답
color = "black", "brown", "red", "orange", "yellow",\
        "green", "blue", "violet", "grey", "white"
# 튜플로 받을땐 그냥 입력하면 되지요~
f_name = color.index(input())  # 해당 문자열의 인덱스 반환
s_name = color.index(input())
t_name = color.index(input())
print(int(str(f_name) + str(s_name)) * (10 ** t_name))