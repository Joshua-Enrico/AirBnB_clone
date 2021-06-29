# Airbnb console

![airbnb_img](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210629%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210629T042130Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=366e77e47a1ee533ae4802f4bd603e5b1d1c213b3c58889ee22debac45e72c9b)

The AirBnB clone project starts now until… the end of the first year. The goal of the project is to deploy on your server a simple copy of the AirBnB website.
After 4 months, you will have a complete web application composed by:

* A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
* A website (the front-end) that shows the final product to everybody: static and dynamic
* A database or files that store data (data = objects)
* An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

![steps](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/d2d06462824fab5846f3.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210629%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210629T042130Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=50b69fd1b2ff10699ea29d046ad4d3fae31ceabf77f6b7b164eeef066cdc33fd)

And the final data diagram looks like this:

![data_diagram](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/99e1a8f2be8c09d5ce5ac321e8cf39f0917f8db5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210629%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210629T042130Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=b21e6f1a6bb6f56dd0d0c8f99eaf1b84ed6471f457b93ec0d2c4ba1a76c0e3e4)

# First step and GOAl of this repository: Write a command interpreter to manage your AirBnB objects.

This is the first step towards building the first full web application: the AirBnB clone. This first step is very important because we will use what we build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

## What’s a command interpreter?

Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object

## Resources
Read or watch:

* cmd module
* packages concept page
* uuid module
* datetime
* unittest module
* args/kwargs
* Python test cheatsheet

## Learning Objectives
* How to create a Python package
* How to create a command interpreter in Python using the cmd module
* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* How to manage datetime
* What is an UUID
* What is *args and how to use it
* What is **kwargs and how to use it
* How to handle named arguments in a function

## Execution

The hbnb command interpreter should work like this in interactive mode:

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

But also in non-interactive mode: (like the Shell project in C):

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

All tests should also pass in non-interactive mode: ``` $ echo "python3 -m unittest discover tests" | bash ```
