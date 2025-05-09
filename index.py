from data import data
from tool import tool
from time import sleep
import argparse

#Este code n ficou dos melhores , porem escrivi equanto apredia o argparse ent ta de boa :)

def Start():
    try:
        args = tool.args()
        tool.clear_screen()
        if not args.push:
            remote_link = input("Digite O Link Do Repositorio: ").strip()
            if remote_link is None or remote_link == "":
                sleep(2)
                Start()
                return
        else:
            remote_link = ""
        
        commit = input("Digite O commit: ").strip()
        if commit is None or commit == "":
            sleep(2)
            Start()
            return
        
        data_local = data(remote_link=remote_link,commit=commit)
        if args.push:
            if tool.gitPush(data_local):
                print("="* 30 + "git_script" + "=" * 30)
                print("Alterações enviadas com sucesso!")
            return
        if tool.gitInit(data_local):
            print("="* 30 + "git_script" + "=" * 30)
            print("Repositório configurado e alterações enviadas com sucesso!")

        return
    except Exception as E:
        print(f"Erro Nos Inputs, Erro: {E}")  
        sleep(2)    
        Start()
        return
    

if __name__ == "__main__":
    Start()