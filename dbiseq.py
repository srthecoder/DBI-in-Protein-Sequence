#!C:/Users/Swachandrika/AppData/Local/Programs/Python/Python39/python.exe
import cgi
# create instance of fieldStorage
form = cgi.FieldStorage()
import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    port = "3307",
    user = "root",
    password = "root",
    database = "mydb"
)
# get data from fields
n = form.getvalue('name')
if form.getvalue("seq"): seq = form.getlist("seq")
else:seq = "Not entered!"
raw = seq1 =""
import re
for i in seq:
    if re.match('^>', i): continue
    elif re.match('^\s*$',i): continue
    elif re.match('^#',i): continue
    else: raw += i

rawseq = re.sub("\s","",seq)

rawseq = ''.join(seq1)
rawseq = re.sub("[\s\d]","",rawseq)
l = len(rawseq)

import Bio.SeqUtils.ProtParam
mw = Bio.SeqUtils.molecular_weight(rawseq, seq_type ="")

a = ''.join(raw)
acc = re.findall('^>.+\.[1-9]\s',a)
acc = "".join(acc)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE seqInfo(AccessionID varchar(250), sequence varchar(200),Length int, molwt int)")

print("Content-type:text/html\r\n\r\n")
print("<html><body>")
print("<h4> Thank You!</h4>")
sql=("INSERT INTO seqInfo VALUES (%s,%s,%s,%s)")
val=(acc, rawseq, l, mw)
mycursor.execute(sql,val)
mydb.commit()
print("</body></html>")
print("Record inserted.")
