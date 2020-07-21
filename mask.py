import os
import wmi
import json

print("正在获取网卡信息...")
deadCycle = 1 #设置一个死循环
changeCount = 1
while deadCycle <2:
    nic = os.system("ipconfig /all")
    # nicConfig = wmi.WMI().Win32_NetworkAdapterConfiguration(IPEnabled=True)
    '''Win32_ NetworkAdapterConfiguration()方法
    NetworkAdapterConfiguration网络适配器的意思
    函数调用: interfaceList = w.Win32_NetworkAdapterConfiguration(IPEnabled=1)
    函数功能: 用于网络接口信息对象，并存以列表形式
    传入参数: *argv
    IPEnabled: bool 类型，可传入1，默认为False，为 True 将显示 IP 信息
    返回参数: interfaceList
    interfaceList: list 类型，list 中每个元素均为一个网络接口信息的 object
    网络接口信息 object 通过 object.name 调用，所含信息包括（部分具体信息已删除）:'''
    # nicWmi = wmi.WMI()
    # nicData = {}
    # count = 0
    # for nic in nicConfig:
    #     if nic.MACAddress is not None:
    #         count+=1
    #         item_data = {}
    #         item_data['网卡型号'] = nic.Description
    #         item_data['物理地址'] = nic.MACAddress
    #         item_data['DHCP状态'] = nic.DHCPEnabled
    #         if  nic.DNSServerSearchOrder is not None:
    #             item_data['DNS服务器'] = nic.DNSServerSearchOrder[0]
    #         else:
    #             item_data['DNS服务器'] = "无DNS服务器"
    #         if nic.IPAddress is not None:
    #             item_data['IP 地址'] = nic.IPAddress[0]
    #             item_data['子网掩码'] = nic.IPSubnet[0]
    #         else:
    #             item_data['ipaddress'] = "无IP地址"
    #             item_data['netmask'] = "无子网掩码"
    #         nicData["网卡%s" %count] = item_data
    # print(json.dumps(nicData,indent=1,ensure_ascii=False)) #ensure_ascii=False，json显示中文
    # firstNetcard = input("是否为所列出的第一个网卡(y or n): ")
    # print("**********************************************************")
    # if  firstNetcard=="n":
    #      nicNumber = int(input("请选择网卡编号: "))-1 #因为第一个接口从0开始计数
    #      print("**********************************************************")
    # else:
    #     nicNumber = 0
    # changeNic = nicConfig[nicNumber]
    changeDHCP = input("是否需要动态获取IP地址(y or n): ")
    print("**********************************************************")
    if changeDHCP=="n":
        changeAddress = input("请输入IP地址: ")
        print("**********************************************************")
        changeNetmask = input("子网掩码是否为255.255.255.0(y or n): ")
        print("**********************************************************")
        if changeNetmask=="n":
            netMask = input("请输入子网掩码：")
            print("**********************************************************")
        else:
            netMask = "255.255.255.0"
        changeGateway = input("请输入网关地址: ")
        print("**********************************************************")
        changeDNS = input("是否将DNS地址设置与网关地址相同(y or n)：")
        print("**********************************************************")
        if changeDNS=="n":
            DNS = input("请输入DNS地址: ")
            print("**********************************************************")
        else:
            DNS = changeGateway
        os.system("netsh interface ip set address name=WLAN static {Address} {Netmask} {Gateway}" .format(Address=changeAddress,Netmask=netMask,Gateway=changeGateway))
        # changeNic.EnableStatic(IPAddress=[changeAddress], SubnetMask=[netMask])
        # changeNic.SetGateways(DefaultIPGateway=[changeGateway])
        # changeNic.SetDNSServerSearchOrder(DNSServerSearchOrder=[DNS])
    else:
        os.system("netsh interface ip set address name=WLAN source=dhcp")
        os.system("netsh interface ip set dns name=WLAN source=dhcp")
        # changeNic.EnableDHCP()
        # changeNic.SetDNSServerSearchOrder()
        pass
    print("                      这是第{}次修改".format(changeCount))
    print("**********************************************************")
    closrNumber = input("按Enter键继续，输入Q退出程序: ")
    print("**********************************************************")
    changeCount+=1
    if closrNumber=="q":
        deadCycle = 2
    else:
        deadCycle = 1
