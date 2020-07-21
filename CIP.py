import wmi
import json
def printDecollator():
    print("**********************************************************")
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
            if  nic.DNSServerSearchOrder is not None:
                item_data['DNS服务器'] = nic.DNSServerSearchOrder[0]
            else:
                item_data['DNS服务器'] = "无DNS服务器"
            if nic.IPAddress is not None:
                item_data['IP 地址'] = nic.IPAddress[0]
                item_data['子网掩码'] = nic.IPSubnet[0]
            else:
                item_data['ipaddress'] = "无IP地址"
                item_data['netmask'] = "无子网掩码"
            nicData["网卡{}".format(nicCount)] = item_data
    print(json.dumps(nicData,indent=1,ensure_ascii=False)) #ensure_ascii=False，json显示中文
    intNiclist = [int(serialNumber) for serialNumber in range(1,nicCount+1)]
    strNiclist = [str(serialNumber) for serialNumber in range(1,nicCount+1)]
    nicNumber = str(input("请输入网卡编号{}，默认为网卡[1]: ".format(intNiclist))) or "1" #因为第一个接口从0开始计数
    judgeNic = nicNumber in strNiclist
    while judgeNic == False:
        printDecollator()
        nicNumber = str(input("无效的数据！请重新输入请输入网卡编号{}，默认为网卡[1]: ".format(intNiclist))) or "1"
        judgeNic = nicNumber in strNiclist
        if judgeNic == True:
            break
    printDecollator()
    changeNic = nicConfig[int(nicNumber)-1]
    print(changeNic)
    changeDHCP = input("是否需要动态获取IP地址(y or n): ") or "y"
    judgeList = ['y', 'n', 'Y', 'N']
    judgeDHCP = changeDHCP in judgeList
    print(judgeDHCP)
    while judgeDHCP == False:
        changeDHCP = input("是否需要动态获取IP地址(y or n): ") or "y"
        judgeDHCP = changeDHCP in judgeList
        if  judgeDHCP == True:
            break
    printDecollator()
    if str.upper(changeDHCP) == "N":
        changeAddress = input("请输入IP地址: ")
        printDecollator()
        changeNetmask = input("子网掩码是否为255.255.255.0(y or n): ")
        printDecollator()
        if changeNetmask=="n":
            netMask = input("请输入子网掩码：")
            printDecollator()
        else:
            netMask = "255.255.255.0"
        changeGateway = input("请输入网关地址: ")
        printDecollator()
        changeDNS = input("是否将DNS地址设置与网关地址相同(y or n)：")
        printDecollator()
        if changeDNS=="n":
            DNS = input("请输入DNS地址: ")
            printDecollator()
        else:
            DNS = changeGateway
        changeNic.EnableStatic(IPAddress=[changeAddress], SubnetMask=[netMask])
        changeNic.SetGateways(DefaultIPGateway=[changeGateway])
        changeNic.SetDNSServerSearchOrder(DNSServerSearchOrder=[DNS])
    else:
        changeNic.EnableDHCP()
        changeNic.SetDNSServerSearchOrder()
        pass
    print("                      这是第{}次修改".format(changeCount))
    printDecollator()
    closeCommand = input("按Enter键继续，输入Q退出程序: ")
    printDecollator()
    changeCount+=1
    if str.upper(closeCommand) == "Q":
        break
