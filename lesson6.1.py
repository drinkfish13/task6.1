import re
str_ = input()
def ekx(st):
    pattern = '[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ][АВЕКМНОРСТУХ]\d{2,3}$'
    if re.match(pattern, st):
        gov_number = re.findall('[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ][АВЕКМНОРСТУХ]', st)
        gov_region = re.findall('\d{2,3}$', st)
        return gov_number[0],gov_region[0]
    else:
        return 'Номер некорректный'
print(ekx(str_))


