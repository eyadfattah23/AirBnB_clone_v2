# AirBnB clone - Web framework

## Questions:

- **What are web application frameworks?**

  GeeksforGeeks describes ‘web application frameworks’ or ‘web frameworks’ as “a software framework that is designed to support the development of web applications including web services, web resources and web APIs”. In simple words, web frameworks are a piece of software that offers a way to create and run web applications. Thus, you don’t need to code on your own and look for probable miscalculations and faults.

  In earlier days of web app development, web frameworks were introduced as a means to end hand-coding of applications where just the developer of a particular app could change it. That was long ago, now we have web-specific languages and the trouble with changing an app’s structure is resolved because of the arrival of a general performance. Now, depending upon your task you may choose one web framework that fulfills all your requirements or converges multiple frameworks.

- **What is init.py for?**
  In Python, the **init**.py file is used to mark a directory as a Python package. It is used to initialize the package when it is imported.

  The **init**.py file can contain code that will be executed when the package is imported, as well as function definitions and variable assignments. It is a good place to put any code that you want to run when the package is first imported.

  For example, suppose you have a package called mypackage with the following structure:

`mypackage/
    __init__.py
    module1.py
    module2.py
    ...
`
If you want to import module1 from mypackage, you can do so using the following import statement:

`import mypackage.module1`

    When you run this import statement, Python will execute the code in **init**.py before it executes the import statement for module1. This can be useful if you want to do some initialization or setup before the other modules in the package are imported.

call remove() method on the private session attribute (self.\_\_session) is based on [tips](https://docs.sqlalchemy.org/en/13/orm/contextual.html) or close() on the class Session [tips(https://docs.sqlalchemy.org/en/13/orm/session_api.html)]
