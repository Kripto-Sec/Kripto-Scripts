import random
import time
import sys
import os

#cores
branco = '\033[1;97m'
azul = '\033[1;34m'
vermelho = '\033[1;31m	'


#Carrega a art ASCII
arte = [branco+"""
 __  _  ____   ____  ____  ______   ___      _____   __  ____   ____  ____  ______  _____
|  l/ ]|    \ l    j|    \|      T /   \    / ___/  /  ]|    \ l    j|    \|      T/ ___/
|  ' / |  D  ) |  T |  o  )      |Y     Y   (   \_  /  / |  D  ) |  T |  o  )      (   \_ 
|    \ |    /  |  | |   _/l_j  l_j|  O  |   \__  T/  /  |    /  |  | |   _/l_j  l_j\__  T
|     Y|    \  |  | |  |    |  |  |     |   /  \ /   \_ |    \  |  | |  |    |  |  /  \ |
|  .  ||  .  Y j  l |  |    |  |  l     !   \    \     ||  .  Y j  l |  |    |  |  \    |
l__j\_jl__j\_j|____jl__j    l__j   \___/     \___j\____jl__j\_j|____jl__j    l__j   \___j
                                                                                       

"""+branco, branco+"""
 _ __      _        _            ___            _        _      
| / / _ _ <_> ___ _| |_ ___     / __> ___  _ _ <_> ___ _| |_ ___
|  \ | '_>| || . \ | | / . \    \__ \/ | '| '_>| || . \ | | <_-<
|_\_\|_|  |_||  _/ |_| \___/    <___/\_|_.|_|  |_||  _/ |_| /__/
             |_|                                  |_|           
      
"""+branco, branco+"""
.-..-.      _       .-.       .--.             _       .-.      
: :' ;     :_;     .' `.     : .--'           :_;     .' `.     
:   ' .--. .-..---.`. .'.--. `. `.  .--. .--. .-..---.`. .'.--. 
: :.`.: ..': :: .; `: :' .; : _`, :'  ..': ..': :: .; `: :`._-.'
:_;:_;:_;  :_;: ._.':_;`.__.'`.__.'`.__.':_;  :_;: ._.':_;`.__.'
              : :                                : :            
              :_;                                :_;            

 """, """
 ____  __.      .__        __          _________            .__        __          
|    |/ _|______|__|______/  |_  ____ /   _____/ ___________|__|______/  |_  ______
|      < \_  __ \  \____ \   __\/  _ \\_____  \_/ ___\_  __ \  \____ \   __\/  ___/
|    |  \ |  | \/  |  |_> >  | (  <_> )        \  \___|  | \/  |  |_> >  |  \___ \ 
|____|__ \|__|  |__|   __/|__|  \____/_______  /\___  >__|  |__|   __/|__| /____  >
        \/         |__|                      \/     \/         |__|             \/ 
"""+branco, branco+"""
                                                                             
 o   o        o          o         .oPYo.               o          o         
 8  .P                   8         8                               8         
o8ob'  oPYo. o8 .oPYo.  o8P .oPYo. `Yooo. .oPYo. oPYo. o8 .oPYo.  o8P .oPYo. 
 8  `b 8  `'  8 8    8   8  8    8     `8 8    ' 8  `'  8 8    8   8  Yb..   
 8   8 8      8 8    8   8  8    8      8 8    . 8      8 8    8   8    'Yb. 
 8   8 8      8 8YooP'   8  `YooP' `YooP' `YooP' 8      8 8YooP'   8  `YooP' 
:..::....:::::..8 ....:::..::.....::.....::.....:..:::::..8 ....:::..::.....:
::::::::::::::::8 ::::::::::::::::::::::::::::::::::::::::8 :::::::::::::::::
::::::::::::::::..::::::::::::::::::::::::::::::::::::::::..:::::::::::::::::
""", """
'||'  |'           ||             .            .|'''.|                   ||             .          
 || .'    ... ..  ...  ... ...  .||.    ...    ||..  '    ....  ... ..  ...  ... ...  .||.   ....  
 ||'|.     ||' ''  ||   ||'  ||  ||   .|  '|.   ''|||.  .|   ''  ||' ''  ||   ||'  ||  ||   ||. '  
 ||  ||    ||      ||   ||    |  ||   ||   || .     '|| ||       ||      ||   ||    |  ||   . '|.. 
.||.  ||. .||.    .||.  ||...'   '|.'  '|..|' |'....|'   '|...' .||.    .||.  ||...'   '|.' |'..|' 
                        ||                                                    ||                   
                       ''''                                                  ''''                  
"""+branco, branco+"""
    __ __      _       __       _____           _       __      
   / //_/_____(_)___  / /_____ / ___/__________(_)___  / /______
  / ,<  / ___/ / __ \/ __/ __ \\__ \/ ___/ ___/ / __ \/ __/ ___/
 / /| |/ /  / / /_/ / /_/ /_/ /__/ / /__/ /  / / /_/ / /_(__  ) 
/_/ |_/_/  /_/ .___/\__/\____/____/\___/_/  /_/ .___/\__/____/  
            /_/                              /_/                
"""+branco, branco+""""
                                               .
                                              /|
                         ____...,---.___..__,) |
   ,_.-._   ,._,.--''''''                   ' ;
  /      '-'                               ) /
,'_._.    `_                             ,' :
      `-.   -.                    _     '  ;
        )`-.  `.     /;          ) )   ,' / 
         '. `.  -.  (  \        | =' .'  ;
           `. '-._+ .\= \.-'-'-.| ; /  :'
             `.    \\ `-        `.+'  ;
      .-.      `. ,-+,' = _  (_  ;  .'
      ; (_      /: =,(    O\  O  ).J
      `. =`.   ;'  =\ \     7P   ' 
        `-. '-: .' = \ \  (:  :) )
           `--| ;   = `.`. `=="./
              ; :       `-`.__.' )
              : |                ;
              '.'.=  -.     .    +
           ,'`)  :=    \    ,  /  `.
           ) =|   `.   ,+-.-'-+.    ;.
           ; \:   /|   | ;      `._  =)
          :  ( `-' |   (/  Kripto  ;  ;
          ( |;    (:    ) Script   |  :
           `-     / )|  ;          )  |)
                 (_/ `-'            `-'

"""+branco,branco+"""             ,----------------,              ,---------,
        ,-----------------------,          ,"        ,"|
      ,"                      ,"|        ,"        ,"  |
     +-----------------------+  |      ,"        ,"    |
     |  .-----------------.  |  |     +---------+      |
     |  |                 |  |  |     | -==----'|      |
     |  |  KRIPTO SCRIPTS |  |  |     |         |      |
     |  |  Bad command or |  |  |/----|`---=    |      |
     |  |  C:\>_          |  |  |   ,/|==== ooo |      ;
     |  |                 |  |  |  // |(((( [33]|    ,"
     |  `-----------------'  |," .;'| |((((     |  ,"
     +-----------------------+  ;;  | |         |,"     -Kevin Lam-
        /_)______________(_/  //'   | +---------+
   ___________________________/___  `,
  /  oooooooooooooooo  .o.  oooo /,   \,"-----------
 / ==ooooooooooooooo==.o.  ooo= //   ,`\--{)B     ,"
/_==__==========__==_ooo__ooo=_/'   /___________,"
`-----------------------------'
"""+branco, branco+"""
              ,---------------------------,
              |  /---------------------\  |
              | |                       | |
              | |     Kripton           | |
              | |      Scripts          | |
              | |       Company         | |
              | |                       | |
              |  \_____________________/  |
              |___________________________|
            ,---\_____     []     _______/------,
          /         /______________\           /|
        /___________________________________ /  | ___
        |                                   |   |    )
        |  _ _ _                 [-------]  |   |   (
        |  o o o                 [-------]  |  /    _)_
        |__________________________________ |/     /  /
    /-------------------------------------/|      ( )/
  /-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/ /
/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/ /
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""+branco, branco+"""
             ________________________________________________
            /                                                \
           |    _________________________________________     |
           |   |                                         |    |
           |   |  C:\> _ KriptoScripts.py                |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |_________________________________________|    |
           |                                                  |
            \_________________________________________________/
                   \___________________________________/
                ___________________________________________
             _-'    .-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.  --- `-_
          _-'.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.--.  .-.-.`-_
       _-'.-.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-`__`. .-.-.-.`-_
    _-'.-.-.-.-. .-----.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-----. .-.-.-.-.`-_
 _-'.-.-.-.-.-. .---.-. .-------------------------. .-.---. .---.-.-.-.`-_
:-------------------------------------------------------------------------:
`---._.-------------------------------------------------------------._.---'
                              -Roland Hangg-
                              """+branco]



os.system('clear')

#Barra de carregamento
print (azul+"[*] CARREGANDO POR FAVOR AGUARDE [*]")
print ("\n")
def progress_bar(done):
    print("\rCarregando: [{0:50s}] {1:.1f}%".format('#' * int(done * 50), done * 100),end='')

def test():
    for n in range(101):
        progress_bar(n/100)
        time.sleep(0.1)

test()

os.system('clear')
print(random.choice(arte))

#Escolhas do script
#dentro de um laco infinitooooooooooooo
while True:
    print("\n")
    print("ESCOLHA UM DOS SCRIPTS PARA INSTALAR")
    print("PARA SABER MAIS SOBRE UM SCRIPT DIGITE: info numero ex: info 1")
    print("\n")
    print("\033[1;92m[01]\033[m \033[1;97mAdmin Painel Finder")
    print("\033[1;92m[02]\033[m \033[1;97mBrasil Cameras Hack")
    print("\033[1;92m[03]\033[m \033[1;97mSSH Brute")
    print("\033[1;92m[04]\033[m \033[1;97mFTP Brute")
    print("\033[1;92m[05]\033[m \033[1;97mBrute Force Gui (TESTADO APENAS EM PC )")
    print("\033[1;92m[06]\033[m \033[1;97mSnake Game (TESTADO APENAS EM PC )")
    print("\033[1;92m[07]\033[m \033[1;97mCifra de Cesar")
    print("\033[1;92m[08]\033[m \033[1;97mFace Detection (TESTADO APENAS EM PC )")
    print("\033[1;92m[09]\033[m \033[1;97mSqlI Scanner")
    print("")
    print("\033[1;91m[00]\033[m \033[1;97mExtras")
    print("")
    print("\033[1;92m[99]\033[m \033[1;97mSair")
    print("\n")
    escolha = input("Krs > ")



#info do Adm Finder
    if escolha == 'info 1' or escolha == 'info 01':
        print("\n")
        os.system('clear')
        print("Script simples feito em python\nusado para encontrar paginas de admin em sites")

#info do Brasil Cameras
    
    elif escolha == 'info 02'or escolha == 'info 2' :
        print("\n")
        os.system('clear')
        print("Script feito em python que busca cameras IPs expostas\nE as exibe para o atacante")
    
#info do SSH brute
    elif escolha == 'info 03' or escolha == 'info 3':
        print("\n")
        os.system('clear')
        print("Script em python para brute force em servidores ssh ")

#info do brute FTP
    elif escolha == 'info 04' or escolha == 'info 4':
        os.system('clear')
        print("Script em python feito para\nfazer brute force em servidores FTP")

#info do Brute Force Gui
    elif escolha == 'info 05' or escolha == 'info 5':
        os.system('clear')
        print("Script De brute force com interface grafica\nUltilizando o modulo RANDOM ")

#info do Snake Game
    elif escolha == 'info 06' or escolha == 'info 6':
        os.system('clear')
        print("O classico Jogo da cobrinha feito em python")

#info do Cifra de Cesar
    elif escolha == 'info 07' or escolha == 'info 7':
        os.system('clear')
        print("Um python Script feito para criptografar e descriptgrafar\nA Cifra de Cesar (Primeira criptografia do mundo) ")

#info do Face Detection
    elif escolha == 'info 08' or escolha == 'info 8':
        os.system('clear')
        print("Script de deteccao de rostos humanos em tempo real\nUltilizando o OpenCV2")

#info do SqlI Scanner
    elif escolha == 'info 09' or escolha == 'info 9':
        os.system('clear')
        print("(NAO FEITO BOM MIN Script Feito Em python\nQue escaneia possiveis vulnerabilidades sql")


#extras
    elif escolha == '00' or escolha == '0':
        os.system('clear')
        print("\033[1;92m[01]\033[m \033[1;97mCreditos")   
        print("\033[1;92m[02]\033[m \033[1;97mBanner")
        print("")
        print("\033[1;92m[00]\033[m \033[1;97mVoltar")
        extra = input("Krs > ")

#Extras Banner
        if extra == '02' or extra == '2':
            os.system('clear')
            print(random.choice(arte))
            

#Extras creditos

        elif extra == '1' or extra == '01':
            os.system('clear')
            print("\033[1;34m[*]\033[m \033[1;31m TODOS OS SCRIPTS PRESENTES FORAM CRIADOS POR\033[m \033[1;34m[*]\033[m")
            print("\033[1;34m[*]\033[m \033[1;31m KRIPTO-SEC (JEAN)\033[m")
            print("\033[1;34m[*]\033[m \033[1;31m github: https://github.com/Kripto-Sec/\033[m" )
            print("")
            print("\033[1;97m[00] voltar")
            creditos = input("Krs > ")
            if creditos == '00' or creditos == '0':
                print("")
                os.system('clear')
                print(random.choice(arte))


#escolha do admin painel finder
    elif escolha == '01' or escolha == '1':
        print("\n")
        print("\n\033[1;92m[+]\033[m \033[1;97m Instalando Admin Painel Finder \033[1;92m[+]\033[m")
        os.system('apt update -y && apt upgrade -y')
        os.system('pip install requests')
        os.system('pip3 install requests')
        os.system('git clone https://github.com/Kripto-Sec/Admin_Painel_Finder.git')
        os.system('mv Admin_Painel_Finder ~')
        os.system('clear')
        print("\033[1;92m[+]\033[m \033[1;97m Feito \033[1;92m[+]")
        print("\033[1;92m[+]\033[m \033[1;97m Instalado em home \033[1;92m[+]")
        print(random.choice(arte))

#escolha do Brasil cameras hack
    elif escolha == '02' or escolha == '2':
        print("\n")
        print("\n\033[1;92m[+]\033[m \033[1;97m  Instalando Brasil Cameras Hack \033[1;92m[+]\033[m")
        os.system('apt update -y && apt upgrade -y')
        os.system('pip3 install requests')
        os.system('pip install emoji')
        os.system('git clone https://github.com/Kripto-Sec/Brasil-Cameras-hack.git')
        os.system('mv Brasil-Cameras-hack ~')
        os.system('clear')
        print("\033[1;92m[+]\033[m \033[;97m Feito \033[1;92m[+]")
        print("\033[1;92m[+]\033[m \033[1;97m Instalado em home \033[1;92m[+]")
        print(random.choice(arte))

#Escolha do ssh brute
    elif escolha == '03' or escolha == '3':
        print("\n")
        print("\n\033[1;92m[+]\033[m \033[1;97m Instalando SSH brute \033[1;92m[+]\033[m")
        os.system('apt update -y && apt upgrade -y')
        os.system('pip install paramiko')
        os.system('pip3 install paramiko')
        os.system('git clone https://github.com/Kripto-Sec/SSHbrute.git')
        os.system('mv SSHbrute ~')
        os.system('clear')
        print("\033[1;92m[+]\033[m \033[1;97m Feito \033[1;92m[+]")
        print("\033[1;92m[+]\033[m \033[1;97m Instalado em home \033[1;92m[+]")
        print(random.choice(arte))

#escolha do brute ftp
    elif escolha == '4' or escolha == '04':
        print("\n")
        print("\n\033[1;92m[+]\033[m \033[1;97m Instalando FTP Brute \033[1;92m[+]\033[m")
        os.system('apt update -y && apt upgrade -y')
        os.system('pip install sockets')
        os.system('pip3 install sockets')
        os.system('git clone https://github.com/Kripto-Sec/BruteFTP.git')
        os.system('mv BruteFTP ~')
        os.system('clear')
        print("\033[1;92m[+]\033[m \033[1;97m Feito \033[1;92m[+]")
        print("\033[1;92m[+]\033[m \033[1;97m Instalado em home \033[1;92m[+]")
        print(random.choice(arte))

#escolha do Brute Force Gui
    elif escolha == '5' or escolha == '05':
        print("\n")
        print("\n\033[1;92m[+]\033[m \033[1;97m Instalando Brute Force GUI \033[1;92m[+]\033[m")
        os.system('apt update -y && apt upgrade -y')
        os.system('pip install PyAutoGUI')
        os.system('pip3 install PyAutoGUI')
        os.system('git clone https://github.com/Kripto-Sec/Brute-ForceGui.git')
        os.system('mv Brute-ForceGui ~')
        os.system('clear')
        print("\033[1;92m[+]\033[m \033[1;97m Feito \033[1;92m[+]")
        print("\033[1;92m[+]\033[m \033[1;97m Instalado em home \033[1;92m[+]")
        print(random.choice(arte))

#Escolha do Snake game
    elif escolha == '06' or escolha == '6':
        print("\n")
        print("\n\033[1;92m[+]\033[m \033[1;97m Instalando Snake Game \033[1;92m[+]\033[m")
        os.system('apt update -y && apt upgrade -y')
        os.system('pip install pygame')
        os.system('pip3 install pygame')
        os.system('git clone https://github.com/Kripto-Sec/Snake-Game.git')
        os.system('mv Snake-Game ~')
        os.system('clear')
        print("\033[1;92m[+]\033[m \033[1;97m Feito \033[1;92m[+]")
        print("\033[1;92m[+]\033[m \033[1;97m Instalado em home \033[1;92m[+]")
        print(random.choice(arte))

#Escolha do Cifra de Cesar       
    elif escolha == '07' or escolha == '7':
        print("\n")
        print("\n\033[1;92m[+]\033[m \033[1;97m Instalando Cifra de Cesar \033[1;92m[+]\033[m")
        os.system('apt update -y && apt upgrade -y')
        os.system('git clone https://github.com/Kripto-Sec/Cifra-de-Cesar.git')
        os.system('mv Cifra-de-Cesar ~')
        os.system('clear')
        print("\033[1;92m[+]\033[m \033[1;97m Feito \033[1;92m[+]")
        print("\033[1;92m[+]\033[m \033[1;97m Instalado em home \033[1;92m[+]")
        print(random.choice(arte))

#Escolha do Face Detection
    elif escolha == '08' or escolha == '8':
        print("\n")
        print("\n\033[1;92m[+]\033[m \033[1;97m Instalando Face Detection \033[1;92m[+]\033[m")
        os.system('apt update -y && apt upgrade -y')
        os.system('pip install opencv-python')
        os.system('pip3 install opencv-python')
        os.system('git clone https://github.com/Kripto-Sec/DeteccaoDeRosto.git')
        os.system('mv DeteccaoDeRosto ~')
        os.system('clear')
        print("\033[1;92m[+]\033[m \033[1;97m Feito \033[1;92m[+]")
        print("\033[1;92m[+]\033[m \033[1;97m Instalado em home \033[1;92m[+]")
        print(random.choice(arte))


#Escolha do SqlI
    elif escolha == '9' or escolha == '09':
        print("\n")
        print("\n\033[1;92m[+]\033[m \033[1;97m Instalando SqlI Scanner \033[1;92[+]\033[m")
        os.system('apt update -y && apt upgrade -y')
        os.system('pip install argparse')
        os.system('pip3 install argparse')
        os.system('pip install logging')
        os.system('pip3 install logging')
        os.system('pip install multiprocess')
        os.system('pip3 install multiprocess')
        os.system('git clone https://github.com/Kripto-Sec/sqli-scanner.git')
        os.system('mv sqli-scanner ~')
        os.system('clear')


    elif escolha == '99':
        print("Adeus")
        break
    else:
        os.system('clear')
        print("Por favor use apenas os comandos abaixo")


