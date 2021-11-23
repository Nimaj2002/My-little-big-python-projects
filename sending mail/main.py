import smtplib

my_mail = "n5jelodari@gmail.com"
my_pass = "n!ma123456789"


def Factorial(N):
    N = int(N)
    fac = 1
    if N == 0:
        fac = 1
        return fac
    elif N < 0:
        return "invalid!"
    else:
        while N != 1:
            fac = N * fac
            N -= 1
        return fac


result = Factorial(input())

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_mail, password=my_pass)
connection.sendmail(from_addr=my_mail, to_addrs="nimajelodari2002@gmail.com", msg=f"{result}")
connection.close()

print(f"{result}")
