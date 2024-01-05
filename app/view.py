from flask import Blueprint,request,jsonify,render_template,url_for
from .model import *
import base64,yaml,urllib.parse,os,re
from flask_jwt_extended import jwt_required,get_jwt_identity,create_access_token,create_refresh_token
blue = Blueprint('blue',__name__)
path = os.path.dirname(os.path.abspath(__file__))
def if_ipv6_address(string): # 判断ipv6
    pattern = r'\[([0-9a-fA-F:]+)\]'
    match = re.search(pattern, string)
    if match:
        ipv6_address = match.group(1)
        return ipv6_address
    else:
        return string
def decode_base64_if(text):  # base64解码
    try:
        name = ''
        decoded_text = text
        if '#' in decoded_text:
            name = '#' + decoded_text.split('#')[1]
            decoded_text = decoded_text.split('#')[0]
        padding = 4 - (len(decoded_text) % 4)
        # 添加填充字符
        decoded_text += "=" * padding
        decoded_text = base64.b64decode(decoded_text).decode('utf-8')
        return decoded_text + name
    except:
        # 如果无法解码为Base64，则返回原始文本
        # print('不是base64')
        return text
def clash_encode(subs): #clash编码
    # 初始化 Clash 配置
    clash_config = {
            'proxies':[],
            'proxy-groups': []
        }
    proxy_name_list = []
    # 解析并添加节点到 Clash 配置
    for sub in subs:
        proxy_type = sub.node.split('://')[0]  # 节点类型
        proxy_test = sub.node.split('://')[1]  # 节点信息
        # print(proxy_type,proxy_test)
        # 处理 VLESS 节点
        if proxy_type == 'vless':
            parse = urllib.parse.urlparse(decode_base64_if(proxy_test))
            query = urllib.parse.parse_qs(parse.query)
            print(query)
            urlpath = decode_base64_if(parse.path)  # uuid@服务器:端口
            uuid = decode_base64_if(urlpath.split('@')[0]) # uuid
            proxy_name = urllib.parse.unquote(parse.fragment)  # url解码
            server_port = urlpath.split('@')[1] # 服务器:端口
            server = if_ipv6_address(server_port.rsplit(':',1)[0]) # 服务器
            port = server_port.rsplit(':',1)[1] # 端口
            # vless配置
            proxy = {
                'name': proxy_name,
                'type': proxy_type,
                'uuid': uuid,
                'server': server,
                'client-fingerprint': 'chrome',
                'port': int(port),
                'network': query.get('type')[0],
                'udp':True,
                'skip-cert-verify': True,
                'tfo': False,
                'tls': True if query.get('sni') else False,
            }
            # 替换规则
            if query.get('fp'):
                proxy['client-fingerprint'] = query.get('fp')[0]
            if query.get('sni'):
                proxy['servername'] = query.get('sni')[0]
            if query.get('flow'):
                proxy['flow'] = query.get('flow')[0]
            if query.get('security')[0] == 'reality':
                proxy['reality-opts'] = {
                    'public-key': query.get('pbk')[0]
                }
                sid = query.get('sid')[0]
                if sid:
                    proxy['reality-opts']['short-id'] = sid
            if query.get('type')[0] == 'ws':
                proxy['ws-opts'] = {
                    'path':query.get('path')[0]
                }
                host = query.get('host')
                if host:
                    proxy['ws-opts']['headers'] = {'Host': host[0]}
            clash_config['proxies'].append(proxy)
            proxy_name_list.append(proxy_name)
        if proxy_type == 'vmess':
            parse = urllib.parse.urlparse(decode_base64_if(proxy_test))
            print(parse)
            if parse.query != '':
                print('非标准格式')
                query = urllib.parse.parse_qs(parse.query)
                info = base64.b64decode(parse.path).decode('utf-8')  # 加密方式:uuid@域名:端口
                print(info)
                for key, value in query.items():
                    query[key] = value[0]
                print(query)
                name = query.get('remarks')
                uuid = info.split('@')[0].split(':')[1]
                server = info.split('@')[1].rsplit(':', 1)[0]
                port = int(info.split('@')[1].rsplit(':', 1)[1])
                aid = int(query.get('alterId'))
                cipher = info.split('@')[0].split(':')[0]
                network = 'ws' if query.get('obfs') == 'websocket' else ''
                tls = query.get('tls')
                pathA = query.get('path')
                host = query.get('obfsParam')
                print(server, port, network, uuid, tls)
            else:
                proxy = eval(parse.path)
                name = proxy['ps']
                uuid = proxy['id']
                server = proxy['add']
                port = int(proxy['port'])
                aid = int(proxy['aid'])
                cipher = proxy['scy']
                network = proxy['net']
                tls = proxy['tls']
                pathA = proxy['path']
                host = proxy['host']
            proxys = {
                'name': name,
                'type': proxy_type,
                'uuid': uuid,
                'server': server,
                'port': port,
                'client-fingerprint': 'chrome',
                'tfo': False,  # 是否启用 TCP Fast Open
                'udp': True,
                'skip-cert-verify': True,  # 是否跳过证书验证
                'alterId': aid,
                'cipher': cipher,
                'network': network,  # 代理的网络类型
                'tls': True if tls else False
            }
            if network == 'ws':
                proxys['ws-opts'] = {
                    'path': pathA,
                }
                if host != '':
                    proxys['ws-opts']['headers'] = {
                        'Host': host
                    }

            clash_config['proxies'].append(proxys)
            proxy_name_list.append(name)
        if proxy_type == 'ss':
            parse = urllib.parse.urlparse(decode_base64_if(proxy_test))
            urlpath = decode_base64_if(parse.path)
            name = urllib.parse.unquote(parse.fragment)
            server = if_ipv6_address(urlpath.split('@')[1].rsplit(':',1)[0])
            port = int(urlpath.split('@')[1].rsplit(':',1)[1])
            cipher = parse.scheme
            password = urlpath.split('@')[0]
            proxy = {
                'name': name,
                'type': proxy_type,
                'server': server,
                'port': port,
                'cipher': cipher,
                'password': password,
                'client-fingerprint':'chrome',
                'tfo':False,
                'udp': True,
                'skip-cert-verify': True
            }
            clash_config['proxies'].append(proxy)
            proxy_name_list.append(name)
        if proxy_type == 'ssr':
            parse = urllib.parse.urlparse(decode_base64_if(proxy_test.replace('-', '+').replace('_', '/')))
            urlpath = decode_base64_if(parse.path)
            print(parse)
            # print(url)
            query = urllib.parse.parse_qs(parse.query)
            name = decode_base64_if(query.get('remarks')[0])
            port = int(urlpath.split(':')[0])
            protocol = urlpath.split(':')[1]
            obfs = urlpath.split(':')[3]
            server = if_ipv6_address(parse.scheme)
            password = decode_base64_if(urlpath.rsplit(':',1)[1].replace('/', ''))
            proxy = {
                'name': name,
                'type': proxy_type,
                'server': server,
                'port': port,
                'protocol':protocol,
                'cipher':'dummy',
                'obfs': obfs,
                'password': password,
                'udp': True,
                'skip-cert-verify': True
            }
            clash_config['proxies'].append(proxy)
            proxy_name_list.append(name)
        if proxy_type == 'trojan':
            parse = urllib.parse.urlparse(decode_base64_if(proxy_test))
            urlpath = decode_base64_if(parse.path)
            print(parse)
            name = urllib.parse.unquote(parse.fragment)
            query = urllib.parse.parse_qs(parse.query)
            password = urlpath.split('@')[0]
            server = if_ipv6_address(urlpath.split('@')[1].rsplit(':',1)[0])
            port = int(urlpath.split('@')[1].rsplit(':',1)[1])
            proxy = {
                'name':name,
                'type':proxy_type,
                'server':server,
                'port':port,
                'password':password,
                'client-fingerprint': 'chrome',
                'udp':True,
                'skip-cert-verify': True
            }
            if query.get('fp'):
                proxy['client-fingerprint'] = query.get('fp')[0]
            if query.get('sni'):
                proxy['sni'] = query.get('sni')[0]
            if query.get('flow'):
                proxy['flow'] = query.get('flow')[0]
            if query.get('type'):
                proxy['network'] = query.get('type')[0]
                if query.get('type')[0] == 'ws':
                    proxy['ws-opts'] = {
                        'path': query.get('path')[0]
                    }
                    host = query.get('host')
                    if host:
                        proxy['ws-opts']['headers'] = {'Host': host[0]}

            clash_config['proxies'].append(proxy)
            proxy_name_list.append(name)
    # 将 Clash 配置转为 YAML 格式
    with open(path + '/db/clash.yaml', 'r') as file:
        data = yaml.safe_load(file)
        data['proxies'] = clash_config['proxies']
        proxy_groups = data.get('proxy-groups')

        for proxy_group in proxy_groups:
            for proxies in proxy_group['proxies']:
                if proxies == 'auto':  # 判断是否包含auto字符串
                    proxy_group['proxies'].remove('auto')
                    for name_list in proxy_name_list:
                        proxy_group['proxies'].append(name_list)
            # print(proxy_group['proxies'])
        # print(data)
        clash_config_yaml = yaml.dump(data, sort_keys=False, allow_unicode=True)
        return clash_config_yaml
