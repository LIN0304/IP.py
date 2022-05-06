import socket as s
host=str(input('please input website name:'))+'.com'
#host='github.com'
print(f'IP of {host} is {s.gethostbyname(host)}')