import os
import platform
from dataclasses import dataclass
import subprocess
from data import data

@dataclass
class tool:
    def clear_screen():
        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')

    def gitInit(data:data) -> bool:
        path = os.path.join(data.path_local)
        if not path:return False
        try:
            subprocess.run(["git","init"])
            subprocess.run(["git", "branch", "-M", "main"], check=True)
            subprocess.run(["git", "remote", "remove", "origin"], check=True)
            subprocess.run(["git", "remote", "add", "origin", data.remote_link], check=True)
            subprocess.run(["git", "add", "."], check=True)
            subprocess.run(["git", "commit", "-m", data.commit], check=True)
            subprocess.run(["git", "push", "-u", "origin", "main"], check=True)
        except Exception as E:
            print(f"Erro Al Execultar Script De git, Erro: {E}")      
            return False  