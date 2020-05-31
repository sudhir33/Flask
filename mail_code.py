import smtplib


server=smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login("yourmail@gmail.com","password")
message="""\
subject:

https://adityagroup-my.sharepoint.com/:v:/g/personal/sudhir_technicalhub_io/ETqT2LZeMxdCpIRlOqvGlOoBzPryaNsZEIDnJTRb4XbJYg?e=gbQlme

"""
server.sendmail(cren[0],"sudhir@technicalhub.io",message)

