import wmi
print('正在修改IP,请稍候...')
wmiService = wmi.WMI()
colNicConfigs = wmiService.Win32_NetworkAdapterConfiguration(IPEnabled=True)  # 返回值是列表
'''Win32_ NetworkAdapterConfiguration()方法
NetworkAdapterConfiguration网络适配器的意思
函数调用: interfaceList = w.Win32_NetworkAdapterConfiguration(IPEnabled=1)
函数功能: 用于网络接口信息对象，并存以列表形式
传入参数: *argv
IPEnabled: bool 类型，可传入1，默认为False，为 True 将显示 IP 信息
返回参数: interfaceList
interfaceList: list 类型，list 中每个元素均为一个网络接口信息的 object
网络接口信息 object 通过 object.name 调用，所含信息包括（部分具体信息已删除）:'''
print(colNicConfigs)
for objNicConfig in colNicConfigs:
    print(objNicConfig.Index)
    print(objNicConfig.SettingID)
    print(objNicConfig.Description.encode("cp936"))
    print(objNicConfig.IPAddress)
    print(objNicConfig.IPSubnet)
    print(objNicConfig.DefaultIPGateway)
    print(objNicConfig.DNSServerSearchOrder)
    print('----------------------------------')

if len(colNicConfigs) < 1:  # 如果没有显示，那么退出
    print('没有找到可用的网络适配器')
    exit()

objNicConfig = colNicConfigs[0]
print(objNicConfig)  # 打印看看什么类容，结果一堆东西。。。
# print(dir(objNicConfig))

print('----------------------------------')
# for method_name in objNicConfig.methods:
#     method = getattr(objNicConfig, method_name)  # 魔法函数，即使调用不成功，也不会报错
#     print(method)

arrIPAddresses = [input("请输入IP地址: \n")] # ip地址
arrSubnetMasks = ['255.255.255.0']  # 子网掩码
arrDefaultGateways = [input("请输入网关地址: \n")]  # 默认网关
arrGatewayCostMetrics = [1]  # 网关成本度量
arrDNSServers = arrDefaultGateways  # DNS
intReboot = 0
returnValue = objNicConfig.EnableStatic(IPAddress=arrIPAddresses, SubnetMask=arrSubnetMasks)  # 启动静态如果返回值是0，表明ip设置成功

if returnValue[0] == 0:
    print('设置IP成功')
elif returnValue[0] == 1:
    print('设置IP成功')
    intReboot += 1
else:
    print('修改IP失败: IP设置发生错误')
    exit()

returnValue = objNicConfig.SetGateways(DefaultIPGateway=arrDefaultGateways,
                                       GatewayCostMetric=arrGatewayCostMetrics)  # 设置网关

if returnValue[0] == 0:
    print('设置网关成功')
elif returnValue[0] == 1:
    print('设置网关成功')
    intReboot += 1
else:
    print('修改网关失败: 网关设置发生错误')
    exit()  # 这一段重复用可以封装一个函数或者类

returnValue = objNicConfig.SetDNSServerSearchOrder(DNSServerSearchOrder=arrDNSServers)  # 设置DNS

if returnValue[0] == 0:
    print('设置DNS成功')
elif returnValue[0] == 1:
    print('设置DNS成功')
    intReboot += 1
else:
    print('修改dns失败: 网关设置发生错误')
    exit()  # 这一段重复用可以封装一个函数或者类

if intReboot > 0:
    print('需要重启计算机或刷新网络')
# else:
#     print('')
#     print('修改后的配置为：')
#     print(objNicConfig.IPAddress)
#     print(objNicConfig.IPSubnet)
#     print(objNicConfig.DNSServerSearchOrder)
#     print('修改ip成功')
#

