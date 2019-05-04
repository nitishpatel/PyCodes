# PyCodes
Python Codes From My Youtube Tutorials

1 - > MacChanger
<iframe
  src="https://carbon.now.sh/embed/?bg=rgba(74%2C144%2C226%2C1)&t=dracula&wt=none&l=python&ds=true&dsyoff=20px&dsblur=68px&wc=true&wa=true&pv=87px&ph=100px&ln=false&fm=Hack&fs=13px&lh=153%25&si=false&es=4x&wm=false&code=%2523Mac%2520Changer%2520For%2520Linux%2520%250Aimport%2520subprocess%250A%250A%2523Code%250Adef%2520macChanger(card_name%252Cmac)%253A%250A%2520%2520%2509subprocess.call(%2522ifconfig%2520%2522%252Bcard_name%252B%2522%2520down%2522%252Cshell%253DTrue)%250A%2509subprocess.call(%2522ifconfig%2520%2522%252Bcard_name%252B%2522%2520hw%2520ether%2520%2522%252Bnew_mac%252Cshell%253DTrue)%250A%2509subprocess.call(%2522ifconfig%2520%2522%252Bcard_name%252B%2522%2520up%2522%252Cshell%253DTrue)%250Acard%253Dint(input(%2522Enter%2520Card%255Cn1.eth0%255Cn2.Wlan0%255Cn--%253E%2522))%250Anew_mac%253Dstr(input(%2522Enter%2520New%2520Mac%2520Address%2520(Eg%253A%252012%253A13%253A14%253A15%253A15%253A14)%253A%2522))%250Aif%2520card%253D%253D1%253A%250A%2509macChanger(%2522eth0%2522%252Cnew_mac)%250Aelif%2520card%253D%253D2%253A%250A%2509macChanger(%2522wlan0%2522%252Cnew_mac)%250Aelse%253A%250A%2509print(%2522Invalid%2520Option%2522)%250A"
  style="transform:scale(0.7); width:1024px; height:473px; border:0; overflow:hidden;"
  sandbox="allow-scripts allow-same-origin">
</iframe>
