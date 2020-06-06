#coding = utf-8
#Author:zhouyou
#date:"2020/5/30 17:32"
import redis

conn = redis.Redis(host='192.168.172.248',port=6379,password='wentjiang',)


print(conn.get("HD:JOIN:FAVORITE106878997|l01L7UHnQwMDKgxfegMnw9CqcxKoR7RntZLcAuSKyUkMIY=|"))
print(conn.get("HD:JOIN:FAVORITE106878997|信01b2utc1DSovUoihuwFf0MGcG0miwTeaF1vSjvj2SncIo=|"))

print(conn.delete("HD:JOIN:FAVORITE106878997|l01L7UHnQwMDKgxfegMnw9CqcxKoR7RntZLcAuSKyUkMIY=|"))
print(conn.delete("HD:JOIN:FAVORITE106878997|信01b2utc1DSovUoihuwFf0MGcG0miwTeaF1vSjvj2SncIo=|"))


print(conn.get('HD:JOIN:MEMBERSHIP_CARD106878997|信01b2utc1DSovUoihuwFf0MGcG0miwTeaF1vSjvj2SncIo=|'))
print(conn.get('HD:JOIN:MEMBERSHIP_CARD122564515|信01b2utc1DSovUoihuwFf0MGcG0miwTeaF1vSjvj2SncIo=|'))

conn.delete('HD:JOIN:MEMBERSHIP_CARD106878997|信01b2utc1DSovUoihuwFf0MGcG0miwTeaF1vSjvj2SncIo=|')
conn.delete('HD:JOIN:MEMBERSHIP_CARD122564515|信01b2utc1DSovUoihuwFf0MGcG0miwTeaF1vSjvj2SncIo=|')
conn.delete('getNicksd12信01b2utc1DSovUoihuwFf0MGcG0miwTeaF1vSjvj2SncIo=|')

conn.delete('HD:JOIN:MEMBERSHIP_CARD106878997|t01HFeEK0rU5TEhkuNZzVRow9Rb2UrFTSalpnV4jMR1Fgo=|')
conn.delete('HD:JOIN:MEMBERSHIP_CARD122564515|t01HFeEK0rU5TEhkuNZzVRow9Rb2UrFTSalpnV4jMR1Fgo=|')
conn.delete('HD_INTERACTIVE31067011|')