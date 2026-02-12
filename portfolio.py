
#=============================================== Video explicativo do projeto: ======================================

# https://youtu.be/KOJUOTfKKRo


#=============================================== Simulação banco de Dados  ==========================================

eventos = {}
inscricoes = {}

#=============================================== Importação do Colorama =============================================


#Importa o Colarama.
import colorama
from colorama import Fore, Back, Style
colorama.init()

#=============================================== função limpa tela ===================================================


#Função para limpar a tela.
def limpar_tela ():     
    print("\033c", end ="")

#=============================================== Inicialização ========================================================

def abrir_menu():
    while True:
        limpar_tela()
        print(Back.CYAN + Style.BRIGHT + "\n\t Sistema de Eventos UNIFECAF - Bem Vindo! "+ Style.RESET_ALL)
        print()
        print(Fore.CYAN + Style.BRIGHT + "Deseja acessar como 'Coordenador' ou 'Aluno' ?\n" + Style.RESET_ALL)
        print(Style.DIM + "1 = Coordenador\n2 = Aluno\n3 = Sair\n" + Style.RESET_ALL )

        try:
            acesso = int(input(Style.BRIGHT +"Selecionar opção: "))
        except ValueError:
            print(Fore.YELLOW + Style.BRIGHT +"⚠️  Entrada inválida. Digite apenas números." + Style.RESET_ALL)
            input(Fore.GREEN + Style.BRIGHT + "Aperte ENTER para continuar."+Style.RESET_ALL)
            continue

        if acesso == 1:
            menu_coordenador()
        elif acesso == 2:
            menu_aluno()
        elif acesso == 3:
            print(Fore.CYAN + Style.BRIGHT +"Saindo do sistema.")
            break
        else:
            print(Fore.YELLOW + Style.BRIGHT +" ⚠️  Opção Invalida" + Style.RESET_ALL)
            input(Fore.GREEN + Style.BRIGHT + "Aperte ENTER para continuar."+Style.RESET_ALL)
        continue

#=================================== Parte do menu do Cordenador =======================================================
def menu_coordenador():    
    while True:
        limpar_tela()
        print(Back.CYAN + Style.BRIGHT + "\t Bem Vindo Coordenador \n" + Style.RESET_ALL)
        print(Style.DIM +"1 - Cadastrar")
        print("2 - Atualizar")
        print("3 - Excluir Evento")
        print("4 - Visualizar Eventos")
        print("5 - Visualizar Inscrições")
        print("6 - Sair\n" + Style.RESET_ALL)

        try:
            opcao = int(input(Style.BRIGHT + "Selecionar opção: "))
        except ValueError:
            print(Fore.YELLOW + Style.BRIGHT +" ⚠️ Entrada inválida. Digite apenas números." + Style.RESET_ALL)
            input(Fore.GREEN + Style.BRIGHT + "Aperte ENTER para continuar."+Style.RESET_ALL)
            continue

        if opcao == 1:
            cadastro_evento()
        elif opcao == 2:
            atualizar_evento()
        elif opcao == 3:
            excluir_evento() 
        elif opcao == 4:
            visualizar_eventos()
        elif opcao == 5:
            visualizar_inscricoes()   
        elif opcao == 6:
            break
        else:
            print(Fore.YELLOW + Style.BRIGHT +" ⚠️  Opção Invalida" + Style.RESET_ALL)
            input(Fore.GREEN + Style.BRIGHT + "Aperte ENTER para continuar."+Style.RESET_ALL)

