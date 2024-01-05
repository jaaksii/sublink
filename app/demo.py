import re

def if_ipv6_address(string):
    pattern = r'\[([0-9a-fA-F:]+)\]'
    match = re.search(pattern, string)
    if match:
        ipv6_address = match.group(1)
        return ipv6_address
    else:
        return string

# 要提取IPv6地址的字符串
string = "192.168.2.12:12613"

# 提取IPv6地址
result = if_ipv6_address(string)

if result:
    print("提取的IPv6地址:", result)
else:
    print("未找到IPv6地址")
