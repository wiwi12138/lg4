# -*— coding:utf-8 —*—
# @time ：2020/10/2618:37
# @Auttor :wiwi
# @File :class_tstl.py

class TongLao():
    def __init__(self,t_hp,t_power):
        self.t_hp=t_hp
        self.t_power=t_power
    def see_people(self,name):
        if name== 'WYZ':
            print("师弟！！！！")
        elif name=='李秋水':
            print("师弟是我的！")
        elif name== '丁春秋':
            print("叛徒！我杀了你")
    def fight_zms(self):
        her_hp=2000
        her_power=200
        her_hp=her_hp-self.t_power*10
        t_hp=self.t_hp/2-her_power
        if t_hp>her_hp:
            print("我天山童姥赢了，哈哈。。")
        else:
            print("敌人太强了，我输了")


if __name__ == "__main__":
    tonglao=TongLao(2100,100)
    tonglao.see_people('WYZ')
    tonglao.fight_zms()
