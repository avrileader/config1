# -*- coding:utf-8 -*-
import os
import wmi
import json
def printDecollator():
    print("-" * 70)
def ipConfigFile():
    path = 'ipConfig.json'
    file = open(path, 'w',encoding='utf8')
    file.write('''{
    "NAME": {
     "ipAddress": "192.168.0.1",
     "subnetMask": "255.255.255.0",
     "defaultIPGateway": "192.168.0.1",
     "dnsServerSearchOrder": "192.168.0.1"
    }
}''')
print("正在获取网卡信息...")
changeCount = 1
while True:
    nicConfig = wmi.WMI().Win32_NetworkAdapterConfiguration(IPEnabled=True)
    nicWmi = wmi.WMI()
    nicData = {}
    nicCount = 0
    for nic in nicConfig:
        if nic.MACAddress is not None:
            nicCount+=1
            itemData = {}
            itemData['网卡型号'] = nic.Description
            itemData['物理地址'] = nic.MACAddress
            itemData['DHCP状态'] = nic.DHCPEnabled
            if nic.IPAddress is not None:
                itemData['IP 地址'] = nic.IPAddress[0]
            else:
                itemData['IP 地址'] = "无IP地址"
                pass
            if nic.IPSubnet is not None:
                itemData['子网掩码'] = nic.IPSubnet[0]
            else:
                itemData['子网掩码'] = "无子网掩码"
                pass
            if nic.DefaultIPGateway is not None:
                itemData['默认网关'] = nic.DefaultIPGateway[0]
            else:
                itemData['默认网关'] = "无默认网关"
                pass
            if  nic.DNSServerSearchOrder is not None:
                itemData['DNS服务器'] = nic.DNSServerSearchOrder[0]
            else:
                itemData['DNS服务器'] = "无DNS服务器"
                pass
            nicData["网卡[{}]".format(nicCount)] = itemData
    print(json.dumps(nicData,indent=1,ensure_ascii=False)) #ensure_ascii=False，json显示中文
    intNicList = [int(serialNumber) for serialNumber in range(1,nicCount+1)]
    strNicList = [str(serialNumber) for serialNumber in range(1,nicCount+1)]
    nicSelect = input("请输入网卡编号{}，默认网卡[1]: ".format(intNicList)) or "1" #因为第一个接口从0开始计数
    judgeNicSelect = nicSelect in strNicList
    while judgeNicSelect == False:
        printDecollator()
        nicSelect = input("无效的数据！请重新输入请输入网卡编号{}，默认网卡[1]: ".format(intNicList)) or "1"
        judgeNicSelect = nicSelect in strNicList
        if judgeNicSelect == True:
            break
    printDecollator()
    changeNic = nicConfig[int(nicSelect)-1]
    judgeFileExists = os.path.exists('ipconfig.json')
    if judgeFileExists == False:
        ipConfigFile()
    else:
        pass
    with open('ipconfig.json', 'r', encoding='utf-8') as ipFile:
        nameOrder = json.load(ipFile) #读取文件中IP地址顺序，字典方式
        nameList = list(nameOrder.keys()) #将字典的keys转换为列表
        nameConut = 1 #列表项目计数
        for config in nameList:
            nameConut+=1
        print(json.dumps(nameOrder, indent=1, ensure_ascii=False))  # 打印文件内容
        for index,value in enumerate(nameList,1): #获取名称索引
            printDecollator()
            print('选择序号[{}]{}>[{}]'.format(index,"-" * 30,value))
        printDecollator()
        strNameIndex = [str(serialNumber) for serialNumber in range(1,nameConut)] #将range里的数字转换为字符串存于列表
        strNameIndex.append('D')
        nameIndexSelect = input("请输入上面列出的序号，默认[DHCP]:") or 'D'  # 选择IP地址的索引
        printDecollator()
        judgeNameIndexSelect = nameIndexSelect in strNameIndex
        while judgeNameIndexSelect == False:
            nameIndexSelect = input("无效的数据！请重新输入上面列出的序号，默认[DHCP]:") or 'D'  # 选择IP地址的索引
            printDecollator()
            judgeNameIndexSelect = nameIndexSelect in strNameIndex
            if judgeNameIndexSelect == True:
                break
        if str.upper(nameIndexSelect) != 'D':
            ipConfig = nameOrder[nameList[int(nameIndexSelect) - 1]]  # 调用字典中的索引对应的内容
            changeNic.EnableStatic(IPAddress=[ipConfig['ipAddress']], SubnetMask=[ipConfig['subnetMask']])
            changeNic.SetGateways(DefaultIPGateway=[ipConfig['defaultIPGateway']])
            changeNic.SetDNSServerSearchOrder(DNSServerSearchOrder=[ipConfig['dnsServerSearchOrder']])
        else:
            changeNic.EnableDHCP()
            changeNic.SetDNSServerSearchOrder()
            pass
    print("                             这是第{}次修改".format(changeCount))
    printDecollator()
    closeCommand = input("按任意键继续，输入Q退出程序: ")
    printDecollator()
    changeCount+=1
    if str.upper(closeCommand) == "Q":
        break
