import os 
op = 0
clientes = []
cliente = dict()
def cadCliente():
    os.system('cls')
    cliente['Nome'] = input('Nome: ')
    cliente['CPF/CNPJ'] = int(input('CPF/CNPJ: '))
    cliente['Telefone'] = int(input('Telefone: '))
    cliente['Endereço'] = input('Endereço: ')
    cliente['E-mail'] = input('E-mail: ')
    cliente['Produto'] = input('Produto: ')
    clientes.append(cliente.copy())
    
    print('Informações do cliente:')
    for c, v in cliente.items():
        print(f'{c} : {v}')


def edit():
    os.system('cls')
    print(':::::::::::::::::|EDITAR CADASTRO|:::::::::::::::::')
    for i, c in enumerate(clientes):
        print('Cliente [{0}]\nNome: {1}'.format(i, c['Nome']))
    while True:
        edit = int(input(('Digite o valor correspondente ao cliente que deseja editar: ')))
        if edit < len(clientes) and edit >= 0:
            break
        print(f'ERRO! digite valores entre {0} e {len(clientes)}')
    edit_c = clientes[edit]
    print('Nome:',edit_c['Nome'])
    print('CPF/CNPJ:',edit_c['CPF/CNPJ'])
    print('Telefone:',edit_c['Telefone'])
    print('Endereço:',edit_c['Endereço'])
    print('E-mail:',edit_c['E-mail'])
    print('Produto:',edit_c['Produto'])
    editar = str(input('Tem certeza que deseja editar?\n[S] SIM [N] NÃO : ')).lower()[0]
    if editar == 's':
        e_nome = input('Nome: ')
        e_cpf = int(input('CPF/CNPJ: '))
        e_tell = int(input('Telefone: '))
        e_endr = input('Endereço: ')
        e_email = input('E-mail: ')
        e_prod = input('Produto: ')
        
        cliente['Nome'] = e_nome
        cliente['CPF/CNPJ'] = e_cpf
        cliente['Telefone'] = e_tell
        cliente['Endereço'] = e_endr
        cliente['E-mail'] = e_email
        cliente['Produto'] = e_prod
        del clientes[edit]
        clientes.insert(edit,cliente)
        
        print('------------------------------------------------')
        print('|O CADASTRO DO CLIENTE FOI EDITADO COM SUCESSO!|')
        print('------------------------------------------------\n')
    elif editar == 'n':
        print('===================================')
        print('|PROCEDIMENTO CANCELADO!|')
        print('------------------------------------\n')

def excl(): 
    os.system('cls')
    print('::::::::::::::::|EXCLUIR CADASTRO|::::::::::::::::')
    for i, c in enumerate(clientes):
        print('Cliente [{0}]\nNome: {1}'.format(i, c['Nome']))
    while True:
        excl = int(input(('Digite o valor correspondente ao cadastro que deseja excluir: ')))
        if len(clientes) > excl and excl >= 0:
            break
        print(f'ERRO! digite valores entre {0} e {len(clientes)}')
    excl_c = clientes[excl]
    print('Nome:',excl_c['Nome'])
    print('CPF/CNPJ:',excl_c['CPF/CNPJ'])
    print('Telefone:',excl_c['Telefone'])
    print('Endereço:',excl_c['Endereço'])
    print('E-mail:',excl_c['E-mail'])
    print('Produto:',excl_c['Produto'])
    excluir = str(input('Tem certeza que deseja excluir?\n[S] SIM [N] NÃO : ')).lower()[0]
    if excluir == 's':
        del clientes[excl]
        print('=================================================')
        print('|O CADASTRO DO CLIENTE FOI REMOVIDO COM SUCESSO!|')
        print('-------------------------------------------------\n')
    elif excluir == 'n':
        print('===================================')
        print('|PROCEDIMENTO CANCELADO!|')
        print('------------------------------------\n')

def info():
    print('::::::::::::|INFORMAÇÕES DE CADASTROS|::::::::::::')
    for i, c in enumerate(clientes):
            print('Cliente [{0}]\nNome: {1}'.format(i, c['Nome']))
            print('CPF/CNPJ: {1}'.format(i, c['CPF/CNPJ']))
            print('Telefone: {1}'.format(i, c['Telefone']))
            print('Endereço: {1}'.format(i, c['Endereço']))
            print('E-mail: {1}'.format(i, c['E-mail']))
            print('Produto: {1}'.format(i, c['Produto']))
            print()
    print('==================================================\n')

while op != 5:
    print('::::::::::::|CADASTRO DE CLIENTES|::::::::::::')
    print('[1] Cadastrar novos clientes')
    print('[2] Editar clientes')
    print('[3] Remover clientes')
    print('[4] Mostrar infrormações dos clientes')
    print('[5] Sair')
    print('==============================================')
    op = int(input('O que deseja fazer?: '))
    
    os.system('cls')
    if op == 1:
        cadCliente()
    if  op == 2:
        edit()
    if op == 3:
        excl()
    if op == 4:
        info()
print('Obrigado por usar o sistema!')