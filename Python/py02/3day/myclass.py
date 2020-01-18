# class Role:
#     def __init__(self,name,weapon):
#         self.name=name
#         self.weapon=weapon
#
# if __name__ == '__main__':
#     lb = Role('吕布','方天画戟')
#     print(lb.name,lb.weapon)
#
# # class Role:
# #     def __init__(self,name,weapon):
# #         self.name = name
# #         self.weapon = weapon
# #
# # if __name__ == '__main__':
# #     lb = Role('吕布','sd')
# #     print(lb.name,lb.weapon)


# if __name__ == '__main__':
#     lb=Role('吕布','方天画戟')
#     print(lb.name,lb.weapon)
#     lb.show_me()

class Role:
    def __init__(self,name,weapon):
        self.name=name
        self.weapon=weapon

    def show_me(self):
        print('我是%s,我的武器是%s' % (self.name,self.weapon))

    def say(self,words):
        print(words)


class Warrior(Role):
    def __init__(self,name,weapon,country):
        Role.__init__(self, name, weapon)
        #super(Warrior,self).__init__(name,weapon)
        self.country = country

    def attack(self,target):
        print('近身攻击:%s' % target)

class Mage(Role):
    def attack(self, target):
        print('远程攻击:%s' % target)

class Meditating(Role):
    def attack(self,target):
        print('精神攻击:%s'%target)


if __name__ == '__main__':
    gy=Warrior('关羽','青龙偃月刀','蜀')
    km=Mage('孔明','大宝剑')
    gy.show_me()
    km.show_me()
    gy.attack('吕布')
    km.attack('周瑜')
    hg=Meditating('黄盖','裸衣')
    hg.show_me()
    hg.attack('公瑾')





# if __name__ == '__main__':
#     lb=Role('吕布','方天画戟')
#     print(lb.name,lb.weapon)
#     lb.show_me()
#     lb.say('马中赤兔,人中吕布')
#
#     zf=Role('张飞','丈八蛇矛')
#     zf.show_me()

