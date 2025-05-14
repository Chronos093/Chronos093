#!/bin/bash

# FUNÇÕES #
# função que copia o arquivo teste.txt
function copiaTeste () {
    scp teste.txt ubuntu@$ip:/home/teste

    if [ $? -eq 0 ] 
    then
        echo $DATA ' -- COPIA DO ARQUIVO TESTE.TXT ---- OK --' >> log.txt 
    else 
        echo $DATA ' -- COPIA DO ARQUIVO TESTE.TXT ---- ERRO --' >> log.txt 
    fi
}


clear
# DIA E HORA
DATA=`date +'%d-%m-%Y - %H:%M:%S'`

# INPUT PARA PEGAR O IP DO SERVER
echo 'Digite o ip do servidor: '
read ip

# VERIFICA SE DIRETORIO PARA COPIA EXISTE
ssh ubuntu@$ip << EOF
    if [ -d /home/teste  ];
    then 
        echo 'O diretorio /home/teste já existe.'
        sleep 3s
        exit
    else
        echo 'Criando o diretorio /home/teste'
        sleep 2s
        sudo mkdir /home/teste
        sudo chmod 777 /home/teste
        exit
    fi
EOF
# CRIA O LOG DO VERIFICA DIRETORIO
if [ $? -eq 0 ] 
then
    echo $DATA ' -- VERIFICA SE ARQUIVO EXISTE ---- OK --' >> log.txt 
else 
    echo $DATA ' -- VERIFICA SE ARQUIVO EXISTE ---- ERRO --' >> log.txt 
fi

clear

copiaTeste