#iflogic netmiko ssh

from netmiko import ConnectHandler

iosv = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.71',
    'username': 'avram',
    'password': 'cisco'
}

net_connect = ConnectHandler(**iosv)
output = net_connect.send_command('show version')
print(output)

output1 =  (output.find('IOSv'))
if output1 > 0:
    IOSv = True
else:
    IOSv = False
print('IOSv = ', IOSv)
router = True

if router:
     IOSv = True
else:
    IOSv = False
print('IOSv = ', IOSv)
router = True

if router:
    if IOSv:
        print('This is a IOSv router.')
    else:
        print('This is a router, but not a IOSv router.')
else:
    print('Not a router.')


