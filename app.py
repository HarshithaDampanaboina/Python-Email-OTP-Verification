import random           #This module helps to generate random numbers accordingly
import smtplib          #The library is intact to send the Emails and have lot of methods which are predefined


otp = str(random.randint(100000, 999999))    #By creating a OTP variable I have choosen to randomly pic the int using the random module by giving range which cotains only 6-digits
smtp_server = 'smtp.gmail.com'               #This is the address of the server which is responsible to send the mails
smtp_port = 587                              #The port is used for communication with the server SMTP
sender_email = 'harshitha3920@gmail.com'


user_email =input( "Enter your E-Mail ID : " )
smtp_connection = smtplib.SMTP( smtp_server, smtp_port )
smtp_connection.starttls( )                              #for secure purpose


login_credentials= smtp_connection.login( sender_email, 'nhil vvxw uszh eywa' )   #This is the another method used for getting loggedin successfully by providing mail and the apppas

if login_credentials[0] ==235:
    message = f'Subject: OTP Verification\n\nYour OTP is: {otp}'
    smtp_connection.sendmail(sender_email, user_email, message)   #The method used to convey the message to send
    print( "OTP has been sent to your email." )

else:
    print( "Error occurred while sending OTP. Authentication failed." )

max_attempts = 3
attempt = 1

while attempt <= max_attempts:
    user_input = input( "Enter the OTP received in your email: " )

    if user_input == otp:
        print( "Access Granted Successfully!" )
        break

    else:

        print("Access Denied. Incorrect OTP.")

        if attempt < max_attempts:
            print(  f"Remaining attempts: { max_attempts - attempt }" )
            attempt += 1

        else:
            print( "Maximum attempts reached. Please try again later." )
            break
smtp_connection.quit( )