#===================================== Parte do menu do aluno ==========================================================
def menu_aluno():
    while True:
        limpar_tela()
        print(Back.CYAN + Style.BRIGHT + "\t Bem Vindo Aluno \n" + Style.RESET_ALL)
        print(Style.DIM +"1. Inscrições")
        print("2. Sair\n"+Style.RESET_ALL)
        try:
            opcao = int(input(Style.BRIGHT + "Selecionar opção: "))
        except ValueError:
            print(Fore.YELLOW + Style.BRIGHT +" ⚠️ Entrada inválida. Digite apenas números." + Style.RESET_ALL)
            input(Fore.GREEN + Style.BRIGHT + "Aperte ENTER para continuar."+Style.RESET_ALL)
            continue

        if opcao == 1:
            inscrever_aluno()
        elif opcao == 2:
            break 
        else:       
            print(Fore.YELLOW + Style.BRIGHT +" ⚠️  Opção Invalida" + Style.RESET_ALL)
            input(Fore.GREEN + Style.BRIGHT + "Aperte ENTER para continuar."+Style.RESET_ALL)

#============================================== Cadastro de Eventos ===========================================================
def cadastro_evento ():
    while True:            
        limpar_tela()
        print(Back.CYAN + Style.BRIGHT + "\t Cadastrar Evento \n" + Style.RESET_ALL)

        while True:
            try:
                nome_evento = input (Style.DIM + "Digite o nome do evento: "+Style.RESET_ALL)
                if not nome_evento: 
                    raise ValueError (Fore.YELLOW + Style.BRIGHT +" ⚠️  Nome do Evento não pode ficar vazio" + Style.RESET_ALL)
                break
            except ValueError as erro:
                print(erro)
        descricao = input (Style.DIM + "descrição do Evento: "+Style.RESET_ALL)
        data_evento = input(Style.DIM +"Data do Evento "+Style.RESET_ALL)
        numero_inscritos = 0
        while True:
            try:    
                participantes = int(input(Style.DIM +"Defina o Número Máximo de Participantes "+ Style.RESET_ALL)) 
                if participantes <= 0:
                    print(Fore.YELLOW + Style.BRIGHT +" ⚠️  O Número deve ser maior que Zero" + Style.RESET_ALL)
                    continue
                break
            except ValueError:
                print(Fore.YELLOW + Style.BRIGHT +" ⚠️  Opção Invalida, Use apenas Números" + Style.RESET_ALL)

                

        eventos [nome_evento] = {
            'descricao' : descricao,
            'data' : data_evento,
            'participantes' : participantes,
            'numero_inscritos' : numero_inscritos  
        }   

        print(Fore.GREEN +Style.BRIGHT + f"\n ✅ Evento {Style.RESET_ALL}{Fore.MAGENTA}'{nome_evento}'{Style.RESET_ALL}{Fore.GREEN}{Style.BRIGHT} Cadastrado com sucesso!\n" + Style.RESET_ALL)
        input(Fore.GREEN + Style.BRIGHT + "Aperte ENTER para continuar."+Style.RESET_ALL)


        while True:
            limpar_tela() 
            print(Fore.CYAN + Style.BRIGHT + "\n\tDeseja Adicionar outro Evento ?\n" + Style.RESET_ALL)
            opcao = input( Style.BRIGHT+"Sim = 1\nSair = 2\nDigite a opção "+Style.RESET_ALL) 
            if opcao == "1":
                break
            elif opcao == "2":
                print(Fore.RED + Style.BRIGHT+"\nVoltando para o menu...\n"+Style.RESET_ALL)
                input(Fore.GREEN + Style.BRIGHT+"Aperte ENTER para continuar.\n"+Style.RESET_ALL)
                return
            else:
                print(Fore.YELLOW + Style.BRIGHT + "⚠️  Opção Invalida,Digite '1' ou '2'.\n" + Style.RESET_ALL)
                input(Fore.GREEN + Style.BRIGHT+"Aperte ENTER para continuar.\n"+Style.RESET_ALL)

#============================================== Atualizar Eventos ===========================================================

