import subprocess

# ls を実行
subprocess.run(['ls'])

# ls -a を実行
subprocess.run(['ls', '-a'])

# ls -a を実行
subprocess.run('ls -al', shell=True)

p1 = subprocess.Popen(['ls', '-al'], stdout=subprocess.PIPE)
p2 = subprocess.Popen(
    ['grep', 'test'], stdin=p1.stdout, stdout=subprocess.PIPE)
p1.stdout.close()
output = p2.communicate()[0]
print(output)

# ============================================
# | を使う
subprocess.run('ls -al | grep test', shell=True)

# return コード取得
r = subprocess.run('ls', shell=True)
print(r.returncode)
print('###')

# check をつけると例外を検知
r = subprocess.run('ls', shell=True, check=True)
print('###')
# ============================================

