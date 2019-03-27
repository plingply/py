
python3 manage.py runserver 127.0.0.1:8009

python mpy/manage.py inspectdb  会按照你的数据库生成Model  拷贝进去用就可以了!

uwsgi --http 127.0.0.1:9999 --file /www/wwwroot/py/mpy --static-map=/www/wwwroot/py/mpy=static

uwsgi --http :8001 --chdir /www/wwwroot/py/mpy --module mpy.wsgi

server {
    listen      80;
    server_name www.ziqiangxuetang.com;
    charset     utf-8;
 
    client_max_body_size 75M;
 
 
    location /static {
        alias /www/wwwroot/py/mpy/static;
    }
 
    location / {
        uwsgi_pass  unix:///home/tu/zqxt/zqxt.sock;
        include     /etc/nginx/uwsgi_params;
    }
}

server {
    listen 80;   # 监听的端口
    server_name    jung.wang;  # 配置域名
    charset        utf-8;   # 字符集

    client_max_body_size    75M;  # 客户端请求发送的内容最大不要超过多少M

# 指定静态文件路径
    location /static {
        alias    /var/www/MySpace/static;
    }

# 指定项目路径uwsgi
# 这个location就和咱们Django的url类似,
    location / {
        uwsgi_pass     django;
        include        /var/www/MySpace/uwsgi_params;  # 导入一个Nginx模块他是用来和uWSGI进行通讯的
    }
}