def atualizar_evento():
    while True:
        limpar_tela()
        print(Back.CYAN + Style.BRIGHT + "\t Atualizar Evento \n" + Style.RESET_ALL)
        for nome, dados in eventos.items():
            print(Fore.YELLOW + Style.BRIGHT + f"Evento: {nome} " + Style.RESET_ALL)
            print("==================================")
           
        nome = input(Style.DIM + "Nome do EVENTO a atualizar: "+Style.RESET_ALL)

        if nome in eventos:
            nova_data = input(Style.DIM + "Nova Data " + Style.RESET_ALL)
            while True:
                try:
                    nova_quantidade = int(input(Style.DIM +"Nova quantidade máxima de Participantes: " + Style.RESET_ALL))
                    if nova_quantidade <= 0:
                        print(Fore.YELLOW + Style.BRIGHT +" ⚠️  O Numero deve ser maior que Zero" + Style.RESET_ALL)
                        continue
                    break
                except ValueError:
                    print(Fore.YELLOW + Style.BRIGHT +" ⚠️  Opção invalida, Use apenas numeros" + Style.RESET_ALL)

        
            eventos[nome]["data"] = nova_data
            eventos[nome]["participantes"] = nova_quantidade
            print(Fore.GREEN +Style.BRIGHT + f"\n ✅ Evento {Style.RESET_ALL}{Fore.MAGENTA}'{nome}'{Style.RESET_ALL}{Fore.GREEN}{Style.BRIGHT} Atualizado com sucesso!\n" + Style.RESET_ALL)
                    
        else:
            print(Fore.RED + Style.BRIGHT + "\n❌ Evento não encontrado.\n" + Style.RESET_ALL)
        input(Fore.GREEN + Style.BRIGHT + " Aperte ENTER para continuar. "+Style.RESET_ALL)


        while True:
            limpar_tela() 
            print(Fore.CYAN + Style.BRIGHT + "\n\tDeseja atualizar outro Evento ?\n" + Style.RESET_ALL)
            opcao = input( Style.BRIGHT+"Sim = 1\nSair = 2\nDigite a opção "+Style.RESET_ALL) 
            if opcao == "1":
                break
            elif opcao == "2":
                print(Fore.RED + Style.BRIGHT+"\nVoltando para o menu...\n"+Style.RESET_ALL)
                input(Fore.GREEN + Style.BRIGHT+"Aperte ENTER para continuar.\n"+Style.RESET_ALL)
                return
            else:
                print(Fore.YELLOW + Style.BRIGHT + "⚠️  Opção Invalida,Digite '1' ou '2'.\n" + Style.RESET_ALL)
                input(Fore.GREEN + Style.BRIGHT+"Aperte ENTER para continuar.\n"+Style.RESET_ALL)


