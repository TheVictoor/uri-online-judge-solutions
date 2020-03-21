#dicionario com os valores de cada codigo
cod = {'=.===' : 'a' , '===.=.=.=' : 'b' ,  '===.=.===.=' : 'c' ,  '===.=.=' : 'd' , '=' : 'e' ,  '=.=.===.=' : 'f' , '===.===.=': 'g' ,  '=.=.=.=':'h' , '=.=' : 'i' , '=.===.===.===' : 'j' , '===.=.===': 'k' , '=.===.=.=' : 'l' ,  '===.===' : 'm', '===.=': 'n'  , '===.===.===' : 'o' , '=.===.===.=' : 'p' , '===.===.=.===' : 'q' , '=.===.=' : 'r' , '=.=.=' : 's' , '===' : 't' , '=.=.===' : 'u' ,  '=.=.=.===' : 'v' ,  '=.===.===' : 'w' ,  '===.=.=.===' : 'x', '===.=.===.===' : 'y' , '===.===.=.=' : 'z' }

#variavel para armazenar a quantidade de testes
j = int(input())

#laço para executar em cada teste
for k in range(j):
	#variavel para receber o codigo
	x = input()
	
	#transformando o codigo em array separando os elementos por '.......' 
	#temos um array de 'palavras em morse'
	x = x.split('.......')

	#varrendo cada palavra do array
	for palavra in range(len(x)):
		#separando a palavra por 'caracteres'
		b = x[palavra]
		b = b.split('...')

		#transformando cada caractere da palavra em uma letra do alfabeto
		for i in range(len(b)):
			#busca no dicionario o caractere cuja Chave seja igual ao codigo atual do array X
			print(cod[b[i]] , end='')

		#imprimindo espaço caso não seja a ultima palavra
		if palavra != len(x) - 1:
			print(end=' ')

	# nova linha apenas
	print()