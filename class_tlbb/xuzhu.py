from class_tlbb.class_tstl import TongLao
import random
class XuZhu(TongLao):

    def __init__(self,t_hp,t_power):
        self.t_hp=t_hp
        self.t_power=t_power
    def read(self):

        print("虚竹：罪过罪过")

if __name__ == "__main__":
    # tonglao = class_tstl.TongLao(1200, 100)
    a=random.randint(1500,2000)
    b=random.randint(100,200)
    xuzhu=XuZhu(a,b)   # 实例化传参
    print(f"我童姥的HP是{a}，攻击力是{b}")
    xuzhu.see_people("丁春秋")
    # xuzhu.see_people("李秋水")
    xuzhu.fight_zms()
    xuzhu.read()  # 调用read 函数