@blue.route('/clash_config',methods=['POST']) #clash配置修改
@jwt_required()
def clash_config():
    if request.method == 'POST':
        data = request.get_json()
        index = data.get('index')
        # print(index)
        if index == 'read':
            with open(path + '/db/clash.yaml', 'r') as file:
                return jsonify({
                    'code':200,
                    'msg':file.read()
                })
        if index == 'save':
            text = data.get('text')
            if text == '':
                return jsonify({
                    'code': 400,
                    'msg': '不能为空'
                })
            with open(path + '/db/clash.yaml', 'w') as file:
                file.write(text)
                return jsonify({
                    'code':200,
                    'msg':'保存成功'
                })
@blue.route('/') #前台程序
def get_index():
    return render_template('index.html')
@blue.route('/login',methods=['POST'])
def get_login():
    if request.method == 'POST':
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        user = User.query.filter_by(username=username).first()
        if not user:
            return jsonify({
                'code': 404,
                'msg': '账号不存在'
            })
        if user.username == username and user.password == password:
            access_token = create_access_token(identity=username)
            refresh_token = create_refresh_token(identity=username)
            return jsonify({
                'code': 200,
                'token':access_token,
                'refresh':refresh_token,
                'msg': '登录成功'
            })
        else:
            return jsonify({
                'code':404,
                'msg':'账号或者密码错误'
            })
