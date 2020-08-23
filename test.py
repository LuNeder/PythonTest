import os

lalala = os.popen('echo "oiiii" >> oie.txt && cat oie.txt')
lululu = lalala.read()
uuu = 'alooooo'
print(lululu)
print(uuu)
print('uiiii')

def fazissoai():
	li = os.system('echo aiaiai')
	print(li)

def fazaquilola():
	la = os.system('echo nao aquilo nao')
	print(la)



def menu():

	print('issoai 1\naquilola 2\nselecione:')

	choice = input('')

	print('oi' + choice + 'oii')

	if choice == '1':
		fazissoai()

	elif choice == '2':
		fazaquilola()

	else:
		print('o seu nescio, voce nao selecionou algo valido')
		menu()



menu()
