# -*— coding:utf-8 —*—
# @time ：2020/10/2610:20
# @Auttor :wiwi
# @File :game_2.py

"""
一个回合制游戏，每个角色都有hp 和power，hp代表血量，power代表攻击力，
hp的初始值为1000，power的初始值为200。
定义一个fight方法：
my_final_hp = my_hp - enemy_power
enemy_final_hp = enemy_hp - my_power
两个hp进行对比，血量剩余多的人获胜
"""

def fight():
    # 给四个变量初始值，并定义规则，只要不是我的血量大于对手，则算我输，反之我赢
    my_hp = 1000
    my_power = 200
    her_hp = 1000
    her_power = 199
    # 加while 循环，条件直接为 True，死循环，需要break 退出循环
    while True:
        my_hp = my_hp-her_power
        her_hp = her_hp-my_power
        # print(my_hp)
        # 判断规则，谁的血量先归0 谁输，并打印双方的血量
        if my_hp <= 0:
            print("我输了")
            print("我的血量",my_hp)
            print("敌人的血量",her_hp)
            break

        elif her_hp <=0:
            print("我赢了")
            print("我的血量",my_hp)
            print("敌人的血量",her_hp)
            break



    # print("我赢了") if my_hp>her_hp   else print("我输了")


fight()