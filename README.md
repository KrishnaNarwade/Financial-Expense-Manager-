# Financial-Expense-Manager-
Hi , This Repository contains Expense Manger Project using Python 
Overview of code Metrics :[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=KrishnaNarwade_Financial-Expense-Manager-&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=KrishnaNarwade_Financial-Expense-Manager-)

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

3) [Component diagram](https://github.com/KrishnaNarwade/Financial-Expense-Manager-/blob/main/UML%20Diagrams/UML%20Component%20Diagram.png)
This Component diagram show the components the expense tracker tool and how they are wired together.

# 3) DDD
Attaching the Darft version of the [DDD](https://github.com/KrishnaNarwade/Expense-Manger-Advanced-Software-Engineering-Project/blob/main/UML%20Diagrams./DDD%20Expense%20Tracker.jpg) diagram. 

# 4) Metrics

- Maintainability : [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=KrishnaNarwade_Financial-Expense-Manager-&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=KrishnaNarwade_Financial-Expense-Manager-)
- Security Rating : [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=KrishnaNarwade_Financial-Expense-Manager-&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=KrishnaNarwade_Financial-Expense-Manager-)
- Bugs : [![Bugs](https://sonarcloud.io/api/project_badges/measure?project=KrishnaNarwade_Financial-Expense-Manager-&metric=bugs)](https://sonarcloud.io/summary/new_code?id=KrishnaNarwade_Financial-Expense-Manager-)
- Vulnerabilities: [![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=KrishnaNarwade_Financial-Expense-Manager-&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=KrishnaNarwade_Financial-Expense-Manager-)
- Duplicated Lines (%) : [![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=KrishnaNarwade_Financial-Expense-Manager-&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=KrishnaNarwade_Financial-Expense-Manager-)
- Reliability Rating : [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=KrishnaNarwade_Financial-Expense-Manager-&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=KrishnaNarwade_Financial-Expense-Manager-)
- Lines of Code : [![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=KrishnaNarwade_Financial-Expense-Manager-&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=KrishnaNarwade_Financial-Expense-Manager-)

# 5) Clean Code Development
**Readability:** The codes written are easy to understand and follow, using clear and meaningful names, concise expressions, and consistent indentation.
                 Before each function a comment is written to explain what the function is exactly doing! As one can see by the sonarcloud readibilty analysis [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=KrishnaNarwade_Financial-Expense-Manager-&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=KrishnaNarwade_Financial-Expense-Manager-)
   
**Simplicity:** The codes are simple with avoiding over-engineering and unnecessary complexity.

**DRY (Don't Repeat Yourself):** Avoiding duplication of code, by creating reusable functions, modules, or libraries.
Another is to use functions/classes/methods which increase the abstraction level of the code, so that it becomes reusable by design.
As also seen in my sonacloud metrics : [![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=KrishnaNarwade_Financial-Expense-Manager-&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=KrishnaNarwade_Financial-Expense-Manager-)

**Test-Driven Development (TDD):** Writing automated tests before writing the code, to ensure that the code works as expected and is easy to maintain. 
The test case code can be seen [here](https://github.com/KrishnaNarwade/Financial-Expense-Manager-/blob/main/DBUnitest.py) 

**Modularity:** The codes written are breaked down into smaller, self-contained modules that can be easily tested, reused, and combined in different ways.

# 6) Build Management
My build management is not alligned with this project.


I choosed Maven for build managemnt. As I started learning it , I found out that It works very well with JAVA projects. So I wrote a small Java project which can be found here and Completed it's built automation using Maven. 

The Main Java Program can be found [here](https://github.com/KrishnaNarwade/Financial-Expense-Manager-/blob/main/Java-Maven%20Project/AppTest.java).

The POM.Xml can be found [here](https://github.com/KrishnaNarwade/Financial-Expense-Manager-/blob/main/Java-Maven%20Project/pom.xml). 

The screenshot of the Maven Build can be found [here](https://github.com/KrishnaNarwade/Financial-Expense-Manager-/blob/main/Java-Maven%20Project/Maven-Build%20Screenshot.jpeg)

# 7) Tests 
For test, I am using python unittest modules , which provides functionality for creating and running tests, such as assert methods for testing conditions, test fixtures for setting up and tearing down test environments. 

For this project 2 Small Unittest are written for the Backend database : 
1) Test 1 : This test case calculates the total remaining balance of the records stored in the database. By default, the total Balance is 5000€
2) Test 2 : This test case fetches all the records stored in the database and verify if we have the same record as we expect.

You can find the link below.
[DB_UNITTEST](https://github.com/KrishnaNarwade/Financial-Expense-Manager-/blob/main/DBUnitest.py)

# 8) Continuous Delivery
For CICD , I decided to go with Jenkins. 

Jenkins can be used to automate tasks such as building, testing, and deploying software, as well as simplifying continuous integration and continuous delivery (CI/CD) processes.
It provides varierty of plugins do these process. 

For This Project I created 4 differnet Pipelines i.e. Checkout, Build, Test , Deploy (The app is not deployed , It was juts written as Echo in Jenkins)
The Build success screenshot can be found [here](https://github.com/KrishnaNarwade/Financial-Expense-Manager-/blob/main/CICD-%20Jenkins/Expense_tracker_Pipelinescreenshot.png)

You can also have a look at [config.xml](https://github.com/KrishnaNarwade/Financial-Expense-Manager-/blob/main/CICD-%20Jenkins/Exprense_tracker_config.xml) and [log file](https://github.com/KrishnaNarwade/Financial-Expense-Manager-/blob/main/CICD-%20Jenkins/Expense_tracker_log)


Also I wanted to learn how to integrate Maven so I interegrated small java written project build with Maven. 

It's Successful build can be found [here](https://github.com/KrishnaNarwade/Financial-Expense-Manager-/blob/main/CICD-%20Jenkins/Maven_Jenkins_Screenshot.png)

 These are [log](https://github.com/KrishnaNarwade/Financial-Expense-Manager-/blob/main/CICD-%20Jenkins/Maven_Jenkins_log) and [config.xml](https://github.com/KrishnaNarwade/Financial-Expense-Manager-/blob/main/CICD-%20Jenkins/java_maven_config.xml) files for it.



# 9) IDE
I choosed Visual studio as an IDE for this Project
VS Code helps you be instantly productive with syntax highlighting, bracket-matching, auto-indentation, box-selection, snippets, and more.

My Faviourite Shortcut tools are 
1) ctrl + L : It allows me to clear the output console
2) Alt+Click : It Inserts a cursor
3) Ctrl+Shift+N : It opens new window/instance
4) Ctrl+Shift+W : It Close window/instance
# 10) Domain Specific Language  

My DSL is realted to my Expense Tracker project.

Here I have a written small Domain Specific language which just take all the expenses details from the [grocery_expenses](https://github.com/KrishnaNarwade/Financial-Expense-Manager-/blob/main/grocery_expenses.dsl) and Do sum of all yours expenses which you have added in the file. It also shows you what item were purhcased and highest purchase amount of individual product.

For it's Interpreation I have used python language you can find the code here [grocery_expenses_interpreter](https://github.com/KrishnaNarwade/Financial-Expense-Manager-/blob/main/grocery_expenses_interpreter.py)


# 11) Functional Programming


[main_expense_manager](https://github.com/KrishnaNarwade/Financial-Expense-Manager-/blob/main/main.py)

[Backend_Database_code](https://github.com/KrishnaNarwade/Financial-Expense-Manager-/blob/main/mydb.py)
