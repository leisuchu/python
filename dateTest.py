"""
日期相差天数、周数测试
"""
import datetime
from dateutil import rrule

"""
获取格式化的日期（指定）
"""
startDate = datetime.datetime.strptime("2020,03,04", "%Y,%m,%d")
endDate = datetime.datetime.strptime("2020,09,04", "%Y,%m,%d")
"""
获取当前日期时间
"""
now = datetime.datetime.now()
# 获取日期
nowDate = now.date()
# 获取时间
nowTime = now.time()

"""
日期增加（不支持年月）
"""
# 增加天数-加2天
now_date_add = nowDate + datetime.timedelta(2)

# 减少天数-减2天
now_date_sub = nowDate - datetime.timedelta(2)

# 计算相差周数
weeks = rrule.rrule(rrule.WEEKLY, dtstart=startDate, until=endDate)
print(weeks.count())
