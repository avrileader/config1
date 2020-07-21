# #coding=utf-8
#
# firstNetcard = input("是否为所列出的第一个网卡(y or n): ")
# if firstNetcard == "n":
#     nicNumber = str(input("请选择网卡编号: "))   # 因为第一个接口从0开始计数
#     # if int(nicNumber) in range(0, 3):
#     #     print("在")
#     # else:
#     #     print("不在")
#     # a = ","
#     # print(a.join(map(range(0,100))))
#     judgeRange = nicNumber in range(0,3)
#     print(judgeRange)
#     while judgeRange == False:
#         print("没有输入任何内容")
#         nicNumber = str(input("没有输入任何内容！请选择网卡编号: "))
#         if  nicNumber is not None:
#             judgeRange = int(nicNumber) in range(0, 3)
#             print(type(nicNumber))
#
#         if  judgeRange == True:
#             break
# #
# #
# #
# #     print(nicNumber)
# # else:
# #     nicNumber = 0
# # print(int(nicNumber)-1)
# #
# # nicNumber = 1
# # if nicNumber in range(3):
# #     print("在")
# # else:
# #     print("不在")
# # b = range(0,3)
# # a = str(nicNumber) in str(b)
# # print(a)
# # print(b)
# # b = range(1,100)
# # a = str.find(b)
# # print(a)
# # a = []
# #
# # for i in range(1,100):
# #     a = i
# #     print(a)
# # li = []
# #
# # a = 1
# # while True:
# #     username = input("请输入要添加的员工姓名：")
# #     if username.strip().upper() == 'Q':
# #         break
# #     li.append(username)
# #     print(li)
# #     for a in li:
# #         print("是的")
# # print(li)
# #
# # a = input("输入数字1到100:")
# #
# while int(a) >1 and int(a)<3:
#
#     print(a)
#     break
# print(a)
# else:

    # print("重新输入")
#

#
# lista=[1,'5','s','cf']
#
# print(lista)
# if 1 in lista:
#     print('1 在列表lista中')
# if '1' in lista:
#     print('"11" 在列表lista中')
# if 'cf' in lista:
#     print('cf 在列表lista中')
# if 'ss' in lista:
#     print('ss 在列表lista中')
#
# # a = input("数字：")
# # list = []
# # for c in range(0,3):
# #     list.append(c)
# list = [str(i) for i in range(0,3)]
# print(list)
# # ss = [str(i) for i in list]
# # print(ss)
# a = input("数字：")
# judge = a in list
# print(judge)
# while judge == False:
#     print(judge)
#     a = input("数字：")
#     judge = a in list
#     if judge == True:
#         break
#
# print(type(a))
# print(type(list))
# if a is not None:
#     while int(a) in b:
#         print(a)
#         break
# list = [str(i) for i in input("y or n :")]
# list = ['y','n','Y','N']
# yn = input("y or n :")
# print(type(yn))
# judgeInput = yn in list
# judgeNone =  is not None
# print(judgeInput)
# print(judgeNone)

# print(judge)
# a=input("2+2=？") or "4"
# print(a)
list = ['y','n','Y','N']
judgeInput = input("y or n:")
judgeNone = str.isalpha(judgeInput)
print(judgeNone)
while judgeNone == False:
    judgeLetter = judgeInput in list
    while judgeLetter == False:
        judgeInput = input("reback y or n:")
        judgeLetter = judgeInput in list
        if judgeLetter == True:
            print(judgeLetter)
            break
    if judgeLetter == True:
        break

# print(judgeNone)



