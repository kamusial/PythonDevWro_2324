import os
import time

print(os.getcwd())
os.chdir('C:\\Users\\vdi-student\\Desktop\\')
print(os.getcwd())
time.sleep(2)
os.mkdir('new_folder')
time.sleep(2)
os.rename('new_folder', 'NOWSZY_FOLDER')
time.sleep(2)
os.rmdir('NOWSZY_FOLDER')