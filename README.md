# Documentação do Projeto

Este documento descreve as etapas executadas no vídeo para criar, configurar e testar um projeto Python.

## Etapas Executadas

### 1. Clonar o Repositório

Clone o repositório usando o comando:

```bash
git clone https://github.com/LuizEduardoMM/Atv2_Teste_Software_2024_Marrano_Eduardo/tree/main
```

### 2. Criar e ativar ambiente virtual

```bash
(Se não tiver instalado dar pip install venv)
python -m venv venv
Para ativar no windows usar: venv\Scripts\activate
Linux/Mac: source venv/bin/activate
```
### 3. Instalar dependências

```bash
(Se não tiver o poetry instalado dar pip install poetry)
poetry install
```

### 4. Rodar os casos de testes

```bash
pytest --cov=pycpfcnpj  (Caso queira gerar um html usar esse a seguir)--cov-report html 
```

### 5. Configurar e rodas casos de mutação

```bash
pip install mutmut
mutmut run --paths-to-mutate=pycpfcnpj/ 
Para gerar a pagina com os resultados mais a fundo: 
mutmut html      
```

### 6. Analisar Resultados dos Testes


### 7. Ajustar Funções e Validações
