# 更新说明：
新增节点国旗自动插入

支持填写订阅节点让其动态解析而不是直接解析出节点

新增订阅解析器

# 功能说明：
![Alt Text](web/readme/1.png)
![Alt Text](web/readme/2.png)

节点转换成订阅，并且能够一直存储

方便多订阅管理，个人搭建使用

解决安全问题预防被偷节点,集成前后端

目前支持v2ray|clash|surge

v2ray格式通用的软件已测有下:v2rayn 小火箭等，还有一些没用过不知名

默认账户密码都是admin，请记得修改否则被扫端口容易泄漏

本人是自学前后端没多久的小白，希望口下留情

# 安装说明：

## 启动docker

进入到你的目录比如你可以创建一个sublink目录然后输入

```
docker run --name sublink -p 8000:5000 \
-v $PWD/db:/app/app/db \
-e PORT=5000 \
-d jaaksi/sublink
```

如果要自定义端口 -p 5000:5000左边的5000改成自定义右边为固定如:8000:5000

那么ip加8000端口即可访问

# 假如你忘记了账号或者密码

初始化为admin，确保你的容器在运行的时候终端执行以下命令：

    docker exec -it sublink bash -c "python init_user_pw.py; exit"

本人电报联系：@toutie_1

电报群组:https://t.me/+u6gLWF0yP5NiZWQ1

USDT打赏：

![Alt Text](readme/img.png)

