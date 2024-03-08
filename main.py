from rcon.battleye import Client


SERVER_ADDRESS = ("192.168.50.133", 2310)
PASSWORD = "123456"



with Client('192.168.50.133', 2310, passwd=PASSWORD) as client:
    response = client.run('players')

print(response)
print(type(response))

