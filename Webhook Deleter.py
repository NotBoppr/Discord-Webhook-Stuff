import os
import dhooks
clear = lambda: os.system("cls")

def start():
    clear()
    global url
    global hook
    url = input("Webhook: ").replace("canary.", "").replace("ptb.", "").replace("discordapp", "discord")
    if url == "":
        input("[Please Give A Webhook]")
        start()
    else:
        try:
            dhooks.Webhook(url).get_info()
            hook = dhooks.Webhook(url)
        except:
            input("[Webhook Doesn't Exist]")
            start()
    delhook()

def delhook():
    try:
        hook.delete()
        input("[Webhook Deleted]")
    except:
        input("[Failed To Delete Webhook]")

start()
