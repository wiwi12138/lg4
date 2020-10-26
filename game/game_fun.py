# -*— coding:utf-8 —*—
# @time ：2020/10/26 10:18
# @Auttor :wiwi
# @File :game_fun.py
import random

   # 定义四个变量，调用时，需要传值
def fight(her_hp,my_hp,my_power,her_power):

    # 给四个变量初始值，并定义规则，只要不是我的血量大于对手，则算我输，反之我赢
    # my_hp = 1000
    # my_power = 200
    # her_hp = 1000
    # her_power = 199
    # 加while 循环，条件直接为 True，死循环，需要break 退出循环
    while True:
        my_hp = my_hp-her_power
        her_hp = her_hp-my_power
        # print(my_hp)
        # 判断规则，谁的血量先归0 谁输，并打印双方的血量
        if my_hp <= 0 and my_hp<=her_hp:
            print("我输了")
            print("我的血量",my_hp)
            print("敌人的血量",her_hp)
            break

        elif her_hp <=0 :
            print("我赢了")
            print("我的血量",my_hp)
            print("敌人的血量",her_hp)

            break
    # print("我的初始血量为",my_hp,";我的攻击力为",my_power,"；敌人的初始血量为",her_hp,"敌人的攻击力为",her_power)
#当.py文件被直接运行时，if __name__ == '__main__'之下的代码块将被运行(不需要调用也会运行)；当.py文件以模块形式被导入时，if __name__ == '__main__'之下的代码块不被运行
if __name__=="__main__":
    # 利用列表推导式生成hp数列
    hp=[x for x in range(990,1100)]
    # print(my_hp)
    #choice(seq): 从seq序列中（可以是列表，元组，字符串）随机取一个元素返回
    her_hp=random.choice(hp)
    my_hp=random.choice(hp)
    print(her_hp)
    print(my_hp)
    my_power=random.randint(190,220)
    her_power=random.randint(190,220)
    print("我的初始血量为",my_hp,";我的攻击力为",my_power,"；敌人的初始血量为",her_hp,"敌人的攻击力为",her_power)

 # 3 print( random.randint(1,10) )        # 产生 1 到 10 的一个整数型随机数
 # 4 print( random.random() )             # 产生 0 到 1 之间的随机浮点数
 # 5 print( random.uniform(1.1,5.4) )     # 产生  1.1 到 5.4 之间的随机浮点数，区间可以不是整数
 # 6 print( random.choice('tomorrow') )   # 从序列中随机选取一个元素
 # 7 print( random.randrange(1,100,2) )   # 生成从1到100的间隔为2的随机整数

 # 传入四个参数值
fight(her_hp,my_hp,my_power,her_power)