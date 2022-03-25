import wmi
import os
import time

constructor = wmi.WMI()

chromeDriversFound = []
quitTime = 0
numberOfBots = 0
with open("quitTime.txt","r") as f:
    quitTime = int(f.read())
def findProcesses():
    chromesFound = []
    for process in constructor.Win32_Process():
        process
        if process.Name == "chrome.exe":
            chromesFound.append(process.ProcessId)
    return chromesFound

for process in constructor.Win32_Process():
    if process.Name == "chromedriver.exe":
        chromeDriversFound.append(process.ProcessId)


print("[G] Finding chromes")
chromes = findProcesses()
while chromes !=[]:
    for chrome in chromes:
        os.system(f"taskkill /F /PID {chrome}")
        time.sleep(quitTime)
        chromes.clear()
    chromes = findProcesses()
print("[G] All chromes have been quit.")
print("[G] Finding chromedrivers.")
for chromeDriver in chromeDriversFound:
    os.system(f"taskkill /F /PID {chromeDriver}")
print("[G] All chromedrivers have been quit.")
os.system("taskkill /F /im bot.exe")
print("[G] Done.")

