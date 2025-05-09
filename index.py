from data import data
from tool import tool
from time import sleep

def Start():
    try:
        tool.clear_screen()
        remote_link = input("Digite O Link Do Repositorio: ").strip()
        if remote_link is None or remote_link == "":
            sleep(2)
            Start()
            return
        
        commit = input("Digite O commit: ").strip()
        if commit is None or commit == "":
            sleep(2)
            Start()
            return
        
        data_local = data(remote_link=remote_link,commit=commit)
        tool.gitInit(data_local)
        return
    except Exception as E:
        print(f"Erro Nos Inputs, Erro: {E}")  
        sleep(2)    
        Start()
        return

if __name__ == "__main__":
    Start()