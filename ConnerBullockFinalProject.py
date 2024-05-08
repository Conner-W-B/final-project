







from tkinter import *
import ip_validate
import network_calculate
from network_calculate import network
mainwindow = Tk()
mainwindow.title("Subnet Caclulator")


            #Allow for ip address entry
ipentryframe = LabelFrame(mainwindow,padx=5,pady=5)
ipentryframe.grid(row=1,column=1,rowspan=1,columnspan=1)

iplabel = Label(ipentryframe,text="Enter Ip address")
iplabel.grid(row=1,column=1)
ipentry = Entry(ipentryframe,width=15)
ipentry.grid(row=2,column=1)

            #Allow for subnet entry
subnetentryframe = LabelFrame(mainwindow,padx=5,pady=5)
subnetentryframe.grid(row=1,column=2,rowspan=1,columnspan=1)

subnetlabel = Label(subnetentryframe,text="Enter Subnet for network")
subnetlabel.grid(row=1,column=2)
subnetentry = Entry(subnetentryframe,width=15)
subnetentry.grid(row=2,column=2)

            #Create button to calculate subnets

calculateframe = LabelFrame(mainwindow,padx=5,pady=5)
calculateframe.grid(row=1,column=3,rowspan=1,columnspan=1)

def button():
    
    ip=str(ipentry.get())
    subnet=str(subnetentry.get())
    print(ip,subnet)
    returnaddresses(ip,subnet)


calculatedrange = Button(calculateframe,text="Calculate",command=button,bg="white",fg="black")
calculatedrange.grid(row=1,column=3)



            #Function to handle ip and subnet, call for validation on both 
            #then call for calculating ip and subnet range
def calculateiprange(ip,subnet):
    ip = ip_validate.ip_format_validation(ip)
    subnet = ip_validate.ip_input(subnet)
    # if ip:
    #     return "Not a valid ip address"
    # if subnet:
    #     return "Not a valid subnet"
    ip=str(ipentry.get())
    subnet=str(subnetentry.get())
    Network = network.networkcalc(ip,subnet)
    return Network    



        #Function  to display returned addresses and format them
def returnaddresses(ip,subnet):

    Network = calculateiprange(ip,subnet)

    
    ipreturnwindow = Tk()
    ipreturnwindow.title("Ip address range and network")

    returnprompt=LabelFrame(ipreturnwindow,padx=10,pady=10)
    returnprompt.grid(row=1,column=1,rowspan=1,columnspan=1)

    returntext=Label(returnprompt,text="Network Address")
    returntext.grid(row=1,column=1)

    returniptext=LabelFrame(ipreturnwindow,padx=10,pady=10)
    returniptext.grid(row=1,column=2,rowspan=1,columnspan=1)
    print(Network)
    returnip=Label(returniptext,Text=Network.basenetwork)
    returnip.grid(row=2,column=2)



    iprange=LabelFrame(ipreturnwindow,padx=10,pady=10)
    iprange.grid(row=2,column=1,rowspan=1,columnspan=1)

    returnprompt=LabelFrame(ipreturnwindow,padx=10,pady=10)
    returnprompt.grid(row=1,column=1,rowspan=1,columnspan=1)










mainwindow.mainloop()



