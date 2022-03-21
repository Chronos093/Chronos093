import os
import shutil
from os import path

if __name__ == '__main__':
    
    dir_Documentos = path.join(path.expanduser("~"), "Documents")
    dir_Imagens = path.join(path.expanduser("~"), "Pictures")
    dir_Videos = path.join(path.expanduser("~"), "Videos")
    dir_Links = path.join(path.expanduser("~"), "Links")
    dir_Desktop = path.join(path.expanduser("~"), "Desktop")
    
    def faz_backup(dir_Desktop, dir_Documentos, dir_Links, dir_Videos, dir_Imagens):
        os.makedirs(path.join(path.expanduser("~"), "Backup"))
        shutil.copy(dir_Desktop, path.join(path.expanduser("~"), "Backup"))
        shutil.copy(dir_Documentos, path.join(path.expanduser("~"), "Backup"))
        shutil.copy(dir_Links, path.join(path.expanduser("~"), "Backup"))
        shutil.copy(dir_Videos, path.join(path.expanduser("~"), "Backup"))
        shutil.copy(dir_Imagens, path.join(path.expanduser("~"), "Backup"))
        
    def verifica_conteudo(dir_Desktop, dir_Documentos, dir_Links, dir_Videos, dir_Imagens):
        if os.listdir(dir_Documentos) == []:
            print("O Diretório Documentos está vazio.")
        else:
            print("Realizanso backup dos arquivos.")
            faz_backup(dir_Desktop, dir_Documentos, dir_Links, dir_Videos, dir_Imagens)
        
        if os.listdir(dir_Imagens) == []:
            print("O Diretório Imagens está vazio.")
        else:
            print("Realizanso backup dos arquivos.")
            faz_backup(dir_Desktop, dir_Documentos, dir_Links, dir_Videos, dir_Imagens)
        
        if os.listdir(dir_Videos) == []:
            print("O Diretório Vídeos está vazio.")
        else:
            print("Realizanso backup dos arquivos.")
            faz_backup(dir_Desktop, dir_Documentos, dir_Links, dir_Videos, dir_Imagens)
        
        if os.listdir(dir_Links) == []:
            print("O Diretório Links está vazio.")
        else:
            print("Realizanso backup dos arquivos.")
            faz_backup(dir_Desktop, dir_Documentos, dir_Links, dir_Videos, dir_Imagens)
        
        if os.listdir(dir_Desktop) == []:
            print("O Diretório Área de Trabalho está vazio.")
        else:
            print("Realizanso backup dos arquivos.")
            faz_backup(dir_Desktop, dir_Documentos, dir_Links, dir_Videos, dir_Imagens)
    
    verifica_conteudo(dir_Desktop, dir_Documentos, dir_Links, dir_Videos, dir_Imagens)
