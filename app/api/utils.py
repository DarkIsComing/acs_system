import pymysql


def connect_to_mysql():
    con=pymysql.connect(host='192.168.10.191',port=3306,user='root',password='116116',database="zhanting",charset='utf8')
    return con