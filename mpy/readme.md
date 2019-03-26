
python3 manage.py runserver 127.0.0.1:8009

python mpy/manage.py inspectdb  会按照你的数据库生成Model  拷贝进去用就可以了!

uwsgi --http 127.0.0.1:9999 --file /www/wwwroot/py/mpy --static-map=/static=static