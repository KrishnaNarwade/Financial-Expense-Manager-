# Financial-Expense-Manager-
Hi , This Repository contains Expense Manger Project using Python 
Overview of code Metrics :[![Quality gate](https://sonarcloud.io/api/project_badges/quality_gate?project=KrishnaNarwade_Expense-Manger-Advanced-Software-Engineering-Project)](https://sonarcloud.io/summary/new_code?id=KrishnaNarwade_Expense-Manger-Advanced-Software-Engineering-Project)

# General
This repository contains a simple Expense manager. You can track your expense and budget get to know where you are spending your money. It already comes with options of adding , deleting, modifying, getting current date of the puchase. 

You can find the Screenshot of GUI [Here](https://github.com/KrishnaNarwade/Financial-Expense-Manager-/blob/main/UML%20Diagrams/Expense%20Tracker%20Screenshot.png)

# 1 Git 
I am using Git to always push my code and required file.
I am regulary adding and updating file as per need and pushing the updates to github.
My git times can be seen at the contribution chart in GitHub and also in the below Chart.


### :fire: My Stats :
[![GitHub Streak](http://github-readme-streak-stats.herokuapp.com?user=KrishnaNarwade&theme=buefy-dark&hide_border=true)](https://git.io/streak-stats)

# 2 UML

I decided to draw 3 UML diagrams i.e 
1) [Activity Daigram](https://github.com/KrishnaNarwade/Expense-Manger-Advanced-Software-Engineering-Project/blob/main/UML%20Diagrams./UML%20Activity%20Diagram1.png):
This activity diagram shows progression and action of the Expense tracker tool.

2) [Use Case Diagram](https://github.com/KrishnaNarwade/Expense-Manger-Advanced-Software-Engineering-Project/blob/main/UML%20Diagrams./Use_Case_Daigram1.png):
This Use-case diagrams describe the high-level functions and scope of a Expense tracker tool.
It also shows interaction between User and System.

3) Component diagram (Still in progress.)
This Component diagram will show the components the expense tracker tool and how they are wired together.

# 3) DDD
Attaching the Darft version of the [DDD](https://github.com/KrishnaNarwade/Expense-Manger-Advanced-Software-Engineering-Project/blob/main/UML%20Diagrams./DDD%20Expense%20Tracker.jpg) diagram. 

# 4) Metrics

- Maintainability : [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=KrishnaNarwade_Expense-Manger-Advanced-Software-Engineering-Project&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=KrishnaNarwade_Expense-Manger-Advanced-Software-Engineering-Project)
- Security Rating : [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=KrishnaNarwade_Expense-Manger-Advanced-Software-Engineering-Project&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=KrishnaNarwade_Expense-Manger-Advanced-Software-Engineering-Project)
- Bugs : [![Bugs](https://sonarcloud.io/api/project_badges/measure?project=KrishnaNarwade_Expense-Manger-Advanced-Software-Engineering-Project&metric=bugs)](https://sonarcloud.io/summary/new_code?id=KrishnaNarwade_Expense-Manger-Advanced-Software-Engineering-Project)
- Vulnerabilities: [![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=KrishnaNarwade_Expense-Manger-Advanced-Software-Engineering-Project&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=KrishnaNarwade_Expense-Manger-Advanced-Software-Engineering-Project)
- Duplicated Lines (%) : [![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=KrishnaNarwade_Expense-Manger-Advanced-Software-Engineering-Project&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=KrishnaNarwade_Expense-Manger-Advanced-Software-Engineering-Project)
- Reliability Rating : [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=KrishnaNarwade_Expense-Manger-Advanced-Software-Engineering-Project&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=KrishnaNarwade_Expense-Manger-Advanced-Software-Engineering-Project)
- Lines of Code : [![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=KrishnaNarwade_Expense-Manger-Advanced-Software-Engineering-Project&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=KrishnaNarwade_Expense-Manger-Advanced-Software-Engineering-Project)

# 5) Clean Code Development
**Readability:** The codes written are easy to understand and follow, using clear and meaningful names, concise expressions, and consistent indentation.
                 Before each function a comment is written to explain what the function is exactly doing!
   
**Simplicity:** The codes are simple with avoiding over-engineering and unnecessary complexity.

**DRY (Don't Repeat Yourself):** Avoiding duplication of code, by creating reusable functions, modules, or libraries.
DRY stands for don't repeat yourself. The principle is very important in my opinion, because repition of code is easily avoidable and makes the code very hard to maintain. Two common rules to make sure to apply DRY is to define constants for values which occur frequently. Another is to use functions/classes/methods which increase the abstraction level of the code, so that it becomes reusable by design.
As also seen in my sonacloud metrics : [![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=KrishnaNarwade_Financial-Expense-Manager-&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=KrishnaNarwade_Financial-Expense-Manager-)


**Test-Driven Development (TDD):** Writing automated tests before writing the code, to ensure that the code works as expected and is easy to maintain.

**Modularity:** Breaking the code into smaller, self-contained modules that can be easily tested, reused, and combined in different ways.

# 6) Build Management
Yet to be done.
# 7) Tests 
For test, I am using python unittest modules , which provides functionality for creating and running tests, such as assert methods for testing conditions, test fixtures for setting up and tearing down test environments. 

For this project 2 Small Unittest are written for the Backend database : 
1) Test 1 : This test case calculates the total remaining balance of the records stored in the database. By default, the total Balance is 5000€
2) Test 2 : This test case fetches all the records stored in the database and verify if we have the same record as we expect.

You can find the link below.
[DB_UNITTEST](https://github.com/KrishnaNarwade/Financial-Expense-Manager-/blob/main/DBUnitest.py)

# 8) Continuous Delivery
Yet to be done.
# 9) IDE
I choosed Visual studio as an IDE for this Project
VS Code helps you be instantly productive with syntax highlighting, bracket-matching, auto-indentation, box-selection, snippets, and more

My Faviourite Shortcut tools are 
1) ctrl + L : It allows me to clear the output console
2) Alt+Click : It Inserts a cursor

# 10) Domain Specific Language  

My DSL is realted to my Expense Tracker project.

Here I have a written small Domain Specific language which just take all the expenses details from the [grocery_expenses](https://github.com/KrishnaNarwade/Financial-Expense-Manager-/blob/main/grocery_expenses.dsl) and Do sum of all yours expenses which you have added in the file. It also shows you what item were purhcased and highest purchase amount of individual product.

For it's Interpreation I have used python language you can find the code here [grocery_expenses_interpreter](https://github.com/KrishnaNarwade/Financial-Expense-Manager-/blob/main/grocery_expenses_interpreter.py)


# 11) Functional Programming


[main_expense_manager](https://github.com/KrishnaNarwade/Financial-Expense-Manager-/blob/main/main.py)

[Backend_Database_code](https://github.com/KrishnaNarwade/Financial-Expense-Manager-/blob/main/mydb.py)
