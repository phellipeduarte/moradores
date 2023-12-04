# moradores
Breve projeto python que tem o objetivo de ilustrar a facilidade de criar uma api REST utilizando flask-restful

---
## Como o projeto foi feito?

A partir da utilização do **flask-restful**, é possível:

- Criar rotas mais rapidamente
- Sempre usar os verbos do *HTTP* 
- Criar API's fáceis de alterar

Para fazer isso tudo, basta criar uma **classe**, e definir seus métodos como os verbos do *HTTP*. Nesse exemplo, eu utilizei a classe morador e estabeleci ela como um *"controller"*. Assim, quando quis criar uma rota para acessar um morador específico pelo *id*, apenas criei um método com nome *```GET```*. E esse padrão se repete por todo o exemplo. Depois disso, bastou utilizar:

```
    api.add_resource(Morador, "/<int:id>")
```

Para registrar o endereço de todos os verbos *HTTPs* da **classe** Morador. O mesmo foi feito para uma lista de moradores, ou seja, a classe Moradores. 

---

## Como rodar o projeto?

1. Instale o [python](https://www.python.org/downloads/)

2. Crie um ambiente virtual
```
python -m venv nome_do_ambiente
```

3. Ative o ambiente virtual
```
nome_do_ambiente\Scripts\activate
```

4. Com o [git](https://git-scm.com/downloads) instalado, clone esse repositório:

```
git clone https://github.com/phellipeduarte/moradores.git
```

5. Instale as dependências do arquivo requirements.txt, no terminal digite:

```
pip install -r requirements.txt
```

6. Com o terminal aberto no endereço da pasta do repositório baixado, digite:
```
python app.py
```
7. Por fim, basta fazer as requisições na ferramenta (ou navegador) que preferir 