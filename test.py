import os

lalala = os.popen('echo "oiiii" >> oie.txt && cat oie.txt')
lululu = lalala.read()
uuu = 'alooooo'
print(lululu)
print(uuu)
print('uiiii')

def menu():
    print('issoai 1\naquilola 2\nselecione:')
    choice = input('')
    print('oi' + choice + 'oii')
    if choice == '1':
        fazissoai()
    if choice == '2':
        fazaquilola()
    else:
        print('o seu nescio, voce nao selecionou algo valido')
        menu()

def fazissoai():
    li = os.popen('echo aiaiai')
    print(li)

def fazaquilola():
    la = os.popen('echo nao aquilo nao')
    print(la)

menu()
