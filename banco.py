from typing import List
from time import sleep

from models.cliente import Cliente
from models.conta import Conta

contas: List[Conta] = []

def main() -> None:
    menu()

def menu() -> None:
    print("="*70)
    print('ATM'.center(70, '='))
    print('Geek Bank'.center(70, '='))
    print("="*70)

    print('1 - Criar conta.')
    print('2 - Efetuar Saque.')
    print('3 - Efetuar depósito.')
    print('4 - Efetuar transferência.')
    print('5 - Listar contas.')
    print('6 - Sair do sistema.')
    opcao: int = int(input('Selecione uma opção no menu: '))
    print()

    if opcao == 1:
        criar_conta()
    elif opcao == 2:
        efetuar_saque()
    elif opcao == 3:
        efetuar_deposito()
    elif opcao == 4:
        efetuar_transferencia()
    elif opcao == 5:
        listar_contas()
    elif opcao == 6:
        print('Saindo do sistema...')
        sleep(2)
        exit()
    else:
        print('Opção inválida. Tente novamente.')
        sleep(2)
        menu


def criar_conta() -> None:
    print('Informe os dados do cliente: ')

    nome: str = input('Nome do cliente: ')
    email: str = input('E-mail do cliente: ')
    cpf: str = input('CPF do cliente: ')
    data_nascimento: str = input('Data de nascimento do cliente: ')

    cliente: Cliente = Cliente(nome, email, cpf, data_nascimento)

    conta: Conta = Conta(cliente)

    contas.append(conta)

    print('Conta criada com sucesso!'.center(70, '='))
    print('Dados da conta: '.center(70, ' '))
    print('-'*70)
    print(conta)

    sleep(2)
    menu()


def efetuar_saque() -> None:
    if len(contas) > 0:
        numero: int = int(input('Informe o número da sua conta: '))

        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor: float = float(input('Informe o valor do saque: '))

            conta.sacar(valor)
        else:
            print(f'A conta {numero} não foi encontrada.')
    else:
        print('Ainda não existem contas cadastradas.\n')
    sleep(2)
    menu()


def efetuar_deposito() -> None:
    if len(contas) > 0:
        numero: int = int(input('Informe o número da sua conta: '))

        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor: float = float(input('Informe o valor do depósito: '))

            conta.depositar(valor)
        else:
            print(f'Não foi encontrada uma conta com o número {numero}')
    else:
        print('Ainda não existem contas cadastradas.\n')
    sleep(2)
    menu()

def efetuar_transferencia() -> None:
    if len(contas) > 0:
        numero_o: int = int(input('Informe o número da sua conta: '))

        conta_o: Conta = buscar_conta_por_numero(numero_o)

        if conta_o:
            numero_d: int = int(input('Informe o número da conta destino: '))

            conta_d: Conta = buscar_conta_por_numero(numero_d)

            if conta_d:
                valor: float = float(input('Informe o valor da transferência: '))

                conta_o.transferir(conta_d, valor)
            else:
                print(f'Não foi encontrada uma conta com o número {numero_d}')
        else:
            print(f'A sua conta com número {numero_o} não foi encontrada. ')

    else:
        print('Ainda não existem contas cadastradas.\n')
    sleep(2)
    menu()


def listar_contas() -> None:
    if len(contas) > 0:
        print('Listagem de contas'.center(70, '='))

        for conta in contas:
            print(conta)
            print('-'*70)
            sleep(1)
    else:
        print('Ainda não existem contas cadastradas.\n')
    sleep(2)
    menu()


def buscar_conta_por_numero(numero: int) -> Conta:
    c: Conta = None

    if len(contas) > 0:
        for conta in contas:
            if conta.numero == numero:
                c = conta
                break
    return c

if __name__ == '__main__':
    main()