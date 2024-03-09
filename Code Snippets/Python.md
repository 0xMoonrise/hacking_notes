***
Serve a reverse shell with `Scripts/server_shell.py`
```
usage: server_shell.py [-h] [-t TYPE] [-i INET] [-p PORT]

options:
  -h, --help            show this help message and exit
  -t TYPE, --type TYPE  Set up type shell: 
	  standard | mkfifo | bash_udp | bash_5 | bashrl
  -i INET, --inet INET  Set up the listening interface: 
	  tun0 | eth0 | enp4s0
  -p PORT, --port PORT  Set netcat port listening
```
