def bmi_custom(h1, w1):
    bmi =  w1 / (h1 * h1)
    print('bmi is '+ str(bmi))
    if bmi < 18.5:
        print('过轻')
    elif 25 > bmi >= 18.5:
        print('正常')
    else:
        print('过重')