import os
import time

# import socket
# hostname = socket.gethostname()
# IPAddr = socket.gethostbyname(hostname)
# print("Your Computer Name is:" + hostname)
# print("Your Computer IP Address is:" + IPAddr)

print(os.getcwd())
os.chdir('C:\\Users\\vdi-student\\Desktop\\')
print(os.getcwd())
os.mkdir('new_folder')
os.rename('new_folder', 'NOWSZY_FOLDER')
# os.rmdir('NOWSZY_FOLDER')
#os.system('cmd /c "dir /s new.txt >> result.txt"')
os.system('cmd /c "cd C:\\Users\\vdi-student\\Desktop\\NOWSZY_FOLDER\\  && ipconfig /all > result.txt"')
