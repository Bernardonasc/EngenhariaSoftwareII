## ✅ Como rodar o projeto localmente

```bash
# 1. Clone o repositório
git clone https://github.com/usuario/trackreview.git
cd trackreview

# 2. Crie e ative um ambiente virtual
python3 -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Aplique as migrações do banco de dados
python manage.py makemigrations
python manage.py migrate

# 5. Execute o servidor local
python manage.py runserver

# 6. Acesse no navegador
# http://127.0.0.1:8000
```
