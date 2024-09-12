# 주/야간 근무시간을 입력 받아 아르바이트 급여 계산하기
# 주간 근무 시급 : 9860원
# 야간 근무 시급 : 주간 시급 * 1.5
# [입력] 주간근무 [1] 야간근무 [2]를 입력하세요 :
# [입력] 근무 시간을 입력하세요 :
# [출력] print(f"{근무시간}시간 동안 근무한 {근무타입문자열} 급여는 {급여}원 입니다.")

# 내 답
# worktype_num = input("주간근무 [1] 야간근무 [2]를 입력하세요 : ")
# worktime = int(input("근무 시간을 입력하세요 : "))
# pay = 0
#
# if worktype_num == "1" :
#     worktype = "주간근무"
#     pay = 9860 * worktime
# else:
#     worktype = "야간근무"
#     pay = 9860 * 1.5 * worktime
#
# print(f"{worktime}시간 동안 근무한 {worktype} 급여는 {pay}원 입니다.")

# 강사님 답
work_type = int(input("주간근무 [1] 야간근무 [2]를 입력하세요 : "))
work_time = int(input("근무 시간을 입력하세요 : "))
HOUR_PAY = 9860

if work_type == 1:
    pay = work_time * HOUR_PAY
else:
    pay = work_time * HOUR_PAY * 1.5

work_type_str = work_type == 1 and "주간" or "야간"
# "주간" if work_type == 1 else "야간"
pay_str = f"{pay:,.0f}"
print(f"{work_time}시간 동안 근무한 {work_type_str} 급여는 {pay_str}원 입니다.")