import sys, time, os, socket, requests
ip = socket.gethostname()
site = input()
ping = " ping"

print("""
⠀▄▄▄▄▄▄▀▀▀▀▀▀▀▄▄ █⠀⠀⠀⠀⠀⠀▀▄⠀⠀⠀▄▀⠀█▀▀▄▄ 
⠀█⠀⠀⠀⠀█▀⠀▀▄▀⠀▄▀⠀⠀⠀⠀⠀▀▀▄▄
⠀⠀█⠀⠀⠀⠀▀▄█⠀▄▀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀▀▀▄ 
⠀⠀⠀█⠀▄▄⠀⠀█⠀█⠀⠀█▀█⠀⠀⠀⠀⠀⠀▀█⠀█ 
⠀⠀⠀⠀██⠀▀▀▄▄█⠀⠀▀⠀▀⠀⠀⠀⠀⠀⠀⠀⠀⠀█ 
⠀⠀⠀⠀⠀▀█⠀█⠀⠀⠀█⠀⠀⠀⠀⠀▀▄▄▀▀▄▄█ 
⠀⠀⠀⠀⠀⠀⠀▀█⠀⠀⠀█▄▄▄▄▄▄▄▄▄▄▄█
 ⠀⠀⠀⠀⠀⠀▄▀▀█⠀⠀⠀█ ⠀⠀⠀⠀⠀⠀▄▀⠀⠀⠀█▀▀▀█▀▄ 
⠀⠀⠀⠀▄▀⠀⠀⠀⠀⠀▀▀▀⠀⠀⠀█ ⠀⠀⠀█⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀█ 
⠀⠀⠀█⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀█ ⠀⠀⠀█⠀⠀⠀⠀⠀█▀█⠀⠀⠀█⠀█ 
⠀⠀⠀⠀▀▄⠀▄█⠀⠀▄▀⠀█⠀█ ⠀⠀⠀⠀⠀▀⠀⠀⠀⠀▀▀▀""")
time.sleep(5)
hostname = socket.gethostname()   
IPAddr = socket.gethostbyname(hostname)   
print("Your Computer Name is:" + hostname)   
print("Your Computer IP Address is:" + IPAddr)
os.system(f"{ping}{site}")
