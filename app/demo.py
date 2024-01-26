import re

# 读取配置文件
with open('surge.conf', 'r') as conf_file:
    conf_data = conf_file.read()

# 定义正则表达式模式
pattern = r'(\[\'Proxy Group\'\].*?)(auto)'

# 执行替换操作
new_conf_data = re.sub(pattern, r'\1asdasd', conf_data, count=1)

# 保存修改后的配置文件
with open('surge.conf', 'w') as conf_file:
    conf_file.write(new_conf_data)
