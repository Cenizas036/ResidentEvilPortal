import mysql.connector as sqltor
mc=sqltor.connect(host="localhost",user="root",passwd="Lol*1234",database="login")
c1=mc.cursor()
st="select * from login where USERNAME= '{}'".format("User1234")
c1.execute(st)
n=c1.fetchall()
print(n)
mc.close()
