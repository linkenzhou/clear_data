#coding = utf-8
#Author:zhouyou
#date:"2020/5/30 17:32"
import pymysql
from sshtunnel import SSHTunnelForwarder

name = "you.zhou"
passwd = "youZHOU20150130"


def hd_qa():
    ssh_server = SSHTunnelForwarder(
        # 中间服务器地址
        ssh_address_or_host=("192.168.175.144", 22),
        ssh_username=name,
        ssh_password=passwd,
        remote_bind_address=('pc-k2jvrk176f5418as0.rwlb.zhangbei.rds.aliyuncs.com', 3306)
    )
    # 启动ssh实例，后续的MySQL网络连接都将在这个环境下运行。
    ssh_server.start()

    db = pymysql.connect(host = '127.0.0.1',user = 'iam',password = 'iam123456',database = 'iam',port = ssh_server.local_bind_port)
    return db
    # cursor = db.cursor()
    # cursor.execute(sql)
    # db.commit()


def lp3_db():
    ssh_server = SSHTunnelForwarder(
        # 中间服务器地址
        ssh_address_or_host=("192.168.175.144", 22),
        ssh_username=name,
        ssh_password=passwd,
        remote_bind_address=('pc-k2jvrk176f5418as0.rwlb.zhangbei.rds.aliyuncs.com', 3306)
    )
    # 启动ssh实例，后续的MySQL网络连接都将在这个环境下运行。
    ssh_server.start()
    db = pymysql.connect(host = '127.0.0.1',user = 'shuyun_admin',password = 'Hdv62GVkKc',database = 'loyalty2_qiushi6',port = ssh_server.local_bind_port)
    return db
    # cursor = db.cursor()
    # cursor.execute()
    # db.commit()