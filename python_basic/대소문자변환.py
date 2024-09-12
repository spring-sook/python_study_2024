# 영어 소문자와 대문자로 이루어진 단어를 입력받은 뒤,
# 대문자는 소문자로, 소문자는 대문자로 바꾸어 출력하는 프로그램을 작성하시오.

## 내 답
# input_text = input("영어 문자열을 입력하세요 : ")
# result = ""
# for i in range(len(input_text)):
#     if input_text[i].islower():
#         result += input_text[i].upper()
#     elif input_text[i].isupper():
#         result += input_text[i].lower()
#     else:
#         result += input_text[i]
# print(result)
tt
## 강사님 답
rst = ""
for e in input("입력 : "):
    if e.islower():
        rst += e.upper()
    else:
        rst += e.lower()
print(rst)