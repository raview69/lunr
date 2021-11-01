import shutil
import subprocess
import random
import os

ra = random.randint(70000, 1000000)
ra2 = random.randint(700, 1000)
a = input("masukan nama file ip : ")
b = input("masukan nama file config : ")
ad = open(a, 'r').read().splitlines()
ap = open(a, 'r').readlines()
c = len(ap)
for i in range(0, c):
    shutil.copyfile(f"{b}", f"visitor{[0+i]}.py")
    with open(f'visitor{[0+i]}.py', f'r') as file :
        filedata = file.read()
    filedata = filedata.replace('kontol', ad[0+i])
    with open(f'vis{[0+i]}.py', 'w') as file:
        file.write(filedata)
    os.remove(f"visitor{[0+i]}.py")


