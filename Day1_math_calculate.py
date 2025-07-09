import math
import random
import time

def generate_random_number():
    """生成0-100之间的随机整数"""
    return random.randint(1, 10)

def signal():
    a=['+', '-', '*', '/']
    # 生成1-4之间的随机整数，返回对应的符号
    return a[random.randint(0, 3)]

start_time=time.time()
end_time=time.time()
num=0
correct=0
result=[]
pre=input('欢迎来到数学计算游戏,你准备好了吗?按Y开始\n')
while pre=='Y' and end_time-start_time<10:#设置时间
    a=generate_random_number()
    b=generate_random_number()
    signal_value = signal()
    #获取随机算式，a，b，符号
    if signal_value == '+':
        re = a + b
    elif signal_value == '-':
        re = a - b
    elif signal_value == '*':
        re = a * b
    elif signal_value == '/':
        if b != 0:
            re = a / b
        else:
            while b==0:
                b=generate_random_number()  # 如果除数为0，重新生成一个除数
            re = a / b
    print(f'{a}{signal_value}{b}=?\n')
    re=round(re,2)#取小数点后2位
    result=round(eval(input()),2)
    if result == re:
        print('正确')
        correct += 1
    else:
        print(f'错误，正确答案是{re}')
    num=num+1
    end_time=time.time()
print(f'时间到！\n你一共答了{num}道题')
print(f'你答对了{correct}道题')
print(f'你的正确率是{correct/num*100:.2f}%')
