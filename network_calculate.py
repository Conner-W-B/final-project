
 
class network():
                #Define opject for every possible output for ip range
    def __init__(self=None,address=None,subnet=None,oct1=None,oct2=None,oct3=None,oct4=None,suboct=None,octpos=None,addresses=None,reversemask=None,bitmask=None,basenetwork=None,first=None,last=None,broadcast=None):
        self.address=address
        self.subnet=subnet
        self.oct1=oct1
        self.oct2=oct2
        self.oct3=oct3
        self.oct4=oct4
        self.suboct=suboct
        self.octpos=octpos
        self.addresses=2
        self.reversemask=reversemask
        self.bitmask=bitmask
        self.basenetwork=basenetwork
        self.first=first
        self.last=last
        self.broadcast=broadcast
            

            #Changing ip address to sets of octets
    def ipoct(Network):
        
        ip=str(Network.address).split(".")
        Network.oct1=ip[0]
        Network.oct1=ip[1]
        Network.oct1=ip[2]
        Network.oct1=ip[3]
        print("ipoct")
        print(Network.address)
        return Network


            #Changing subnet into sets of octets
    def suboctet(Network):
        subnet=str(Network.subnet).split(".")
        for index , value in enumerate(subnet):
            print(index,value)
            if value != 255:
                Network.suboct= str(value)
                Network.octpos = 3 - index
                print("In the loop")
                break
            print(index,value)
            for _ in range(Network.octpos):
                for _ in range(8):
                    Network.addresses *= 2
        Network.addresses + int(Network.suboct) - 257
        print("suboctet")
        return Network
    

        #Calculating base network and reverse mask, reverse mask is inverse of subnet in binary but in decimal format
        #Calculations are done by turning values into binary using bitwise then back to decimal
    def iprange(Network):
        print("iprange start")
        ipdecimal = []
        subdecimal = []
        address = str(Network.address).split(".")
        subnet = str(Network.subnet).split(".")
        for i in range(4):
            for l in range(4):
                ipdecimal[i] = bin(int(address[l])).strip("0b")
        for i in range(4):
            for l in range(4):
                subdecimal[i] = bin(int(subnet[l])).strip("0b")
        
        counter = 0
        networkdecimal = ""
        hostdecimal = ""
        while counter !=3:
            tempip = ipdecimal[counter]
            tempsub = subdecimal[counter]
            for i in range(8):
                if tempip[i] == tempsub[i]:
                    networkdecimal += "1"
                else:
                    networkdecimal += "0"
                if tempsub == "1":
                    hostdecimal += "0"
                else:
                    hostdecimal += "1"

        for _ in range(4):
            Network.basenetwork = str(int(networkdecimal[8:],2))+"."
            networkdecimal = int(str(networkdecimal)[8:])
            Network.reversemask = str(int(hostdecimal[8:],2))+"."
            hostdecimal = int(str(hostdecimal)[8:])
        print("iprange done")
        print(Network)
        return Network



                #Using previous calculations to find network broadcast
                #Calculation is Networkportion of Base Ip + Host portion of reverse mask
    def ipcalc(Network):
        print("Ipcalc start")
        subnet = str(Network.subnet).split(".")
        address = str(Network.address).split(".")
        reverse = Network.reversemask.split(".")
        broadcast = []
        for i in range(4):
            if subnet[i] == "255":
                broadcast[i] = address[i]
            if subnet[i] == "0":
                broadcast[i] = reverse[i]
            else:
                broadcast[i] = str(int(reverse[i]) + int(address[i]))
        Network.broadcast = broadcast[1]
        for i in range(1,3,1):
            if i != 3:
                Network.broadcast += broadcast[i]+"."
            else:
                Network.broadcast + broadcast[i]
        print("ipcalc done")
        print(Network)
        return Network


                #Main call to run functions and calculations
    def networkcalc(ip,subnet):
        Network=network()
        Network.address = ip
        Network.subnet = subnet
        Network = network.ipoct(Network)
        print("1")
        subnet = network.suboctet(Network)
        print(Network)
        Network.octpos = subnet.octpos
        Network.suboct = subnet.suboct
        print(Network.address)
        Network = network.iprange(Network)
        print("1")
        Network = network.ipcalc(Network)
        print("1")
        print(Network)
        return Network


        



