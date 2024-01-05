#!/usr/bin/python

import os
import time

# 1. 在列表中指定要备份的文件或目录
source = ['/etc/paths', '/etc/ssh']
# window中用 source = [r'C:\Documents', r'D:\Work']或其他类似功能

# 2. 备份存储目标的目录
target_dir = '/tmp/'

# 3. 文件备份到zip文件中
# 4. 当前日期是主目录的子目录
today = target_dir + time.strftime('%Y%m%d')
# 当前时间是日期目录的子目录
now = time.strftime('%H%M%S')

# 给zip文件一个有意义的名字
# comment = raw_input('Enter a comment --> ')
comment = "a.zip"
if len(comment) == 0:  # 是否输入注释名
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + \
      comment.replace(' ', '_') + '.zip'
# Notice the backslash!

# 如果目录不存在，创建它
if not os.path.exists(today):
    os.mkdir(today) # make directory
    print('Successfully created directory', today)

# 5. 使用linux的zip命令把文件打包到zip包中
zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))

# Run the backup
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')