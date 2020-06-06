#coding = utf-8
import connect_db

#程序内部查询用
def select_self(nick):
    sql_list = ["select mix_nick from t_taobao_nick where nick = '%s'"%nick]
    db = connect_db.hd_qa()
    cursor = db.cursor()
    try:
        for i in sql_list:
            cursor.execute(i)
            result = cursor.fetchall()
            return result[0][0]
    except Exception as e:
        return 'nick不存在或输入有误~'
        db.rollback()
    else:
        db.commit()
        cursor.close()
        db.close()

#删除领卡有礼数据
def member_card(mix_nick,shop_id):
    sql_list = ["delete from t_membership_log where nick = '%s' AND shop_id = '%s'" %(mix_nick,shop_id)]
    db = connect_db.hd_qa()
    cursor = db.cursor()
    try:
        for i in sql_list:
            cursor.execute(i)
    except Exception as e:
        return 'nick不存在或输入有误~'
        db.rollback()
    else:
        db.commit()
        cursor.close()
        db.close()

#删除新/旧邀请领卡有礼被邀请人数据
def invite_collar_card(mix_nick):
    sql_list = ["UPDATE t_mall_ccgroup_log SET user_type = 1 WHERE user_type = 0 and  mix_nick = '%s'" %(mix_nick)]
    db = connect_db.hd_qa()
    cursor = db.cursor()
    try:
        for i in sql_list:
            cursor.execute(i)
    except Exception as e:
        return 'nick不存在或输入有误~'
        db.rollback()
    else:
        db.commit()
        cursor.close()
        db.close()