@blue.route('/refresh' ,methods=['POST']) #刷新令牌
@jwt_required(refresh=True)
def get_refresh():
    if request.method == 'POST':
        current_user = get_jwt_identity()
        if current_user:
            token = create_access_token(current_user)
            return token
        else:
            return '没获取到'
@blue.route('/create_sub',methods=['POST']) # 新建节点
@jwt_required()
def get_create_sub():
    if request.method == 'POST':
        data = request.get_json()
        name = data.get('name')
        nodes = data.get('node')
        print(name,nodes)
        if Sub.query.filter_by(name=name).first():
            return jsonify({
                'code':400,
                'msg':'订阅名字已经存在'
            })
        for i in nodes:
            if len(i.split('|')) >= 2:
                node = i.split('|')[0]
                remarks = i.split('|')[1]
            else:
                node = i
                remarks = ''
            if node != '':
                sub = Sub(name=name, node=node, remarks=remarks)
                try:
                    db.session.add(sub)
                    db.session.commit()
                except Exception as e:
                    db.session.rollback()
                    db.session.flush()
                    return jsonify({
                        'code':400,
                        'msg':'错误信息：' + str(e)
                    })
        return jsonify({
            'code':200,
            'msg':'创建成功'
        })
            # print('节点：' + node)
            # print('备注：' + remarks)
@blue.route('/get_subs',methods=['POST']) #获取所有的订阅
@jwt_required()
def get_subs():
    if request.method == 'POST':
        subs = Sub.query.all()
        data = []
        for sub in subs:
            item = {
                'name':sub.name,
                'node':sub.node,
                'remarks':sub.remarks
            }
            data.append(item)
        return jsonify(data)
