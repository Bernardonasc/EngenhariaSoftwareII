# Track Review - EngSoft 2

## Integrantes do grupo
Bernardo Nunes

César Morais

Pedro Henrique Baptista

Tomas Lacerda

## Como rodar o projeto localmente

```bash
# 1. Clone o repositório
git clone https://github.com/Bernardonasc/EngenhariaSoftwareII
cd EngenhariaSoftwareII

# 2. Instale as dependências
pip install -r requirements.txt

# 4. Aplique as migrações do banco de dados
python manage.py makemigrations
python manage.py migrate

# 5. Execute o servidor local
python manage.py runserver

# 6. Acesse no navegador
# http://127.0.0.1:8000
```

## Explicação do sistema

Track Review é uma plataforma feita por fãs de música, para fãs de música. Aqui, você pode avaliar seus álbuns favoritos, escrever resenhas e compartilhar suas opiniões com o mundo.

Com integração ao catálogo do Deezer, é possível buscar álbuns diretamente da plataforma, atribuir uma nota de 0 a 5 estrelas e escrever sua análise — tudo de forma simples e intuitiva.

A aplicação também conta com abas por estilo musical, facilitando a navegação por gêneros e a descoberta de novos álbuns dentro dos seus gostos. Por fim, o sistema inclui autenticação de usuários, garantindo que suas reviews fiquem salvas e acessíveis como um histórico pessoal.

## Tecnologias utilizadas

### Django
Django é um framework web de alto nível para Python, projetado para facilitar o desenvolvimento de aplicações de forma rápida e estruturada. Ele oferece diversos recursos prontos, como sistema de autenticação, painel administrativo, integração com banco de dados, entre outros.

No Track Review, o Django foi utilizado para gerenciar as rotas, lidar com formulários, autenticar usuários, organizar o banco de dados e renderizar as páginas da aplicação. Isso permitiu focar mais na lógica da aplicação e menos na infraestrutura.

### Testes
Para garantir a estabilidade e o bom funcionamento da aplicação, utilizamos o framework pytest para escrever e executar nossos testes de unidade.

Para automatizar a execução dos testes, configuramos GitHub Actions. A cada push, a suíte de testes é executada automaticamente em um ambiente controlado. Isso ajuda a identificar rapidamente possíveis quebras no código e garante que novas funcionalidades não afetem o que já funciona.