#============================================== Excluir Eventos ============================================================
def excluir_evento():
    while True:
        limpar_tela()
        print(Back.CYAN + Style.BRIGHT + "\t Excluir Evento \n" + Style.RESET_ALL)

        for nome_evento, dados in eventos.items():
            print(Fore.YELLOW + Style.BRIGHT + f"Evento: {nome_evento}" + Style.RESET_ALL)
            print("==================================")

        try:
            nome_evento = input(Style.DIM + "Digite o nome do EVENTO a ser Excluido: " + Style.RESET_ALL)

            if nome_evento.strip() == "":
                raise ValueError("O nome do evento não pode estar vazio.")
                
            if nome_evento not in eventos:
                raise ValueError("❌ Evento não encontrado.")

        except ValueError as erro:
            print(Fore.YELLOW + Style.BRIGHT + f"\n⚠️ Erro: {erro}" + Style.RESET_ALL)
            input(Fore.GREEN + Style.BRIGHT + "Aperte ENTER para continuar.\n" + Style.RESET_ALL)
            return
            

        print(Fore.RED + Style.BRIGHT + f"\n🛑 Esta ação é irreversível. Deseja realmente excluir o evento '{nome_evento}'?" + Style.RESET_ALL)

        while True:
            opcao = input(Style.BRIGHT + "Excluir = 1\nCancela = 2\nDigite a opção: " + Style.RESET_ALL).lower()
            if opcao == "2":
                print(Fore.RED + Style.BRIGHT + "Voltando para menu...\n" + Style.RESET_ALL)
                input(Fore.GREEN + Style.BRIGHT + "Aperte ENTER para continuar.\n" + Style.RESET_ALL)
                return
            elif opcao == "1":
                break
            else:
                print(Fore.YELLOW + Style.BRIGHT + "⚠️  Opção inválida. Digite 's' ou 'n'.\n" + Style.RESET_ALL)

        del eventos[nome_evento]
        print(Fore.GREEN + Style.BRIGHT + f"\n✅ Evento '{nome_evento}' excluído com sucesso!\n" + Style.RESET_ALL)
        input(Fore.GREEN + Style.BRIGHT + "Aperte ENTER para continuar.\n" + Style.RESET_ALL)

        while True:
            limpar_tela()
            print(Fore.CYAN + Style.BRIGHT + "\n\tDeseja excluir outro Evento?\n" + Style.RESET_ALL)
            repetir = input(Style.BRIGHT + "Sim = 1\nSair = 2\nDigite a opção: " + Style.RESET_ALL).lower()
            if repetir == "1":
                break
            elif repetir == "2":
                print(Fore.RED + Style.BRIGHT + "\nVoltando para o menu...\n" + Style.RESET_ALL)
                input(Fore.GREEN + Style.BRIGHT + "Aperte ENTER para continuar.\n" + Style.RESET_ALL)
                return
            else:
                print(Fore.YELLOW + Style.BRIGHT + "⚠️ Opção inválida. Digite '1' ou '2'.\n" + Style.RESET_ALL)
                input(Fore.GREEN + Style.BRIGHT + "Aperte ENTER para continuar.\n" + Style.RESET_ALL)
        
#============================================== Visualizar Inscrições ========================================================

def visualizar_inscricoes():
    limpar_tela()
    print(Back.CYAN + Style.BRIGHT + "\t Alunos Cadastrados \n" + Style.RESET_ALL)

    if not inscricoes:
        print(Fore.YELLOW + Style.BRIGHT + "\n⚠️  Nenhum Aluno Cadastrado\n" + Style.RESET_ALL)
    else:
        print(Fore.CYAN + Style.BRIGHT +" 📖  Lista de Alunos por Evento:"+ Style.RESET_ALL)
        for evento, lista_alunos in inscricoes.items():
            print(f"\n 🗓️  Evento: {evento}")
            for aluno in lista_alunos:
                print(Style.BRIGHT + f" 👤  Nome: {aluno}{Style.RESET_ALL}")

    input(Fore.GREEN + Style.BRIGHT + "\nAperte ENTER para continuar."+Style.RESET_ALL)

    

#============================================== Visualizar Eventos ===========================================================
def visualizar_eventos():
    limpar_tela()
    print(Back.CYAN + Style.BRIGHT + "\t Eventos Cadastrados \n" + Style.RESET_ALL)
    if not eventos:
        print(Fore.YELLOW + Style.BRIGHT +"\n⚠️  Nenhum Evento Cadastrado\n" + Style.RESET_ALL)
    else:
        for nome, dados in eventos.items():
            print(Fore.YELLOW + Style.BRIGHT + f"Evento: {nome} " + Style.RESET_ALL)
            print(f"Descrição: {dados['descricao']}")
            print(f"Data: {dados['data']}")
            print(f"Vagas: {dados['numero_inscritos']}/{dados['participantes']}")
            print ("==============================================================\n")
    input(Fore.GREEN + Style.BRIGHT + " Aperte ENTER para continuar."+Style.RESET_ALL)

