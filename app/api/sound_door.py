import random

from app.api.utils import connect_to_mysql

# 1 false 0 true
def main_sound(*params, number, area):
    con = connect_to_mysql()
    cursor = con.cursor()
    if number == 1:
        count = len(params)
        if count == 1:
            # 有记录的人
            sql = 'select * from user_base where id="%s"' % (params[0])
            cursor.execute(sql)
            row = cursor.fetchone()
            if row[5] == 0:
                pass # 直接开门
                return
            else:
                if row[7] == 1:  # 没有权限  XXX,欢迎光临, 请稍等,马上通知为你开门
                    sql = 'select * from welcomesound where one_or_more = "1" and open_status = "1" and stranger_status = "1"'
                    cursor.execute(sql)
                    sound = cursor.fetchone()
                    sound_url = [row[4], sound[2]]
                    sound_name = [row[6], sound[3]]
                    sound_number = [1, 2]
                else: # 有权限  XXX,欢迎光临, 请稍等,马上为你开门
                    sql = 'select * from welcomesound where one_or_more = "1" and open_status = "0" and super_status = "0"'
                    cursor.execute(sql)
                    sounds = cursor.fetchall()
                    sound = random.choice(sounds)
                    sound_url = [row[4], sound[2]]
                    sound_name = [row[6], sound[3]]
                    sound_number = [1, 2]
        else:
            # 一个人 陌生人    #  欢迎光临, 请稍等,马上通知为你开门
            sql = 'select * from welcomesound where one_or_more = "1" and open_status = "1" and stranger_status = "0"'
            cursor.execute(sql)
            sound = cursor.fetchone()
            sound_url = sound[2]
            sound_name = sound[3]
            sound_number = [1]
    elif number == 2:
        count = len(params)
        if count == 2: # 两个熟人
            sql1 = 'select * from user_base where id="%s"' % (params[0])
            sql2 = 'select * from user_base where id="%s"' % (params[1])
            cursor.execute(sql1)
            row1 = cursor.fetchone()
            cursor.execute(sql2)
            row2 = cursor.fetchone()
            if row1[5] == 0 and row2[5] == 0:  # 全部接待
                pass  # 直接开门
                return
            else:
                if row1[7] == 1 and row2[7] == 1:
                    sql = 'select * from welcomesound where one_or_more = "2" and open_status = "0" and stranger_status = "1" and super_status = "0"'
                    cursor.execute(sql)
                    sounds = cursor.fetchall()
                    sound = random.choice(sounds)
                    if row1[3] != row2[3]:  # 职位不同
                        if row1[6] != row1[6]:  # 音频不同
                            position_sql1 = 'select * from position where id="%s"' % (row1[3])
                            position_sql2 = 'select * from position where id="%s"' % (row2[3])
                            cursor.execute(position_sql1)
                            position_row1 = cursor.fetchone()
                            cursor.execute(position_sql2)
                            position_row2 = cursor.fetchone()
                            if position_row1[2] < position_row2[2]:  # 1的权限大于2

                                sound_url = [row1[4], row2[4], sound[2]]
                                sound_name = [row1[6], row2[6], sound[3]]
                                sound_number = [1, 2, 3]
                            else:  # 1的权限小于2
                                sound_url = [row2[4], row1[4], sound[2]]
                                sound_name = [row2[6], row1[6], sound[3]]
                                sound_number = [1, 2, 3]
                        else:  # 音频相同
                            position_sql1 = 'select * from position where id="%s"' % (row1[3])
                            position_sql2 = 'select * from position where id="%s"' % (row2[3])
                            cursor.execute(position_sql1)
                            position_row1 = cursor.fetchone()
                            cursor.execute(position_sql2)
                            position_row2 = cursor.fetchone()
                            if position_row1[2] < position_row2[2]:  # 1的权限大于2
                                userdouble_sql = 'select * from user_double where position_id = "%s"' % (row1[3])
                                cursor.execute(userdouble_sql)
                                userdouble = cursor.fetchone()
                                sound_url = [userdouble[3], sound[2]]
                                sound_name = [userdouble[2], sound[3]]
                                sound_number = [1, 2]
                            else:  # 1的权限小于2
                                userdouble_sql = 'select * from user_double where position_id = "%s"' % (row2[3])
                                cursor.execute(userdouble_sql)
                                userdouble = cursor.fetchone()
                                sound_url = [userdouble[3], sound[2]]
                                sound_name = [userdouble[2], sound[3]]
                                sound_number = [1, 2]
                    else:  # 职位相同
                        if row1[6] != row1[6]:  # 音频不同
                            sound_url = [row1[4], row2[4], sound[2]]
                            sound_name = [row1[6], row2[6], sound[3]]
                            sound_number = [1, 2, 3]
                        else:  # 音频相同
                            userdouble_sql = 'select * from user_double where position_id = "%s"' % (row1[3])
                            cursor.execute(userdouble_sql)
                            userdouble = cursor.fetchone()
                            sound_url = [userdouble[3], sound[2]]
                            sound_name = [userdouble[2], sound[3]]
                            sound_number = [1, 2]
                elif row1[7] != 1 and row2[7] != 1:  # 没有权限  XXX,XXX,欢迎光临, 请稍等,马上通知为你开门
                    sql = 'select * from welcomesound where one_or_more = "2" and open_status = "1" and stranger_status = "1"'
                    cursor.execute(sql)
                    sound = cursor.fetchone()
                    if row1[3] != row2[3]:  # 职位不同
                        if row1[6] != row1[6]:  # 音频不同
                            position_sql1 = 'select * from position where id="%s"' % (row1[3])
                            position_sql2 = 'select * from position where id="%s"' % (row2[3])
                            cursor.execute(position_sql1)
                            position_row1 = cursor.fetchone()
                            cursor.execute(position_sql2)
                            position_row2 = cursor.fetchone()
                            if position_row1[2] < position_row2[2]:  # 1的权限大于2

                                sound_url = [row1[4], row2[4], sound[2]]
                                sound_name = [row1[6], row2[6], sound[3]]
                                sound_number = [1, 2, 3]
                            else:  # 1的权限小于2
                                sound_url = [row2[4], row1[4], sound[2]]
                                sound_name = [row2[6], row1[6], sound[3]]
                                sound_number = [1, 2, 3]
                        else:  # 音频相同
                            position_sql1 = 'select * from position where id="%s"' % (row1[3])
                            position_sql2 = 'select * from position where id="%s"' % (row2[3])
                            cursor.execute(position_sql1)
                            position_row1 = cursor.fetchone()
                            cursor.execute(position_sql2)
                            position_row2 = cursor.fetchone()
                            if position_row1[2] < position_row2[2]:  # 1的权限大于2
                                userdouble_sql = 'select * from user_double where position_id = "%s"' % (row1[3])
                                cursor.execute(userdouble_sql)
                                userdouble = cursor.fetchone()
                                sound_url = [userdouble[3], sound[2]]
                                sound_name = [userdouble[2], sound[3]]
                                sound_number = [1, 2]
                            else:  # 1的权限小于2
                                userdouble_sql = 'select * from user_double where position_id = "%s"' % (row2[3])
                                cursor.execute(userdouble_sql)
                                userdouble = cursor.fetchone()
                                sound_url = [userdouble[3], sound[2]]
                                sound_name = [userdouble[2], sound[3]]
                                sound_number = [1, 2]
                    else:  # 职位相同
                        if row1[6] != row1[6]:  # 音频不同
                            sound_url = [row1[4], row2[4], sound[2]]
                            sound_name = [row1[6], row2[6], sound[3]]
                            sound_number = [1, 2, 3]
                        else:  # 音频相同
                            userdouble_sql = 'select * from user_double where position_id = "%s"' % (row1[3])
                            cursor.execute(userdouble_sql)
                            userdouble = cursor.fetchone()
                            sound_url = [userdouble[3], sound[2]]
                            sound_name = [userdouble[2], sound[3]]
                            sound_number = [1, 2]
                else:   # 一个有权限  XXX XXX,欢迎光临, 请稍等,马上为你们开门
                    sql = 'select * from welcomesound where one_or_more = "2" and open_status = "0" and stranger_status = "1"'
                    cursor.execute(sql)
                    sound = cursor.fetchone()
                    if row1[3] != row2[3]:  # 职位不同
                        if row1[6] != row1[6]:  # 音频不同
                            position_sql1 = 'select * from position where id="%s"' % (row1[3])
                            position_sql2 = 'select * from position where id="%s"' % (row2[3])
                            cursor.execute(position_sql1)
                            position_row1 = cursor.fetchone()
                            cursor.execute(position_sql2)
                            position_row2 = cursor.fetchone()
                            if position_row1[2] < position_row2[2]:  # 1的权限大于2

                                sound_url = [row1[4], row2[4], sound[2]]
                                sound_name = [row1[6], row2[6], sound[3]]
                                sound_number = [1, 2, 3]
                            else:  # 1的权限小于2
                                sound_url = [row2[4], row1[4], sound[2]]
                                sound_name = [row2[6], row1[6], sound[3]]
                                sound_number = [1, 2, 3]
                        else:  # 音频相同
                            position_sql1 = 'select * from position where id="%s"' % (row1[3])
                            position_sql2 = 'select * from position where id="%s"' % (row2[3])
                            cursor.execute(position_sql1)
                            position_row1 = cursor.fetchone()
                            cursor.execute(position_sql2)
                            position_row2 = cursor.fetchone()
                            if position_row1[2] < position_row2[2]:  # 1的权限大于2
                                userdouble_sql = 'select * from user_double where position_id = "%s"' % (row1[3])
                                cursor.execute(userdouble_sql)
                                userdouble = cursor.fetchone()
                                sound_url = [userdouble[3], sound[2]]
                                sound_name = [userdouble[2], sound[3]]
                                sound_number = [1, 2]
                            else:  # 1的权限小于2
                                userdouble_sql = 'select * from user_double where position_id = "%s"' % (row2[3])
                                cursor.execute(userdouble_sql)
                                userdouble = cursor.fetchone()
                                sound_url = [userdouble[3], sound[2]]
                                sound_name = [userdouble[2], sound[3]]
                                sound_number = [1, 2]
                    else:  # 职位相同
                        if row1[6] != row1[6]:  # 音频不同
                            sound_url = [row1[4], row2[4], sound[2]]
                            sound_name = [row1[6], row2[6], sound[3]]
                            sound_number = [1, 2, 3]
                        else:  # 音频相同
                            userdouble_sql = 'select * from user_double where position_id = "%s"' % (row1[3])
                            cursor.execute(userdouble_sql)
                            userdouble = cursor.fetchone()
                            sound_url = [userdouble[3], sound[2]]
                            sound_name = [userdouble[2], sound[3]]
                            sound_number = [1, 2]

        elif count == 1:  # 一个熟人 一个陌生人
            sql = 'select * from user_base where id="%s"' % (params[0])
            cursor.execute(sql)
            row = cursor.fetchone()
            if row[7] == 1:
                if row[5] == 0: # 两个人, 一个熟人, 接待过, 没有权限, 通知接待   你们好,马上通知XXX为你们开门
                    sql = 'select * from welcomesound where one_or_more = "3" and open_status = "1"'
                    cursor.execute(sql)
                    sound = cursor.fetchone()
                    sound_url = [sound[2]]
                    sound_name = [sound[3]]
                    sound_number = [1]
                else: # 两个人, 一个熟人, 未接待, 没有权限, 通知接待     XXX  你好,马上通知XXX为你们开门
                    sql = 'select * from welcomesound where one_or_more = "2" and open_status = "1"'
                    cursor.execute(sql)
                    sound = cursor.fetchone()
                    sound_url = [row[4], sound[2]]
                    sound_name = [row[6], sound[3]]
                    sound_number = [1, 2]
            else:  # 有权限  xxx , 又带新朋友过来了
                sql = 'select * from welcomesound where one_or_more = "2" and open_status = "0" and stranger_status = "0"'
                cursor.execute(sql)
                sound = cursor.fetchone()
                sound_url = [row[4], sound[2]]
                sound_name = [row[6], sound[3]]
                sound_number = [1, 2]

        else:  # 都是陌生人 你们好,正在通知XXX给你们开门
            sql = 'select * from welcomesound where one_or_more = "3" and open_status = "1"'
            cursor.execute(sql)
            sound = cursor.fetchone()
            sound_url = [sound[2]]
            sound_name = [sound[3]]
            sound_number = [1]
    elif number >= 3:
        row_status = []
        row_super = []
        for i in params:
            user_sql = 'select * from user_base where id = "%s"' % (i)
            cursor.execute(user_sql)
            row = cursor.fetchone()
            row_status.append(row[5])
            row_super.append(row[7])
        if len(params) == number:
            if 1 in row_status:
                if 0 in row_super:
                    sql = 'select * from welcomesound where one_or_more = "3" and  open_status = "0"'
                    cursor.execute(sql)
                    sound = cursor.fetchone()
                else:
                    sql = 'select * from welcomesound where one_or_more = "3" and  open_status = "1"'
                    cursor.execute(sql)
                    sound = cursor.fetchone()
            else:
                pass  # 直接开门
                return
        else:
            if 0 in row_super:
                sql = 'select * from welcomesound where one_or_more = "3" and  open_status = "0"'
                cursor.execute(sql)
                sound = cursor.fetchone()
            else:
                sql = 'select * from welcomesound where one_or_more = "3" and  open_status = "1"'
                cursor.execute(sql)
                sound = cursor.fetchone()
        sound_url = sound[2]
        sound_name = sound[3]
        sound_number = [1]
    # 喇叭
    loudspeaker_sql = 'select * from loudspeaker where area = "%s"' % (area)
    cursor.execute(loudspeaker_sql)
    loudspeaker_row = cursor.fetchone()
    # 拼写任务名称
    data_name = ''
    for j in sound_name:
        data_name += j

    data = {
        "id": 0,  # 任务唯一标识（>=1，添加任务时为 0)
        "en": 1,  # 任务是否可用（开启 1，关闭 0）
        "exe": 0,  # 任务运行状态（运行中 1，空闲 0）
        "name": data_name,  # 任务名称
        "mode": 0,  # 任务广播方式（单播为 0，组播为 1）
        "dur": 0,  # 延迟时间（秒）
        "power": 0,  # 用户的任务级别
        "user": 1,  # 指定播放次数（默认为 1 次）
        "lv": 99,  # 任务优先级别(11-100)，数值越小，优先级别 越大。
        "btime": 4294967295,
        "rule": 2,  # 任务执行规则（每天为 0，每周为 1，手动为 2)
        "bdate": 1554134400,  # 任务开始日期，一般为任务创建日期
        "edate": 4294967295,  # 任务结束日期，一直有效为-1
        "week": 0,  # 每周执行规则，rule 为 1 时，有效
        "type": 1,  # 任务类型，定时任务为 1
        "src_type": 0,
        "em": 52685,
        "ev": 0,
        "emm": 52685,
        "emv": 205,
        "elm": 52685,
        "elv": 205,
        "ei": 0,
        "echannel": 0,
        "SchemeID": 0,
        "prule": 0,
        "mgr": 52685,
        "sample": 32000,  # 任务音频源类型为采集时，指定采集质量（8000、16000、32000）
        "voice": 0,
        "instime": 1,
        "isins": 0,
        "ps": 0,  # 任务播放状态（空闲 0、播放中 1、暂停 2）
        "exec": [],  # 任务执行时间列表，详情查看任务运行时间列表数据类型
        "i": 100,  # 当前任务播放音频文件标识
        "files": [],
        "vol": 80,  # 任务指定音量
        "terminals": [  # 播放终端 ID 列表
            {
                "i": loudspeaker_row[2],
                "vol": -1
            }
        ]
    }
    for i in sound_number:
        i_index = i - 1
        item = {
            "i": i,  # ID
            "n": sound_url[i_index].replace('/', '\\'),  # 音频文件在服务器绝对路径
            "t": 269,  # 音频文件持续时间（秒）
            "rule": 4319669  # 文件大小
        }
        data['files'].append(item)