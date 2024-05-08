
#Module to verify if in ip decimal format and validate that is in the range of 0-255
#extra validation for subnets with extra flag 

import subnet_list #Importing static lists pertaining to subnet validation


def debug(bug):    #Bug reporting for troubleshooting
    import traceback
    from datetime import datetime
    trace = "".join(traceback.format_list(traceback.extract_stack()))
    with open("debug.txt", "a") as bug_file:
        now = datetime.now()
        bug_file.write(now.strftime("%Y-%m-%d %H:%M:%S") + "\n")
        bug_file.write(bug + "\n")
        bug_file.write("Traceback:" + trace + "\n")
        

def subnet_input(subnet):             #Getting input for calculations
    subnet, validation = validate_subnet(subnet)
    if validation:
        return True
    else:
        debug("Error Code 1")
        return False


def validate_subnet(subnet):              #Validation if input is either ip or shorthand format
    try:
        if "." in subnet:       #Check if decimal format
            if ip_format_validation(subnet, flag_sub=True):
                return subnet, True
            else:
                debug("Error Code 8")
                return None, False
        elif "/" in subnet:         #Check if shorthand
            subnet = int(str(subnet).strip("/").strip())
            if 0 <= subnet <=32:
                return subnet_short_validation(subnet), True
            else:
                debug("Error Code 7")
                return None, False
        else:
            debug("Error Code 2")
            return None, False
    except ValueError:
            debug("Error Code 9")
            return None, False

def ip_format_validation(ip, flag_sub=False):              #Validation of ip or subnet in decimal format
    octets = str(ip).split(".")
    if int(len(octets)) != 4:            #If there are 4 numbers seperated by a "."
        debug("Error Code 3")
        return False
    
    for octet in octets:                      #Check if each set of decimal numbers is valid
        try:
            octet_int = int(octet)
            if not 0 <= octet_int <= 255:
                debug("Error Code 4")
                return False
        except ValueError:
            debug("Error Code 5")
            return False
        
    if flag_sub:    #Flag to check agasint standard subnet octet's
        sub_octets = subnet_list.subnet_octet
        if any(all(sub_octet != ip_octet for ip_octet in octets) for sub_octet in sub_octets):
            debug("Error Code 6")
            return False
        
        
    return True

def subnet_short_validation(subnet):           #Function to determine format of input
    return subnet_list.subnets[subnet]
            

def ip_input(ip):
    try:
        if ip_format_validation(ip):
            return False
        else:
            return True
    except ValueError:
        return False