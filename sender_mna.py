import csv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import date

#Nombre de la persona que envia el correo
from_addr='SENDER\'S NAME'

#Credenciales
email='ACCOUNT'
password='PASS'

#Lista de correos enviados
list_correos = []

with open('mails.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            #Primera linea
            line_count += 1
        else:
            #Empresa: row[0]
            #Fundador: founder_split
            #Contacto: row[3]
            msg=MIMEMultipart()
			
            #from_addr: Cuenta que envia el correo
            msg['From']=from_addr
            
            #Destinatario: to_addr=[row[3]]
            to_addr=[XXXXX]
            msg['To']=" ,".join(to_addr)
                                   
            #Subject
            msg['subject']='SUBJECT'
            
            #Body
            body='BODY'
            msg.attach(MIMEText(body,'plain'))

            #Envio
            mail=smtplib.SMTP('smtp.gmail.com',587)
            mail.ehlo()
            mail.starttls()
            mail.login(email,password)
            text=msg.as_string()
            mail.sendmail(from_addr,to_addr,text)
            mail.quit()
            
            #Agregar cuenta de correo a nuestra lista
            list_correos.append(str(to_addr))

            #Cuenta la cantidad de cuentas que envio
            line_count += 1


    #string
    string_counter = str(line_count - 1)
    today = str(date.today())

    #Formamos envios.txt
    f= open("envios.txt","w")
    f.write("Fecha: " + today)
    f.write("\nCuenta utilizada: " + email)
    f.write("\nCantidad de envios: " + string_counter)
    f.write("\n===============================\n")
    for i in list_correos:
        f.write(str(i) + "\n")
    f.write("===============================\n")
    f.write("Autor: Mariano Amoroso")
    f.close()     







