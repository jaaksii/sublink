#拉取docker镜像

```docker pull jaaks/sublink:latest```

#启动docker

```docker run -p 5000:5000 -d jaaks/sublink:latest uwsgi --ini uwsgi.ini```

然后你的公网加5000端口即可访问

