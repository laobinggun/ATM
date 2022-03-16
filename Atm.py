

class Atm:
    """定义一个银行卡类Atm：用于描述银行卡对象的三个属性和四个功能.

    类的属性:
        card:银行卡号.
        password:密码.
        balance:余额.
    """

    def __init__(self, card, password, balance):
        """类Atm的构造方法：创建该类的对象时调用."""
        self.card = card
        self.password = password
        self.balance = balance

    def __repr__(self):
        """重写父类object的 __repr__()，返回当前对象所有属性值构成的字符串."""
        return self.card + " " + self.password + " " + str(self.balance) + "\n"

    def search_info(self):
        """查询方法：用于查询银行卡余额."""
        print(f"余额为：{self.balance}")

    def set_money(self, money):
        """存款方法：用于向银行卡中存入金额."""
        self.balance += money

    def get_money(self, money):
        """取款方法：用于从银行卡中取出金额."""
        self.balance -= money

    def trans_money(self, money, trans_atm):
        """转账方法：用于向其它银行卡进行转账."""
        self.balance -= money
        trans_atm.balance += money

