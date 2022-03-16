import sys

from Atm import Atm


class AtmUtil:
    """定义一个银行卡工具类AtmUtil：用于实现银行卡操作过程中的辅助功能.

    成员属性:
        atm:成员属性，代表成功登录的Atm对象.

    类属性：
        account_file:类属性，定义account.txt文件的路径
        atm_list:类属性，用于存储Atm对象

    """
    account_file = 'D:\\PycharmProjects\\test\\account.txt'  # 定义account.txt文件的路径
    atm_list = []  # 定义列表，用于存储Atm对象

    def __init__(self, atm):
        """类AtmUtil的构造方法：创建该类的对象时调用."""
        self.atm = atm

    @classmethod
    def find_atm_by_card(cls, card):
        """查找方法：根据输入卡号从atm_list列表中查找Atm对象并返回.并使用@classmethod声明为一个类方法：只绑定到类本身，实现对类属性atm_list的访问."""
        for atm in cls.atm_list:
            if card == atm.card:
                return atm
        return None  # 查找不到，返回空对象

    @classmethod
    def init_datas(cls):
        """初始化方法：读取account.txt中所有银行卡信息，转化为Atm对象，存储于列表atm_list中.并使用@classmethod声明为一个类方法：只绑定到类本身，实现对类属性atm_list的访问."""
        account_file_object = open(AtmUtil.account_file, "r")  # 以只读方式打开文件，返回文件对象
        account_list = account_file_object.readlines()  # 通过文件对象，调用方法，读取文件所有行，并返回一个列表
        for account in account_list:  # 循环读取account_list列表元素
            account_info_list = account.strip().split(' ')  # 去除account前后的空白符，并以空格切割account，封装为一个列表返回
            temp_card = account_info_list[0]  # 从列表中取出卡号
            temp_pass = account_info_list[1]  # 从列表中取出密码
            temp_balance = int(account_info_list[2])  # 从列表中取出余额，并转换为整数类型
            atm = Atm(temp_card, temp_pass, temp_balance)  # 调用Atm类的构造方法，创建一个Atm对象，并初始化该对象的卡号、密码、余额
            AtmUtil.atm_list.append(atm)  # 向列表中添加元素
        account_file_object.close()  # 关闭文件对象

    def user_choose(self):
        """功能选择方法：实现用户的功能选择."""
        choose = input("请选择功能：1 查询、2 存款、3 取款、4 转账、5 退出\n")
        if choose == '1':
            self.atm.search_info()
            self.is_continue()
        elif choose == '2':
            money = int(input("请输入存款金额："))
            self.atm.set_money(money)
            # self.atm.search_info()
            self.is_continue()
        elif choose == '3':
            money = int(input("请输入取款金额："))
            self.atm.get_money(money)
            # self.atm.search_info()
            self.is_continue()
        elif choose == '4':
            trans_card = input("请输入转账卡号：")
            trans_atm = self.find_atm_by_card(trans_card)
            while trans_atm not in self.atm_list:
                card = input("卡号有误，请重新输入卡号：\n")
                trans_atm = self.find_atm_by_card(card)
            trans_money = int(input("请输入转账金额：\n"))
            self.atm.trans_money(trans_money, trans_atm)
            # self.atm.search_info()
            self.is_continue()
        elif choose == '5':
            self.save_datas()  # 保存数据
            sys.exit()  # 退出程序
        else:
            print("输入错误，请重新选择！")
            self.user_choose()

    def is_continue(self):
        """继续方法：判断用户是否继续操作."""
        answer = input("继续操作吗？")
        if answer == 'y':
            self.user_choose()
        elif answer == 'n':
            self.save_datas()  # 保存数据
            sys.exit()  # 退出程序
        else:
            print("输入错误，请重新输入！")
            self.is_continue()

    @classmethod
    def save_datas(cls):
        """保存方法：将atm_list中的数据重新写入account.txt文件中.并使用@classmethod声明为一个类方法：只绑定到类本身，实现对类属性atm_list和account_file的访问."""
        atm_attr_values_list = []  # 定义一个列表，用于存放所有Atm对象的属性值字符串
        account_file_object = open(cls.account_file, "w")  # 以写的方式打开文件，返回文件对象
        for atm in cls.atm_list:  # 循环atm_list列表中的Atm对象
            atm_attr_values = repr(atm)  # 调用Atm对象的__repr__方法，返回该对象的所有属性值连接成的字符串
            atm_attr_values_list.append(atm_attr_values)  # 添加到列表中
        account_file_object.writelines(atm_attr_values_list)  # 写入文件中
