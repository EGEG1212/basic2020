brirthday = input('생일 (6, 7, 8자리 숫자> ')
if len(brirthday) == 6:
    b_year = int(brirthday[:2])
    if b_year <= 20:
        b_year += 2020
    else:
        b_year += 1900
    b_month = int(brirthday[2:4])
    b_day = int(brirthday[4:])
elif len(brirthday) == 7:
    b_year = int(brirthday[:2])
    if int(brirthday[-1]) > 2:
        b_year += 2000
    else:
        b_year += 1900
    b_month = int(brirthday[2:4])
    b_day = int(brirthday[4:6])
elif len(brirthday) == 8:
    b_year = int(brirthday[:4])
    b_month = int(brirthday[4:6])
    b_day = int(brirthday[6:8])
else:
    print('6~8자리의 숫자를 입력하세요')

print(b_year, b_month, b_day)