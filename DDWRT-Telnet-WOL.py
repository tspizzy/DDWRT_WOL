
import telnetlib
from time import sleep
#Telnet WOL Script

# set vars for DD-WRT credentials
host = '' #WAN IP or DDNS name for router
user = 'root' #username is root for telnet connections
my_password = '' #router admin password

#vars for WOL


broadcast_ip = '' #usually your subnet plus .255 (eg 192.168.1.255)
packet_port = '7' #usually 7
device_mac = '' #MAC address of the network port on the device you want to wake up.

print "Connecting..."
# Telnet to server
tn = telnetlib.Telnet(host)
sleep(0.5)
print "Logging In..."
#look for login prompt
tn.read_until("login: ")



#enter username, press enter
tn.write(user + '\n')
print 'username sent'

#print tn.read_all()

#enter password, press enter
#print "Entering password."
tn.read_until("Password: ")



sleep(0.5)
tn.write(my_password + '\n')
print "Password entered"
sleep(0.5)


#execute commands

print "Waking..."
tn.write("/usr/sbin/wol -i "+ broadcast_ip + " -p "+ packet_port + " " + device_mac + '\n')

sleep(0.5)

#disconnect
tn.write("exit\n")
print "Disconnected"

#to see output, uncomment below
#print tn.read_very_eager()

