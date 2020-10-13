## 介绍
pydivert可以拦截PC端的网络请求
这里demo是用flask起个服务返回hello word，用pyfivert进行拦截并篡改数据，讲hello word篡改为hello hacker

## 使用
### 安装环境
pip install -r req .txt

### 正常使用
运行server.py文件，访问http://127.0.0.1:5000，返回hello word

### 拦截篡改
运行server.py的同时再运行tamper.py文件，然后再次访问http://127.0.0.1:5000，返回hello hacker，篡改成功