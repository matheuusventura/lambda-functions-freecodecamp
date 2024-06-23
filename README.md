# 🌎🖥 Criando uma lista de despesas em Python
Aprendendo Funções Lambda em Python criando um software de despesas durante o curso Scientific Computing with Python da freecodecamp.org.
<br>
<br>
🗣️ [portuguese](https://github.com/matheuusventura/lambda-functions-freecodecamp) - [english](https://github.com/matheuusventura/lambda-functions-freecodecamp/blob/main/README-english.md)
<h3>O que são Funções Lambda?<h3></h3>
Lambda Functions são funções anônimas definidas usando a palavra-chave 'lambda'. Elas são geralmente usadas para criar pequenas funções de forma rápida, especialmente quando a função será usada apenas uma vez ou por um curto período de tempo.

<h3>Como funciona?</h3>
A sintaxe básica de uma função lambda é a seguinte:
<br>

```python
lambda argumentos: expressão
```
<b>Aqui, 'argumentos' são os parâmetros que a função aceita, e 'expressão' é o corpo da função que retorna um valor. A expressão deve ser uma única linha.</b>
<br>
<br>
A função lambda foi utilizada em duas funções no projeto. 'total_expenses(expenses)' para extrair o valor da despesa '(amount)' de cada dicionário na lista 'expenses'. A função map aplica a função lambda a cada elemento da lista, retornando um iterador de valores amount e a função sum soma todos esses valores.
<br>
<br>
Este é um software de despesas simples. Ele permite que o usuário adicione despesas, liste todas as despesas, calcule o total das despesas e filtre despesas por categoria.

```
Expense Tracker
1. Add an expense
2. List all expenses
3. Show total expenses        
4. Filter expenses by category
5. Exit
Enter your choice:
```

```
user input: 1
```

```
Enter amount: 200
Enter category: food
```

O programa apresenta o menu principal e solicita a escolha do usuário, onde entrada do usuário é 1, que corresponde à opção "Add an expense". A lista expenses agora contém uma despesa:

```python
[{'amount': 200, 'category': 'food'}]
```

então a função de listar todas as despesas imprime:

```All Expenses:
Amount: 200.0, Category: food
```

<hr>
<h4>👋😆 Essa foi minha terceira etapa do curso da freecodecamp, estarei publicando e explicando todos os projetos e minha progressão durante o andamento.</h4>
