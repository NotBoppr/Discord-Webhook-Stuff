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
    spam()

def spam():
    clear()
    msg = input("[Message You Want To Spam]> ")
    if msg == "":
        input("[Please Give A Message]")
        spam()
    def repeat():
        try:
            clear()
            global amount
            print(f"[Message] {msg}")
            amount = int(input("[How Many Messages You Want To Spam]> "))
        except ValueError:
            input("[Please Enter A Number]")
            repeat()
    repeat()
    print("\n[Spamming Webhook...]")
    for i in range(amount):
        hook.send(msg)
    input("\n[Spamming Finished]")
    spam()

start()
