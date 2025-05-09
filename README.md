# git\_start\_script

Script Python simples para automatizar a inicialização de repositórios Git.

Este script é útil para quem cria repositórios com frequência e deseja:

* Iniciar um repositório local
* Definir a branch `main`
* Puxar o histórico remoto (mesmo que tenha histórias diferentes)
* Configurar o `origin`
* Fazer `add`, `commit` e `push` automáticos

---

## 📁 Estrutura do projeto

```
git_start_script/
├── data.py
├── index.py
├── tool.py
├── git_script.bat       ← atalho opcional para rodar no CMD
└── README.md
```

---

## 🚀 Instalação e configuração no Windows

### 1. Requisitos

* Python 3.7+ instalado (e no PATH)
* Git instalado (e no PATH)

### 2. Clonar ou baixar o repositório

```bash
git clone https://github.com/SeuUsuario/git_start_script.git
cd git_start_script
```

### 3. (Opcional) Adicionar ao PATH

Assim você pode executar `git_script` de qualquer pasta.

#### a. Mover para uma pasta fixa

Ex: `C:\Scripts\`

#### b. Criar um atalho bat

Arquivo `git_script.bat`:

```bat
@echo off
python "C:\Scripts\git_start_script\index.py" %*
```

> Altere o caminho conforme onde salvou o script.

#### c. Adicionar ao PATH

1. Iniciar → pesquisar "variáveis de ambiente"
2. Clique em **"Editar variáveis de ambiente do sistema"**
3. Em "Variáveis do sistema" → **Path** → Editar → Novo
4. Adicione:

```
C:\Scripts
```

5. OK em todas as janelas.
6. Reinicie o CMD ou PowerShell.

---

## 🎯 Como usar

Abra o CMD ou PowerShell e execute:

```cmd
git_script
```

Siga os prompts:

```
Digite O Link Do Repositorio: https://github.com/SeuUsuario/novo-repo.git
Digite O commit: commit inicial
```

O script executa:

1. `git init`
2. `git branch -M main`
3. `git pull origin main --allow-unrelated-histories`
4. `git remote remove origin`
5. `git remote add origin <link>`
6. `git add .`
7. `git commit -m "<mensagem>"`
8. `git push -u origin main`

---

## 📝 Explicação do código

### index.py

```python
def Start():
    tool.clear_screen()
    remote_link = input("Digite O Link Do Repositorio: ").strip()
    commit = input("Digite O commit: ").strip()
    data_local = data(remote_link=remote_link, commit=commit)
    tool.gitInit(data_local)
```

* Limpa a tela
* Coleta link e commit
* Cria objeto `data`
* Chama a função `gitInit`

### data.py

```python
@dataclass
class data:
    commit: str
    remote_link: str
    path_local: str = os.path.abspath(__file__)
```

* Define estrutura de dados para armazenar commit, link remoto e path atual

### tool.py

```python
class tool:
    def clear_screen():
        ...

    def gitInit(data:data):
        subprocess.run(["git", "init"])
        subprocess.run(["git", "branch", "-M", "main"], check=True)
        subprocess.run(["git", "pull", "origin", "main", "--allow-unrelated-histories"], check=True)
        subprocess.run(["git", "remote", "remove", "origin"], check=True)
        subprocess.run(["git", "remote", "add", "origin", data.remote_link], check=True)
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", data.commit], check=True)
        subprocess.run(["git", "push", "-u", "origin", "main"], check=True)
```

* Função `gitInit` executa os comandos Git de forma automatizada

---

## 📆 Dicas de uso

* ✉️ Caso receba erro `Updates were rejected`, faça um `git pull` antes do push.
* ⚙️ Pode modificar a branch padrão para `master` alterando `main` nas chamadas.
* 📄 Recomendado adicionar `.gitignore` antes do commit.

---

## 📚 Licença

MIT License
(c) 2025 Seu Nome
