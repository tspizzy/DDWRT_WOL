
import paramiko

from time import sleep
#SSH WOL Script

# set vars for DD-WRT credentials
host = '' #WAN IP or DDNS name for router
sshport =    #port in integer format- no quotes!
user = 'root' #username is root for telnet/ssh connections
my_password = '' #router admin password

#vars for WOL


broadcast_ip = '' #usually your subnet plus .255 (eg 192.168.1.255)
packet_port = '7' #usually 7
device_mac = '' #MAC address of the network port on the device you want to wake up.



#connecting
print "Connecting..."
client = paramiko.SSHClient()
client.load_system_host_keys(filename=None)
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, port=sshport, username=user, password=my_password)
sleep(1)
(stdin, stdout, stderr) = client.exec_command("uptime")


print stdout.read()





#
#execute commands
wake_command = '/usr/sbin/wol -i '+ broadcast_ip + ' -p '+ packet_port + ' ' + device_mac
print wake_command

print "Waking..."
(stdin, stdout, stderr) = client.exec_command(wake_command)
sleep(0.5)

#disconnect
client.close()
print "Disconnected"


