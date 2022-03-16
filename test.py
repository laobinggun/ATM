import sys

from AtmUtil import AtmUtil


def login():
    """登录方法：模拟实现用户登录过程."""
    card = input("请输入银行卡号：")
    atm = AtmUtil.find_atm_by_card(card)  # 调用AtmUtil类的类方法find_atm_by_card，查找输入卡号是否存在
    while atm not in AtmUtil.atm_list:  # 如果卡号不存在，需要用户重新输入卡号
        card = input("卡号有误，请重新输入卡号：\n")
        atm = AtmUtil.find_atm_by_card(card)
    for count in range(1, 4):  # 控制密码输错次数为3次
        password = input("请输入密码：")
        if password == atm.password:  # 判断输入的密码与输入卡号所对应的真实密码是否相同
            break
        else:
            print(f"密码错误{count}次！")
            if count == 3:
                print("密码连续错误三次，程序退出！")
                sys.exit()  # 退出程序
    atm_util = AtmUtil(atm)  # 使用上面登录成功的Atm对象atm作为参数，调用AtmUtil类的构造方法，创建AtmUtil对象
    welcome(atm_util)  # 使用AtmUtil对象atm_util，调用欢迎方法


def welcome(atm_util):
    """欢迎方法：打印欢迎信息，调用atm_util对象的功能选择方法."""
    print("登录成功,欢迎使用中国银行！\n")
    atm_util.user_choose()  # 调用对象atm_util的功能选择方法


AtmUtil.init_datas()  # 调用init_datas()方法，初始化列表atm_list
login()  # 调用登录方法
