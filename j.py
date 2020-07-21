import os
import wmi
import json
def printDecollator():
    print("-" * 50)
# def ipConfig():
#     path = 'ipConfig.json'
#     file = open(path, 'w',encoding='utf8')
#     file.write('宿迁中医')
print("正在获取网卡信息...")
changeCount = 1
while True:
    nicConfig = wmi.WMI().Win32_NetworkAdapterConfiguration(IPEnabled=True)
    '''Win32_ NetworkAdapterConfiguration()方法
    NetworkAdapterConfiguration网络适配器的意思
    函数调用: interfaceList = w.Win32_NetworkAdapterConfiguration(IPEnabled=1)
    函数功能: 用于网络接口信息对象，并存以列表形式
    传入参数: *argv
    IPEnabled: bool 类型，可传入1，默认为False，为 True 将显示 IP 信息
    返回参数: interfaceList
    interfaceList: list 类型，list 中每个元素均为一个网络接口信息的 object
    网络接口信息 object 通过 object.name 调用，所含信息包括（部分具体信息已删除）:'''
    nicWmi = wmi.WMI()
    nicData = {}
    nicCount = 0
    for nic in nicConfig:
        if nic.MACAddress is not None:
            nicCount+=1
            item_data = {}
            item_data['网卡型号'] = nic.Description
            item_data['物理地址'] = nic.MACAddress
            item_data['DHCP状态'] = nic.DHCPEnabled
            if nic.IPAddress is not None:
                item_data['IP 地址'] = nic.IPAddress[0]
                item_data['子网掩码'] = nic.IPSubnet[0]
                item_data['默认网关'] = nic.DefaultIPGateway[0]
            else:
                item_data['IP 地址'] = "无IP地址"
                item_data['子网掩码'] = "无子网掩码"
            if  nic.DNSServerSearchOrder is not None:
                item_data['DNS服务器'] = nic.DNSServerSearchOrder[0]
            else:
                item_data['DNS服务器'] = "无DNS服务器"
            nicData["网卡[{}]".format(nicCount)] = item_data
    # print(nicData)
    print(json.dumps(nicData,indent=1,ensure_ascii=False)) #ensure_ascii=False，json显示中文
    intNicList = [int(serialNumber) for serialNumber in range(1,nicCount+1)]
    strNicList = [str(serialNumber) for serialNumber in range(1,nicCount+1)]
    nicSelect = input("请输入网卡编号{}，默认为网卡[1]: ".format(intNicList)) or "1" #因为第一个接口从0开始计数
    judgeNicSelect = nicSelect in strNicList
    while judgeNicSelect == False:
        printDecollator()
        nicSelect = input("无效的数据！请重新输入请输入网卡编号{}，默认为网卡[1]: ".format(intNicList)) or "1"
        judgeNicSelect = nicSelect in strNicList
        if judgeNicSelect == True:
            break
    printDecollator()
    changeNic = nicConfig[int(nicSelect)-1]
    DHCPSelect = input("请择是否需要动态获取IP地址(Y or N)，默认为[Y]: ") or "y"
    ynList = ['y', 'n', 'Y', 'N']
    judgeDHCPSelect = DHCPSelect in ynList
    while judgeDHCPSelect == False:
        DHCPSelect = input("无效的数据！请选择是否需要动态获取IP地址(Y or N)，默认为[Y]:  ") or "y"
        printDecollator()
        judgeDHCPSelect = DHCPSelect in ynList
        if  judgeDHCPSelect == True:
            break
    printDecollator()
    if str.upper(DHCPSelect) == "N":
        # judgeFileExists = os.path.exists('ipconfig.json')
        # if judgeFileExists == False:
        #     ipConfig()
        # else:
        #     pass
        with open('ipconfig.json', 'r', encoding='utf-8') as ipFile:
            configOrder = json.load(ipFile) #读取文件中IP地址顺序，字典方式
            configIndex = list(configOrder.keys()) #将字典的keys转换为列表
            configCount = 0 #列表项目计数
            for config in configIndex:
                configCount+=1
            print(json.dumps(configOrder, indent=1, ensure_ascii=False))  # 打印文件内容
            for index,value in enumerate(configIndex,1): #获取列表索引
                printDecollator()
                print('选择序号[{}]为---------------------------------->[{}]'.format(index,value))
            printDecollator()
            strConfigList = [str(serialNumber) for serialNumber in range(1,configCount)] #将range里的数字转换为字符串存于列表
            indexSelect = input("请输入序号，默认为[1]:") or '1'  # 选择IP地址的索引
            printDecollator()
            judgeIndexSelect = indexSelect in strConfigList
            while judgeIndexSelect == False:
                indexSelect = input("无效的数据！请重新输入序号，默认为[1]:") or '1'  # 选择IP地址的索引
                printDecollator()
                judgeIndexSelect = indexSelect in strConfigList
                if judgeIndexSelect == True:
                    break
            configOrderSelect = configIndex[int(indexSelect)]  # 将索引对应的值存起来
            Config = configOrder[configOrderSelect]  # 调用字典中的索引对应的内容
            ipAddress = Config['ipAddress']
            subnetMask = Config['subnetMask']
            defaultIPGateway = Config['defaultIPGateway']
            dnsServerSearchOrder = Config['dnsServerSearchOrder']
            nic.EnableStatic(IPAddress=[ipAddress], SubnetMask=[subnetMask])
            nic.SetGateways(DefaultIPGateway=[defaultIPGateway])
            nic.SetDNSServerSearchOrder(DNSServerSearchOrder=[dnsServerSearchOrder])
    else:
        changeNic.EnableDHCP()
        changeNic.SetDNSServerSearchOrder()
        pass
    print("                          这是第{}次修改".format(changeCount))
    printDecollator()
    closeCommand = input("按Enter键继续，输入Q退出程序: ")
    printDecollator()
    changeCount+=1
    if str.upper(closeCommand) == "Q":
        break
