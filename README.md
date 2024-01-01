#拉取docker镜像

```docker pull jaaksi/sublink:latest```

#启动docker

```docker run -p 5000:5000 -d jaaksi/sublink:latest```

如果要自定义端口 -p 5000:5000左边的5000改成自定义右边为固定如:8000:5000

那么公网加8000端口即可访问

#clash配置说明：

目前适配了vless,vmess,ssr,ss协议，其中vmess中的传输只支持ws和默认，vless则是reality

这些并未测试使用，如果发现连接无效问题请找我反馈

#clash规则说明：

我提供了一个默认带分流规则，提供了策略组变量：auto，在proxy-groups下面的proxies写上auto可自动获取节点名称

本人电报联系和投喂：@toutie_1




