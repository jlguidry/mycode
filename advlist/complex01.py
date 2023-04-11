#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   List - complex list """


def main():

    # create a list called list1
    list1 = ["cisco_nxos", "arista_eos", "cisco_ios"]

    # display list1
    print(list1)

    # display list1[1] 
    print(list1[1])

    # create a new list 
    list2 = ["juniper"]

    # extend list1 by list2
    list1.extend(list2)

    # display extended list
    print(list1)

    # create list3
    list3 = ["10.1.0.1", "10.2.0.1", "10.3.0.1"]

    # append list1 by list3
    list1.append(list3)

    # display new complex list
    print(list1)

    # print IP address list
    print(list1[4])
    
    # display first item in the list (first IP)
    print(list1[4][0])



main()

