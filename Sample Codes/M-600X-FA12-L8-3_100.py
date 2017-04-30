def inToStr(i):
    digits = '0987654321'
    if i == 0:
        return '0'
    result = ''
    while i>0:
        result = digits[i%10] + result
        i = i/10
    return result
    