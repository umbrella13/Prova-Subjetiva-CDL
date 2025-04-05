"""
Nome: Italo de Sousa Batista
Link do GitHub: 
https://github.com/umbrella13/Prova-Subjetiva-CDL.git
"""



# importando a biblioteca para manipulação de caminhos
import os      

# bibliotecas para ler o tipo de arquivo
from docx import Document  # ler arquivos .docx
import PyPDF2              # ler arquivos .pdf

# definindo o caminho da pasta "Documentos" no usuário do windows
# os.path.expanduser("~") retorna o diretório home do usuário e por ai junta com "Documents"
# assumindo que o arquivo "documentos" éo Documentos do windows
documentos_dir = os.path.join(os.path.expanduser("~"), "Documents")


# definindo o nome do arquivo que vai ser procurado sem a extensão
nome_arquivo_base = "dados"


# criando váriaveis para os caminhos de .pdf e .docx
caminho_pdf = os.path.join(documentos_dir, f"{nome_arquivo_base}.pdf")
caminho_docx = os.path.join(documentos_dir, f"{nome_arquivo_base}.docx")

# lista para armazenar todos os números do arquivo que vai ser lido
numeros = []

# função auxiliar para extrair números de uma string 
def extrair_numeros(texto):
    
    #percorre a string caractere por caractere e extrai as sequências de dígitos,
    #convertendo a inteiros.
    
    nums = []         # lista que armazenará os números extraídos
    numero_str = ""   # string que armazena os digitos
    
    # checa por cada caractere na string
    for char in texto:
        if char.isdigit():
            # se o caractere for dígito, armazena na variável
            numero_str += char
        else:
            # se não for dígito e já tiver acumulado algum número, converte e armazena
            if numero_str:
                nums.append(int(numero_str))
                numero_str = ""
    # saso a string termine com dígitos, adiciona o número final à lista
    if numero_str:
        nums.append(int(numero_str))
    return nums

# função para ler arquivos .pdf e extrair números 
def ler_pdf(caminho):
    try:
        # abre o arquivo .pdf no modo binário
        with open(caminho, 'rb') as file:
            leitor = PyPDF2.PdfReader(file)  # cria o objeto leitor do PDF
            # checa por cada página do PDF
            for pagina in leitor.pages:
                texto = pagina.extract_text()  # Extrai o texto da página
                if texto:
                    # divide o texto em linhas e extrai números de cada linha
                    for linha in texto.strip().splitlines():
                        encontrados = extrair_numeros(linha)
                        # adiciona os numeros achados na lista global
                        numeros.extend(encontrados)
    except Exception as e:
        print(f"erro ao ler .pdf: {e}")

# função para ler arquivos .docx e extrair números 
def ler_docx(caminho):
    try:
        doc = Document(caminho)  # abre o arquivo .docx
        # checa por cada parágrafo do documento
        for paragrafo in doc.paragraphs:
            linha = paragrafo.text.strip()  # remove espaços em branco do começo ao fim do arquivo
            encontrados = extrair_numeros(linha)
            # adiciona os números achados a lista global
            numeros.extend(encontrados)
    except Exception as e:
        print(f"erro ao ler .docx: {e}")

# verifica se o arquivo existe e chama a função de leitura apropriada 
if os.path.exists(caminho_pdf):
    print(f"arquivo .pdf encontrado em: {caminho_pdf}")
    ler_pdf(caminho_pdf)
elif os.path.exists(caminho_docx):
    print(f"arquivo .docx encontrado em: {caminho_docx}")
    ler_docx(caminho_docx)
else:
    print("arquivo 'dados.pdf' ou 'dados.docx' não encontrado na pasta 'Documentos' do usuário.")
    exit()

#  cálculo das estatísticas 
if not numeros:
    print("nenhum número foi encontrado no arquivo.")
else:
    # cálculo da média: soma dos números dividido pela quantidade
    media = sum(numeros) / len(numeros)
    
    # cálculo da mediana:
    numeros_ordenados = sorted(numeros)  # organiza os números
    n = len(numeros_ordenados)
    if n % 2 == 1:
        # se a quantidade for ímpar, a mediana é o valor do meio
        mediana = numeros_ordenados[n // 2]
    else:
        # se for par, a mediana é a média dos dois valores centrais
        mediana = (numeros_ordenados[n // 2 - 1] + numeros_ordenados[n // 2]) / 2

    # exibe os resultados
    print("\nestatísticas:")
    print(f"média: {media}")
    print(f"mediana: {mediana}")
    print(f"somatório: {sum(numeros)}")
    print(f"maior valor: {max(numeros)}")
    print(f"menor valor: {min(numeros)}")