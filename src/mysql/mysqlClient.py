# encoding=utf-8
import sys
import MySQLdb
from plus import ReadKeyWord

reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable
conn = MySQLdb.connect(host='localhost', user='root', passwd='toor', db='work', port=3306, charset='utf8')
cursor = conn.cursor()
keyworks = ReadKeyWord()
count=0
for (l, c) in enumerate(keyworks):
    if (l%3==0):
        count=count+1
    group=str(count)
    cursor.execute("INSERT INTO t_keyword(id,keyword,dTaskID) VALUES(" + str( l) + ",'" + c + "'," + group + ")")
conn.commit()
cursor.close()
conn.close()
print "end"
