# def decode_base64_if(text):
#     text = urllib.parse.unquote(text)
#     def base64_decoder(match):
#         base64_str = match.group(0)
#         try:
#             # 补齐长度
#             while len(base64_str) % 4 != 0:
#                 base64_str += '='
#
#             # 解码base64编码
#
#             decoded_bytes = base64.b64decode(base64_str)
#             return decoded_bytes.decode('utf-8')
#         except (base64.binascii.Error, UnicodeDecodeError):
#             # 如果解码失败，直接返回原始base64编码
#             return match.group(0)
#
#     # 匹配文本中的所有base64编码并替换
#
#     result = re.sub(r'([A-Za-z0-9+/]+={0,2})', base64_decoder, text)
#
#     return result
