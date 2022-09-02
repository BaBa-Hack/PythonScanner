# We need run the code with Thread Cause WE need multi process for the future programming
import threading
import time

import python_socket_scanner as myscanner


def Interface():
        # Basic user interface header
    print(r"""
    ▄████████    ▄█   ▄█▄         ▄█    █▄       ▄████████  ▄████████    ▄█   ▄█▄ 
    ███    ███   ███ ▄███▀        ███    ███     ███    ███ ███    ███   ███ ▄███▀ 
    ███    █▀    ███▐██▀          ███    ███     ███    ███ ███    █▀    ███▐██▀   
    ███         ▄█████▀          ▄███▄▄▄▄███▄▄   ███    ███ ███         ▄█████▀    
    ███        ▀▀█████▄         ▀▀███▀▀▀▀███▀  ▀███████████ ███        ▀▀█████▄    
    ███    █▄    ███▐██▄          ███    ███     ███    ███ ███    █▄    ███▐██▄   
    ███    ███   ███ ▀███▄        ███    ███     ███    ███ ███    ███   ███ ▀███▄ 
    ████████▀    ███   ▀█▀        ███    █▀      ███    █▀  ████████▀    ███   ▀█▀ 
                ▀                                                       ▀         
    """)
    print("\n****************************************************************")
    #print("\n* Copyright of Austin0072009, 2022                              *")
    print("\n* 官网:https://www.ckhack.com                                  *")
    print("\n****************************************************************")
    print("\n****************************************************************")
    print("\n1:端口扫描")
    print("\n2:暴力破解SQL")
    print("\n3:木马上传")
    print("\n****************************************************************")
    print("\n*********************输入指令Enter******************************")

    choose = int(input())
    if choose == 1 :
        # arg1 : the function will run in the thread
        # arg2 : the args will pass to the funtion 
        print("端口扫描服务启动")

        t1 = threading.Thread(target=myscanner.Start, args=())
        t1.start()

    elif choose == 2:
        print("Developing....")
    elif choose == 3:
        print("Developing...")


if __name__ == "__main__":

    Interface()