@blue.route('/sub/<string:target>/<path:name>',methods=['GET']) #获取指定订阅
def get_sub(target,name):
    if request.method == 'GET':
        def decode_base64_with_emoji(encoded_text):
            # 先解url编码
            encoded_text = urllib.parse.unquote(encoded_text)
            # 将字符串转换为字节流
            byte_text = encoded_text.encode('utf-8')
            # 使用Base64解码字节流
            decoded_bytes = base64.b64decode(byte_text)
            # 将字节流转换为文本
            decoded_text = decoded_bytes.decode('utf-8')
            return decoded_text
        name = decode_base64_with_emoji(name)
        subs = Sub.query.filter_by(name=name).all()
        # print(target, name)
        if not subs:
            return jsonify({
                'code':400,
                'msg':'订阅不存在'
            })

        if target == 'clash':
            data = clash_encode(subs)
            return data
        if target == 'v2ray':
            data = []
            for sub in subs:
                data.append(sub.node)
            encoded_node = base64.b64encode('\n'.join(data).encode('utf-8')).decode('utf-8')
            return encoded_node
@blue.route('/del_sub/<string:name>',methods=['POST']) #删除指定订阅
@jwt_required()
def del_sub(name):
    if request.method == 'POST':
        subs =  Sub.query.filter_by(name=name).all()
        print(name,subs)
        if not subs:
            return jsonify({
                'code': 400,
                'msg': '不存在'
            })
        for sub in subs:
            try:
                db.session.delete(sub)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                db.session.flush()
                return jsonify({
                    'code': 400,
                    'msg': '错误信息:'+str(e)
                })
        return jsonify({
            'code': 200,
            'msg': '删除成功'
        })
@blue.route('/set_sub',methods=['POST']) # 修改节点
@jwt_required()
def get_set_sub():
    remarks = ''
    newNode = ''
    if request.method == 'POST':
        data = request.get_json()
        name = data.get('name')
        newNodes = data.get('newNode')
        subs = Sub.query.filter_by(name=name).all()
        for sub in subs: # 删除表
            try:
                db.session.delete(sub)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                db.session.flush()
                return jsonify({
                    'code': 400,
                    'msg': '错误信息：' + str(e)
                })
        for i in newNodes: #创立表
            if len(i.split('|')) >= 2:
                newNode = i.split('|')[0]
                remarks = i.split('|')[1]
            else:
                newNode = i
                remarks = ''
            if newNode != '':
                sub = Sub(name=name, node=newNode, remarks=remarks)
                try:
                    db.session.add(sub)
                    db.session.commit()
                except Exception as e:
                    db.session.rollback()
                    db.session.flush()
                    return jsonify({
                        'code':400,
                        'msg':'错误信息：' + str(e)
                    })
        return jsonify({
            'code':200,
            'msg':'修改成功'
        })
@blue.route('/set_user',methods=['POST']) # 修改账号信息
@jwt_required()
def get_set_user():
    if request.method == 'POST':
        data = request.get_json()
        username = data.get('username')
        newUserName = data.get('newUserName')
        password = data.get('password')
        user = User.query.filter_by(username=username).first()
        if not user:
            return jsonify({
                'code':400,
                'msg':'账号不正确'
            })
        user.username = newUserName
        user.password = password
        try:
            db.session.commit()
            return jsonify({
                'code': 200,
                'msg': '修改成功'
            })
        except Exception as e:
            db.session.rollback()
            db.session.flush()
            return jsonify({
                'code': 400,
                'msg': '错误信息:'+str(e)
            })
# @blue.route('/decode_sub',methods=['POST']) # 订阅解析
# def decode_sub():
#     if request.method == 'POST':
#         data = request.get_json()
#         urls = data.get('urls')
#         datas = []
#         for url in urls:
#             response = requests.get(url)
#             print(response.status_code)
#             if response.status_code == 200:
#                 datas.append(decode_base64_if(response.text))
#             else:
#                 return jsonify({
#                     'code': response.status_code,
#                     'msg': response.text
#                 })
#         return jsonify({
#             'code': 200,
#             'msg': datas
#         })