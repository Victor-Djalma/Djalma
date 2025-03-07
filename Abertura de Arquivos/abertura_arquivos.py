import sys

# Nome do arquivo de configuração
CONFIG_FILE = "config.txt"
RESULTADO_FILE = "resultado.txt"

def ler_config():   # Função para ler o arquivo "config.txt" nesse arquivo está os parametros configurados
    """Lê o valor de 'num' no arquivo config.txt."""
    try:
        with open(CONFIG_FILE, "r") as arquivo:
            for linha in arquivo:        # For utilizado para a leitura de linha por linha do arquivo "config.txt"
                if linha.strip().startswith("num="):
                    try:
                        return int(linha.strip().split("=")[1])
                    except ValueError:
                        print(f"Erro: O valor de 'num' no {CONFIG_FILE} não é um número válido.")
                        sys.exit(1)
    except FileNotFoundError:            # Caso o arquivo "config.txt" não for encontrado
        print(f"Erro: Arquivo '{CONFIG_FILE}' não encontrado.")
        sys.exit(1)

    print("Erro: Parâmetro 'num=' não encontrado no arquivo de configuração.")
    sys.exit(1)

# Lê o número esperado de arquivos do arquivo de configuração
num_esperado = ler_config()

# Obtém os argumentos da linha de comando (nomes dos arquivos)
arquivos = sys.argv[1:]

# Verifica se a quantidade de arquivos fornecida está correta
if len(arquivos) != num_esperado:
    print(f"Erro: Esperado exatamente {num_esperado} arquivos, mas {len(arquivos)} foram fornecidos.")
    sys.exit(1)

# Cria o arquivo de resultado e escreve os conteúdos dos arquivos nele
try:
    with open(RESULTADO_FILE, "w") as resultado:
        for nome_arquivo in arquivos:
            try:
                with open(nome_arquivo, "r") as arquivo:
                    conteudo = arquivo.read()
                    resultado.write(conteudo + "\n")
            except FileNotFoundError:
                print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")
                sys.exit(1)
            except PermissionError:
                print(f"Erro: Sem permissão para ler '{nome_arquivo}'.")
                sys.exit(1)

    print(f"Conteúdo dos arquivos foi mesclado com sucesso em '{RESULTADO_FILE}'.")
except Exception as e:
    print(f"Erro ao criar o arquivo '{RESULTADO_FILE}': {e}")
    sys.exit(1)
