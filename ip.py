import wmi
import os
import socket
# print(os.name)
#
# #获取本机电脑名
# myname = socket.getfqdn(socket.gethostname(  ))
# # python = socket.getaddrinfo("www.python.org", 80, 0, 0, socket.SOL_TCP)
# # print(python)
# #获取本机ip
# myaddr = socket.gethostbyname(myname)
# # myinfo = socket.getfqdn(socket.getaddrinfo())
# print (myname)
# print (myaddr)
# # print (myinfo)


# Obtain network adaptors configurations
# nic_configs = wmi.WMI().Win32_NetworkAdapterConfiguration(IPEnabled=True)
#
# # First network adaptor
# nic = nic_configs[0]
# # print(nic)
# # IP address, subnetmask and gateway values should be unicode objects
# ip = '10.10.10.3'
# subnetmask = '255.255.255.0'
# gateway = '10.10.10.1'
#
# # Set IP address, subnetmask and default gateway
# # Note: EnableStatic() and SetGateways() methods require *lists* of values to be passed
# nic.EnableStatic(IPAddress=[ip],SubnetMask=[subnetmask])
# nic.SetGateways(DefaultIPGateway=[gateway])
# nic.EnableDHCP()


# print('正在修改IP,请稍候...')
# wmiService = wmi.WMI()
# colNicConfigs = wmiService.Win32_NetworkAdapterConfiguration(IPEnabled=True)  # 返回值是列表
# '''Win32_ NetworkAdapterConfiguration()方法
# NetworkAdapterConfiguration网络适配器的意思
# 函数调用: interfaceList = w.Win32_NetworkAdapterConfiguration(IPEnabled=1)
# 函数功能: 用于网络接口信息对象，并存以列表形式
# 传入参数: *argv
# IPEnabled: bool 类型，可传入1，默认为False，为 True 将显示 IP 信息
# 返回参数: interfaceList
# interfaceList: list 类型，list 中每个元素均为一个网络接口信息的 object
# 网络接口信息 object 通过 object.name 调用，所含信息包括（部分具体信息已删除）:'''
# print(colNicConfigs)
# for objNicConfig in colNicConfigs:
#     print(objNicConfig.Index)
#     print(objNicConfig.SettingID)
#     print(objNicConfig.Description.encode("cp936"))
#     print(objNicConfig.IPAddress)
#     print(objNicConfig.IPSubnet)
#     print(objNicConfig.DefaultIPGateway)
#     print(objNicConfig.DNSServerSearchOrder)
#     print('----------------------------------')
#
# if len(colNicConfigs) < 1:  # 如果没有显示，那么退出
#     print('没有找到可用的网络适配器')
#     exit()
#
# # objNicConfig = colNicConfigs[0]
# # print(objNicConfig)  # 打印看看什么类容，结果一堆东西。。。
# # print(dir(objNicConfig))
#
# print('----------------------------------')
# # for method_name in objNicConfig.methods:
# #     method = getattr(objNicConfig, method_name)  # 魔法函数，即使调用不成功，也不会报错
# #     print(method)
#
# arrIPAddresses = [input("请输入IP地址: \n")] # ip地址
# arrSubnetMasks = ['255.255.255.0']  # 子网掩码
# arrDefaultGateways = [input("请输入网关地址: \n")]  # 默认网关
# arrGatewayCostMetrics = [1]  # 网关成本度量
# arrDNSServers = arrDefaultGateways  # DNS
# intReboot = 0
# returnValue = objNicConfig.EnableStatic(IPAddress=arrIPAddresses, SubnetMask=arrSubnetMasks)  # 启动静态如果返回值是0，表明ip设置成功
#
# if returnValue[0] == 0:
#     print('设置IP成功')
# elif returnValue[0] == 1:
#     print('设置IP成功')
#     intReboot += 1
# else:
#     print('修改IP失败: IP设置发生错误')
#     exit()
#
# returnValue = objNicConfig.SetGateways(DefaultIPGateway=arrDefaultGateways,
#                                        GatewayCostMetric=arrGatewayCostMetrics)  # 设置网关
#
# if returnValue[0] == 0:
#     print('设置网关成功')
# elif returnValue[0] == 1:
#     print('设置网关成功')
#     intReboot += 1
# else:
#     print('修改网关失败: 网关设置发生错误')
#     exit()  # 这一段重复用可以封装一个函数或者类
#
# returnValue = objNicConfig.SetDNSServerSearchOrder(DNSServerSearchOrder=arrDNSServers)  # 设置DNS
#
# if returnValue[0] == 0:
#     print('设置DNS成功')
# elif returnValue[0] == 1:
#     print('设置DNS成功')
#     intReboot += 1
# else:
#     print('修改dns失败: 网关设置发生错误')
#     exit()  # 这一段重复用可以封装一个函数或者类
#
# if intReboot > 0:
#     print('需要重启计算机或刷新网络')
# # else:
# #     print('')
# #     print('修改后的配置为：')
# #     print(objNicConfig.IPAddress)
# #     print(objNicConfig.IPSubnet)
# #     print(objNicConfig.DNSServerSearchOrder)
# #     print('修改ip成功')
# #
#
# import  json
#
# nic_configs = wmi.WMI().Win32_NetworkAdapterConfiguration(IPEnabled=True)
# nic = nic_configs[0]
# with open('./ip.json','r',encoding='utf8') as ipFile:
#     ipOrder = json.load(ipFile)
#     for key  in ipOrder:
#         print(key)
#     ipSelect = input("请输入ip序号:")
#     ipConfig = ipOrder[ipSelect]
#     ipAddress = ipConfig['ipAddress']
#     subnetMask = ipConfig['subnetMask']
#     defaultIPGateway = ipConfig['defaultIPGateway']
#     dnsServerSearchOrder = ipConfig['dnsServerSearchOrder']
#     nic.EnableStatic(IPAddress = [ipAddress],SubnetMask = [subnetMask])
#     nic.SetGateways(DefaultIPGateway = [defaultIPGateway])
#     nic.SetDNSServerSearchOrder(DNSServerSearchOrder = [dnsServerSearchOrder])
    # print(ipConfig)
    # print(type(ipConfig['ipAddress']))
    # print(type(ipAddress))
    # print(ipAddress)
    # print(ipConfig['ipAddress'])
    # nic.EnableStatic(IPAddress = ipConfig['ipAddress'],SubnetMask = ipConfig['subnetMask'])
    # nic.SetGateways(DefaultIPGateway = ipConfig['defaultIPGateway'])
    # nic.SetDNSServerSearchOrder(DNSServerSearchOrder = ipConfig['dnsServerSearchOrder'])
# li = list(range(1,10))
# inp = str(input("input:"))
# judgeLi = inp in li
# print(li)
# print(type(li))
# print(judgeLi)
import os
# a=os.path.exists('222.py')
# print(a)
# os.path.isfile('ip.json')
# if not os.path.exists('1.txt'):

def ipConfig(name, config):
      # desktop_path = "C:\\Users\\Administrator\\Desktop\\"  # 新创建的txt文件的存放路径
      path = name + '.json'  # 也可以创建一个.doc的word文档
      file = open(path, 'w')
      file.write(config)  # msg也就是下面的Hello world!
      # file.close()


ipConfig('mytxtfile', '{"宿迁中医院": {"ipAddress": "192.168.0.105","subnetMask": "255.255.255.0","defaultIPGateway": "192.168.0.1","dnsServerSearchOrder": "192.168.0.1"},}')
