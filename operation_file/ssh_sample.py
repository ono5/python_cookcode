import subprocess, paramiko


client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.WarningPolicy())
client.connect('ipaddress', username='hostname', password='*****')

client.exec_command('mkdir test')
client.exec_command('cd test')
client.exec_command('pwd')

# stdin, stdout, stderr = client.exec_command('ls -a')
# for line in stdout:
#     print(line)

client.exec_command('/home/ubuntu/test/test.sh')

stdin, stdout, stderr = client.exec_command('/home/ubuntu/test/test.sh')
for line in stdout:
    print(line)

client.close()