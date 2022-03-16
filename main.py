import sys


def welcome(login_user_index):
    print('欢迎使用中国银行\n')
    user_choose(login_user_index)  # 调用用户选择方法


def login():
    card = input("请输入卡号：")
    login_user_index = find_user_by_card(card)
    while login_user_index == "not found":  # 如果卡号不存在
        card = input("卡号有误，请重新输入卡号：\n")
        login_user_index = find_user_by_card(card)
    for count in range(1, 4):  # 控制密码输错次数为3次
        password = input("请输入密码：")
        if password == users_infolist_list[login_user_index][1]:  # 判断输入的密码与输入卡号所对应的真实密码是否相同
            break
        else:
            print(f"密码错误{count}次！")
            if count == 3:
                print("密码连续错误三次，程序退出！")
                users_file_object.close()  # 关闭文件对象
                sys.exit()  # 退出程序
    welcome(login_user_index)  # 调用欢迎方法，传递当前登录用户在用户列表中的索引值


def search_info(login_user_index):
    print(f"余额为：{users_infolist_list[login_user_index][2]}")


def set_money(login_user_index, money):
    users_infolist_list[login_user_index][2] = str(int(users_infolist_list[login_user_index][2]) + money)


def get_money(login_user_index, money):
    users_infolist_list[login_user_index][2] = str(int(users_infolist_list[login_user_index][2]) - money)


def trans_money(login_user_index, trans_user_index, money):
    users_infolist_list[login_user_index][2] = str(int(users_infolist_list[login_user_index][2]) - money)
    users_infolist_list[trans_user_index][2] = str(int(users_infolist_list[trans_user_index][2]) + money)


def is_continue(login_user_index):
    answer = input("继续操作吗？")
    if answer == 'y':
        user_choose(login_user_index)
    elif answer == 'n':
        save_datas() # 退出前保存数据
        user_exit() # 退出程序
    else:
        print("输入错误，请重新输入！")
        is_continue(login_user_index)


def find_user_by_card(card):
    for user_infolist in users_infolist_list:
        if card == user_infolist[0]:
            return users_infolist_list.index(user_infolist)
    return "not found"


def user_choose(login_user_index):
    choose = input("请选择功能：1 查询、2 存款、3 取款、4 转账、5 退出\n")
    if choose == '1':
        search_info(login_user_index)
        is_continue(login_user_index)
    elif choose == '2':
        money = int(input("请输入存款金额："))
        set_money(login_user_index, money)
        search_info(login_user_index)
        is_continue(login_user_index)
    elif choose == '3':
        money = int(input("请输入取款金额："))
        get_money(login_user_index, money)
        search_info(login_user_index)
        is_continue(login_user_index)
    elif choose == '4':
        trans_card = input("请输入转账卡号：")
        trans_user_index = find_user_by_card(trans_card)
        while trans_user_index == "not found":  # 如果卡号不存在
            trans_card = input("卡号有误，请重新输入卡号：\n")
            trans_user_index = find_user_by_card(trans_card)
        money = int(input("请输入转账金额：\n"))
        trans_money(login_user_index, trans_user_index, money)
        search_info(login_user_index)
        is_continue(login_user_index)
    elif choose == '5':
        save_datas()  # 退出前保存数据
        sys.exit() # 退出程序
    else:
        print("输入错误，请重新选择！")
        user_choose(login_user_index)


def save_datas():
    users_file_object.seek(0)  # 回到文件开头，写入数据
    for user_infolist in users_infolist_list:
        for user_info in user_infolist:
            users_file_object.write(user_info)
            users_file_object.write(' ')
        users_file_object.write('\n')


def user_exit():
    users_file_object.close() # 退出前关闭文件对象
    sys.exit()


if __name__ == '__main__':
    users_file = 'D:\\PycharmProjects\\test\\user.txt'
    users_file_object = open(users_file, 'r+')
    users_info_list = users_file_object.readlines()
    users_infolist_list = [user_info.strip().split(' ') for user_info in users_info_list]
    print(users_infolist_list)  # 打印从文件中读取的用户信息生成的列表
    login()
