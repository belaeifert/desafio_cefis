# Desafio CEFIS

Manipulação da API para processo seletivo.

1. Clone o repositório
2. Crie um virtualenv com python 3.6
3. Ative o virtualenv
4. Instale as dependências
5. Execute os testes
6. Execute o sevidor

```
git clone git@github.com:belaeifert/desafio_cefis.git desafio_cefis
cd desafio_cefis
python -m venv .desafio_cefis
source .desafio_cefis/bin/activate
pip install -r requirements.txt
python manage.py test
python manage.py runserver

```