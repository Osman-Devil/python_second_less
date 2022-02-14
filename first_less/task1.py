number = int(input("duration = "))

day = number // 86400
number = number - (day*86400)

hour = number // 3600
number = number - hour * 3600

minut = number // 60
number = number - minut * 60

sec = number

if day == 0 and hour and minut == 0:
    print(f"В чиcле содержится: {sec} сек")
elif day == 0 and hour == 0:
    print(f"В чиcле содержится: {minut} мин : {sec} сек")
elif day == 0:
    print(f"В чиcле содержится: {hour} час : {minut} мин : {sec} сек")
else:
    print(f"В чиcле содержится: {day} дн :{hour} час : {minut} мин : {sec} сек")
