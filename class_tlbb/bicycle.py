
"""
写一个Bicycle(自行车)类,有run(骑行)方法,
调用时显示骑行里程km(骑行里程为传入的数字):
再写一个电动自行车类EBicycle继承自Bicycle,
添加电池电量valume属性通过，参数传入, 同时有两个方法：
1. fill_charge(vol) 用来充电, vol 为电量
2. run(km) 方法用于骑行,每骑行10km消耗电量1度,
当电量消耗尽时调用Bicycle的run方法骑行，
通过传入的骑行里程数，显示骑行结果
"""

class Bicycle():
    def run(self,km):
        print(f"骑车好嗨啊,我用脚骑了{km}")
    # 继承：把父类名称放在类名后面的小括号中
class EBicycle(Bicycle):
    def __init__(self,valume):
        self.valume=valume
        #充电的方法
    def fill_charge(self,vol):
        self.valume=vol+self.valume

    def run(self,km):
        #最大骑行公里数
        max_km=self.valume*10
        if max_km>=km:
            print(f"我使用电瓶车骑行了{km}公里")
        else:
            print(f"我使用电瓶车骑行了{max_km}公里")
# 非继承调用
# bike = Bicycle()
# bike.run(km - max_km)
# 继承调用
            super().run(km - max_km)

ebike = EBicycle(10)
ebike.run(150)
# ebike.fill_charge(3)

# bike = Bicycle()
# bike.run(10)

