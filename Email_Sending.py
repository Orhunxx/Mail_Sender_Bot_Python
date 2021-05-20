import smtplib

mail = "youremail@gmail.com"
password = "yourpassword"

mail_server = smtplib.SMTP("smtp.gmail.com", 587) # smtp.gmail.com is server and 587 is port. You can choose 465 or 2525 too
mail_server.starttls()  #starts security protocol

mail_server.login(mail, password) #login to mail


message = "Example message"

receiever = mail

mail_server.sendmail(mail, receiever,message)
print("Mail sent")
