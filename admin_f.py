import requests as r
import os
class color:
    GREEN = '\033[92m'
    GREEN1 = '\033[32m'
    WHITE = '\033[0m'
    RED = '\033[91m'
    BLUE = '\033[96m'
def __start__():
    os.system('clear')
	
	
    print(color.GREEN1 + '')
	
    print('███╗   ███╗ ██████╗ ██╗  ██╗ ██████╗     ████████╗███╗   ███╗')
    print('████╗ ████║██╔═══██╗██║  ██║██╔═══██╗    ╚══██╔══╝████╗ ████║')
    print('██╔████╔██║██║   ██║███████║██║   ██║       ██║   ██╔████╔██║')
    print('██║╚██╔╝██║██║   ██║██╔══██║██║▄▄ ██║       ██║   ██║╚██╔╝██║')
    print('██║ ╚═╝ ██║╚██████╔╝██║  ██║╚██████╔╝       ██║   ██║ ╚═╝ ██║')
    print('╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝ ╚══▀▀═╝        ╚═╝   ╚═╝     ╚═╝')
    print(color.GREEN + '                            ************************************')
    print('                            ** Telegram : @Hamiyan_Haj_Qassem **')
    print('                            **     Email : mohq@gmail.com     **')
    print('                            **      Developer : PDHNMSN       **')
    print('                            ************************************')
    #url
    url = str(input (color.BLUE+"Enter your target address (Example: https://www.google.com/) : "))
    #admin_list
    ad_list=open("admin.txt","r")
    #range
    for i in ad_list:
        req=r.post(url+i.strip())
        if req.status_code == 200:
            print("{} Admin Panel {} => {} {} {} Found".format(color.GREEN,color.RED,color.GREEN1,url+i,color.GREEN))
            exit()

        else:
            print("{} Not Found {} {}".format(color.RED,color.WHITE,url+i))
__start__()
