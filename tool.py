import os
import platform
from dataclasses import dataclass
import subprocess
import argparse
from data import data

@dataclass
class tool:
    def clear_screen():
        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')

    def args():
        parameter = argparse.ArgumentParser(prog="git_script")
        parameter.add_argument('--push', action='store_true', help='Executa o push no repositório')
        parameter.add_argument('--pull', action='store_true', help="Ultila O Pull para siconizar o code atual com o do Git Hub")
        return parameter.parse_args()

    def gitInit(data:data) -> bool:
        path = os.path.join(data.path_local)
        if not path:return False
        try:
            subprocess.run(["git","init"])
            subprocess.run(["git", "branch", "-M", "main"], check=True)
            #git pull origin main --allow-unrelated-histories
            subprocess.run(["git", "remote", "add", "origin", data.remote_link], check=True) #Adiciona A coneçao remote novamente
            subprocess.run(["git","pull","origin","main","--allow-unrelated-histories"]) #remove o commit que nao foi puchados
            subprocess.run(["git", "add", "."], check=True)
            subprocess.run(["git", "commit", "-m", data.commit], check=True)
            subprocess.run(["git", "push", "-u", "origin", "main"], check=True)
            subprocess.run(["git","branch","dev"])
        except Exception as E:
            print(f"Erro Al Execultar Script De git, Erro: {E}")      
            return False  
        
    def gitPush(data:data):
        path = os.path.join(data.path_local)
        if not path:return False
        try:
            subprocess.run(["git","pull","origin","main","--allow-unrelated-histories"]) #remove o commit que nao foi puchado
            subprocess.run(["git", "branch", "-M", "main"], check=True)
            subprocess.run(["git", "add", "."], check=True)
            subprocess.run(["git", "commit", "-m", data.commit], check=True)
            subprocess.run(["git", "push", "-u", "origin", data.brach], check=True)
        except Exception as E:
            print(f"Erro Al Execultar Script De git, Erro: {E}")      
            return False  
        
    def gitPull():
        path = os.path.join(data.path_local)
        if not path:return False
        try:
            subprocess.run(["git","pull","origin","main"])
        except Exception as E:
            print(f"Erro Al Execultar Script De git, Erro: {E}")      
            return False  
        