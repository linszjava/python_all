# 基本数据类型
# 测量身高体重的bmi指数 小程序
# 体重(kg) / 身高(m)的平方

# height = 1.82
# weight = 54
height = float(input('input ur height(m): '))
weight = float(input('input ur weight(kg): '))
bmi = weight / (height * height)
print('ur height is %.2f m, weight is %.2f kg, bmi is %.2f' % (height, weight, bmi))
if bmi < 18.5:
    print('过轻')
elif 25 > bmi >= 18.5:
    print('正常')
else:
    print('过重')


