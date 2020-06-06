#coding = utf-8
#Author:zhouyou
#date:"2020/5/30 17:35"
from flask import Flask,render_template,request
import connect_db,execute
import traceback
import time
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

#页面查询功能用
@app.route('/select')
def select():
    sql_list = ["select mix_nick from t_taobao_nick where nick = ('" + request.args.get('nick') + "')"]
    db = connect_db.hd_qa()
    cursor = db.cursor()
    try:
        for i in sql_list:
            cursor.execute(i)
            result = cursor.fetchall()
        content = '查询结果是：'
        return render_template('index.html',content = content,result = result[0][0])
    except Exception as e:
        return render_template('index.html',content ='nick不存在或输入有误~')
        db.rollback()
    else:
        db.commit()
        cursor.close()
        db.close()

@app.route('/clear')
def clear():
    nick = request.args.get('nick')
    mix_nick = execute.select_self(nick)
    print("mix_nick========",mix_nick)
    ac_type = request.args.get('ac_type')
    shop_id = request.args.get('shop_id')
    # if ac_type == 'MEMBERSHIP_CARD':
    #     execute.member_card(mix_nick,shop_id)
    switch = {
        'MEMBERSHIP_CARD':lambda :execute.member_card(mix_nick,shop_id),
        'INVITE_MEMBERSHIP':lambda :execute.invite_collar_card(mix_nick)
    }
    switch[ac_type]()
    return render_template('index.html')

@app.route('/hd_user_db')
def hd_user_db():
    phone = request.args.get('phone')
    nick = request.args.get('nick')
    sql_list = ["DELETE from tb_user_plat_relation where mobile = '%s'"%phone,\
                "DELETE from tb_user where member_mobile = '%s'"%phone,\
                "DELETE from t_account_bind_log where mobile = '%s'"%phone, \
                "DELETE FROM t_mall_user_info where nick = '%s'"%nick, \
                "DELETE FROM t_taobao_nick where nick = '%s'"%nick]
    db = connect_db.hd_qa()
    cursor = db.cursor()
    try:
        for i in sql_list:
            cursor.execute(i)
    except Exception as e:
        db.rollback()
    else:
        db.commit()
        cursor.close()
        db.close()
        return render_template('index.html')

@app.route('/clear_lp3')
def clear_lp3():
    id = request.args.get('lp3_id')
    sql_list = ["DELETE FROM t_m_member where tenant_id='qiushi6' and id='%s'"%id,\
                "DELETE FROM t_m_member_grade where tenant_id='qiushi6' and member_id='%s'"%id,\
                "DELETE FROM t_m_mem_grade_record where tenant_id='qiushi6' and member_id='%s'"%id,\
                "DELETE FROM t_m_member_point where tenant_id='qiushi6' and member_id='%s'"%id,\
                "DELETE FROM t_m_mem_point_record where tenant_id='qiushi6' and member_id='%s'"%id,\
                "DELETE FROM t_m_mem_point_rec_fast where tenant_id='qiushi6' and member_id='%s'"%id,\
                "DELETE FROM t_m_plat_member_log where tenant_id='qiushi6' and member_id='%s'"%id,\
                "DELETE FROM t_m_plat_member where member_id = '%s'"%id
                ]
    db = connect_db.lp3_db()
    cursor = db.cursor()
    try:
        for i in sql_list:
            print(i)
            rs = cursor.execute(i)
            print("执行结果------",rs)
    except Exception as e:
        db.rollback()
    else:
        db.commit()
        cursor.close()
        db.close()
        return render_template('index.html')

if __name__ == '__main__':
    # app.run(host, port, debug, options)
    # 默认值：host=127.0.0.1, port=5000, debug=false
    app.run(host='172.19.0.199',port=5005, debug='false')