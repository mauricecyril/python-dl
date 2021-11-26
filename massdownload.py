import time
import os
import subprocess

for i in range(0,1):
    filename = str("/home/user/list.txt")
    websitefile = open(filename, "r").read().splitlines()

    for k in websitefile:
#        rundl = subprocess.run(["youtube-dl" + " -cti " + k + " --referer " + ""], shell=True)
        rundl = subprocess.run(["youtube-dl" + " -cti " + k ], shell=True)
        print(rundl)

        time.sleep(2)

    print("Pausing for the next download")
    time.sleep(15)
    print("Starting Next Download")

print("Completed Downloads")
