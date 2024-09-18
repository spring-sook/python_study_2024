# 날짜와 시간 관련 함수
from datetime import datetime  # datetime 모듈에서 datetime 함수를 가져옴
# import datetime

# print(datetime.datetime.today())  # 이건 import datetime만 했을 때
print(datetime.today())
print(datetime.today().month)
print(datetime.today().date())
print(datetime.today().time())
print(datetime.today().hour)

import calendar
# print(calendar.calendar(2024))

# math 모듈 : 수학과 관련된 기능을 처리할 때 사용
import math

print(math.sin(1))
print(math.cos(1))
print(math.tan(1))
print(math.ceil(1.0000000001))  # 소수점 이하가 있으면 무조건 올림
print(math.floor(1.999999999))  # 소수점 이하가 있으면 무조건 내림