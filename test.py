


#Just using this file as a central place to test things




import project
import subnet_list


for i in subnet_list.test:
    asdf = project.subnet_input(i)
    if asdf == False:
        print("You entered shit poorly")
    else:
        print("The code works as far as i can tell")

print("Well no errors happened")

