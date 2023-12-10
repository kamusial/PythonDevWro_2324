import os
import time

ts1 = time.time()
print(os.getcwd())
os.chdir('C:\\Users\\vdi-student\\Desktop\\')
print(os.getcwd())
time.sleep(1)
os.mkdir('Nowy_folder')
time.sleep(1)
os.rename('Nowy_folder', 'NOWSZY_folder')
time.sleep(1)
os.rmdir('NOWSZY_folder')
ts2 = time.time()
print(f'czas trwania {ts2-ts1}')
#print(os.environ)

os.system('cmd /c "ipconfig "')