#============================================== Cadastro em Eventos ==========================================================
def inscrever_aluno():
    limpar_tela()
    print(Back.CYAN + Style.BRIGHT + "\t Inscrições \n" + Style.RESET_ALL)

    if not eventos:
        print(Fore.YELLOW + Style.BRIGHT + " ⚠️  Nenhum evento disponível para inscrição.\n" + Style.RESET_ALL)
        input(Fore.GREEN + Style.BRIGHT + "Aperte ENTER para continuar." + Style.RESET_ALL)
        return

 #========================================= mostrar todos os eventos cadastrados ================================================

    while True:
        print(Fore.CYAN + Style.BRIGHT + "\nEventos Disponíveis para Inscrição\n" + Style.RESET_ALL)
        for nome_evento, dados in eventos.items():
            dados = eventos[nome_evento]
            descricao = dados["descricao"]
            data_evento = dados["data"]
            vagas = f"{dados['numero_inscritos']}/{dados['participantes']}"
            print(Style.BRIGHT + Fore.MAGENTA + f"🚨 {nome_evento}{Style.RESET_ALL}")
            print(Fore.YELLOW + Style.BRIGHT + f"{descricao}\n{data_evento}\nVagas: {vagas}" + Style.RESET_ALL)

#============================================= Validação do Cadastro ================================================

        print(Fore.CYAN + Style.BRIGHT + "\nDeseja se inscrever?" + Style.RESET_ALL)
        opcao = input(Style.BRIGHT + "Inscreve-se = 1\nSair = 2\nDigite a opção: " + Style.RESET_ALL).lower()

        if opcao == "2":
            print(Fore.RED + Style.BRIGHT + "Voltando para o menu...\n" + Style.RESET_ALL)
            input(Fore.GREEN + Style.BRIGHT + "Aperte ENTER para continuar.\n" + Style.RESET_ALL)
            return

        elif opcao != "1":
            limpar_tela()
            print(Fore.YELLOW + Style.BRIGHT + " ⚠️  Opção inválida. Digite '1' ou '2'.\n" + Style.RESET_ALL)
            continue

#=============================================Aluno se Cadastrando ============================================================

        escolha = input(Fore.MAGENTA + Style.BRIGHT + "Digite o nome do evento que deseja se cadastrar: " + Style.RESET_ALL)

        if escolha not in eventos:
            limpar_tela()
            print(Fore.YELLOW + Style.BRIGHT + " ⚠️  Evento não encontrado!\n" + Style.RESET_ALL)
            continue

        evento = eventos[escolha]

        if evento["numero_inscritos"] >= evento["participantes"]:
            limpar_tela()
            print(Fore.RED + Style.BRIGHT + "📢 Vagas esgotadas para este evento. Selecione uma opção ainda disponível.\n" + Style.RESET_ALL)
            continue

        while True:
            try:
                nome_aluno = input(Fore.MAGENTA + Style.BRIGHT + "Digite seu nome: " + Style.RESET_ALL)
                if not nome_aluno: 
                    raise ValueError (Fore.YELLOW + Style.BRIGHT +" ⚠️  Nome não pode ficar vazio" + Style.RESET_ALL)
                break
            except ValueError as erro:
                print(erro)   

        if escolha not in inscricoes:
            inscricoes[escolha] = []

        if nome_aluno in inscricoes[escolha]:
            limpar_tela()
            print(Fore.YELLOW + Style.BRIGHT + "⚠️  Você já está inscrito neste evento. \n" + Style.RESET_ALL)
        else:
            inscricoes[escolha].append(nome_aluno)
            evento["numero_inscritos"] += 1
            limpar_tela()
            print( Style.BRIGHT + f"✅ {nome_aluno}{Style.RESET_ALL}{Fore.YELLOW}{Style.BRIGHT} Inscrito em {Style.RESET_ALL}{Style.BRIGHT}{escolha}{Style.RESET_ALL}{Fore.YELLOW}{Style.BRIGHT} com sucesso.\n" + Style.RESET_ALL)

        input(Fore.GREEN + Style.BRIGHT + "Aperte ENTER para continuar." + Style.RESET_ALL)
        
        limpar_tela()

                
                
abrir_menu()