f=open(r'c:\users\lab02\Desktop\teste.txt')

for linha in f.readlines():
    print(linha.strip())
    
f.close()
