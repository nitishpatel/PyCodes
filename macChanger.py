import subprocess
card=int(input("Enter Card\n1.eth0\n2.Wlan0\n-->"))
new_mac=str(input("Enter New Mac Address (Eg: 12:13:14:15:15:14):"))
if card==1:
	subprocess.call("ifconfig eth0 down",shell=True)
	subprocess.call("ifconfig eth0 hw ether "+new_mac,shell=True)
	subprocess.call("ifconfig eth0 up",shell=True)
elif card==2:
	subproces.call("ifconfig wlan0 down",shell=True)
	subprocess.call("ifconfig wlan0 hw ether "+new_mac,shell=True)
	subprocess.call("ifconfig  wlan0 up",shell =True)
else:
	print("Invalid Option")
