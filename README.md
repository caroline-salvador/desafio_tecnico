DESAFIO TÉCNICO - INTRODUÇÃO
O projeto foi desenvolvido em Python e contêm um servidor HTTP que, para cada requisiçãoGET, retorna um JSON cuja chave extenso é a versão por extenso do número inteiro enviado no path. Os números podem estar no intervalo [-99999, 99999].

REQUISITOS 	
    Python 3.7
    Pip 19.3.1
    Virtualenv 16.7.9
    Flask 1.1.1

INSTALANDO O PYTHON
	Guias de instalação:
		Windows: https://python.org.br/instalacao-windows/
		Linux: https://python.org.br/instalacao-linux/
		MAC OS: https://python.org.br/instalacao-mac/
	
DOWNLOAD DO CÓDIGO
     git clone https://github.com/caroline-salvador/desafio_tecnico.git

AMBIENTE VIRTUAL
	1. No terminal, navege até a pasta do projeto
	2. Crie um ambiente virtual na pasta raiz do projeto executando o comando:
		virtualenv venv
	3. Ative o ambiente virtual usando o comando:
		souce venv/bin/activate (Linux ou macOS)
		venv/Scripts/activate (Windows)
	4. Instale os pacotes requeridos para o projeto executando o comando:
		pip install -r requirements.txt

EXECUTANDO O PROJETO
	1. Execute o projeto usando o seguinte comando: 
		python app.py

	2. O servidor estará disponível no seguinte endereço: 
		http://127.0.0.1:8000/
	
	3. Se a porta 8000 não estiver disponível, altere no arquivo app.py
		linha 114 => app_service.run(port=8000)

TESTES UNITÁRIOS
	Verifica o status de resposta do servidor
	Verifica os valores limites do intervalo definido
	Verifica valores fora do intervalo definido
	Verifica a versão por extenso do número inteiro
	
	Executar teste:	
		1. Comente a linha 114 => app_service.run(port=8000) no arquivo app.py antes de executar o arquivo test.py
		2. Execute o teste usando o seguinte comando:
			python test.py

