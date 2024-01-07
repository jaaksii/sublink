import base64
def decode_base64_if(text):  # base64解码
    try:
        name = ''
        decoded_text = text
        at = ''
        if '#' in decoded_text:
            name = '#' + decoded_text.split('#')[1]
            decoded_text = decoded_text.split('#')[0]
        if '@' in decoded_text:
            at = '@' + decoded_text.split('@')[1]
        padding = 4 - (len(decoded_text) % 4)
        # 判断是否需要补齐长度
        if padding > 0 and padding < 4:
            # 添加填充字符
            decoded_text += "=" * padding
        decoded_text = base64.b64decode(decoded_text).decode('utf-8')
        print('解：' + decoded_text)
        return decoded_text + at + name
    except:
        # 如果无法解码为Base64，则返回原始文本
        print('不是base64')
        return text
encoded_text = "YWVzLTEyOC1nY206MjhiMzA3MTctZjA2Yy00MzI2LTk1ZDYtYTBkY2MwOGMzMWE1"
decoded_text = decode_base64_if(encoded_text)
print(decoded_text)
