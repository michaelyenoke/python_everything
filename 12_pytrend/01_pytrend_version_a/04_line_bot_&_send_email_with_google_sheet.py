###### section 01 ######

##########
#Line Bot#
##########

###### section 02 ######

#############
#寄送電子郵件#
#############

import smtplib

#mySMTP = smtplib.SMTP('smtp.gmail.com',587)
#print(type(mySMTP))
#mySMTP.ehlo() # 250 代表成功,啟動伺服器對話
#mySMTP.starttls() # 220 代表成功,告知郵件伺服器郵件加密

#mySMTP.login('michaelyenoke@gmail.com','2ouiougi')


s = smtplib.SMTP('smtplib.gmail.com',587)
s.ehlo()
s.starttls()
s.login('michaelyenoke@gmail.com','zaleoc2ouiougi')
try:
    s.sendmail('michaelyenoke@gmail.com','michaelyenoke@hotmail.com','message_hihi')
except:
    print (failed)
    



