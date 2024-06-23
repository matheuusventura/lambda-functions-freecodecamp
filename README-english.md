# 🌎🖥 Creating an Expense List in Python
Learning Lambda Functions in Python by creating an expense tracking software during the Scientific Computing with Python course from freecodecamp.org.
<br>
<br>
🗣️ [portuguese](https://github.com/matheuusventura/lambda-functions-freecodecamp) - [english](https://github.com/matheuusventura/lambda-functions-freecodecamp/blob/main/README-english.md) - [spanish](https://web.whatsapp.com/)
<h3>What are Lambda Functions?<h3></h3>
Lambda functions are anonymous functions defined using the 'lambda' keyword. They are typically used to create small, quick functions, especially when the function will be used only once or for a short period of time.

<h3>How do they work?</h3>
The basic syntax of a lambda function is as follows:
<br>

```python
lambda arguments: expression
```
<b>Here, 'arguments' are the parameters that the function accepts, and 'expression' is the body of the function that returns a value. The expression must be a single line.</b>
<br>
<br>
The lambda function was used in two functions in the project. 'total_expenses(expenses)' to extract the value of the expense '(amount)' from each dictionary in the list 'expenses'. The map function applies the lambda function to each element of the list, returning an iterator of amount values, and the sum function adds all these values together.
<br>
<br>
This is a simple expense tracking software. It allows the user to add expenses, list all expenses, calculate the total expenses, and filter expenses by category.

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

The program displays the main menu and prompts the user to make a choice, where the user input is 1, corresponding to "Add an expense". The expenses list now contains an expense:

```python
[{'amount': 200, 'category': 'food'}]
```

then the function to list all expenses prints:

```All Expenses:
Amount: 200.0, Category: food
```

<hr>
<h4>👋😆 This was my third step in the freecodecamp course, and I will be publishing and explaining all projects and my progression during the course.</h4>
