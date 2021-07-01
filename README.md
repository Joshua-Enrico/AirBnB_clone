# Hbnb console

![airbnb_img](https://imgur.com/symULZt)

The AirBnB clone project starts now until… the end of the first year. The goal of the project is to deploy on your server a simple copy of the AirBnB website.
After 4 months, you will have a complete web application composed by:

* A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
* A website (the front-end) that shows the final product to everybody: static and dynamic
* A database or files that store data (data = objects)
* An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

![steps](https://imgur.com/9WkM9nn)

And the final data diagram looks like this:

![data_diagram](https://imgur.com/I7VURNR)

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

## Airbnb files structure

##|File|Description|Recommendations
---|---|---|---
0|[console.py](./console.py)|command interpreter to manage your AirBnB objects|Create a new object (ex: a new User or a new Place) ; Retrieve an; object from a file, a database etc… ; Do operations on objects (count, compute stats, etc…); Update attributes of an object; Destroy an object
1|[models](./models)|directory of class|-
2|[tests](./tests)|directory of tests of the console and classes|-

## 0.Console and how to executes

you can run it writting ```./console.py``` in your terminal and you will enter to the command interpreter like you see in this example, after it you can use the commands allowed for the terminal.

```
guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) help quit
Quit command to exit the program

(hbnb) 
(hbnb) 
(hbnb) quit 
guillaume@ubuntu:~/AirBnB$ 
```

##|Commands|how to use it|Instance form|Description
---|---|---|---|---
0.0|quit|```quit```||Exit the program
0.1|EOF|```EOF```||Exit the program
0.2|empty line|``` ```||not do nothing
0.3|create|```create <class name>```|| create an instance of the class
0.4|show|```show <class name> <id number>```|```<class name>.show(<id>)```|Prints the string representation of an instance based on the class name and id
0.5|destroy|```destroy <class name> <id number>```|```<class name>.destroy(<id>)```|Deletes an instance based on the class name and id (save the change into the JSON file)
0.6|all|```all``` or ```all <class name>```|```<class name>.all()```|Prints all string representation of all instances based or not on the class name
0.7|update|```update <class name> <id number> <attribute to update> "<new value of attribute>"```|simple form:```<class name>.update(<id>, <attribute name>, <attribute value>)``` update more than 1 attribute(using dictionaries): ```<class name>.update(<id>, <dictionary representation>)```|Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). If there are more commands, the command interpreter will only count the first attribute with its value
0.8|count|```count <class name>```|```<class name>.count()```|retrieve the number of instances of a class

##|Allowed classes
---|---
a|BaseModel|```BaseModel```
b|User|```User```
c|Place|```Place```
d|State|```State```
e|City|```City```
f|Amenity|```Amenity```
g|Review|```Review```
h|User|```User```

## 1.Models file Structure

##|File|Description|Recommendations
---|---|---|---
1.0|[engine](./models/engine)|directory of Store first object|The first way you will see here is to save these objects to a file with dictionaries: ```<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> <class 'BaseModel'>```
1.1|[__init__.py](./models/engine/__init__.py)|initialization code for the package|files are required to make Python treat the directories as containing packages; this is done to prevent directories with a common name
1.2|[amenity.py](./models/engine/amenity.py)||
1.3|[base_model.py](./models/engine/base_model.py)||
1.4|[city.py](./models/engine/city.py)||
1.5|[place.py](./models/engine/place.py)||
1.6|[review.py](./models/engine/review.py)||
1.7|[state.py](./models/engine/state.py)||
1.8|[user.py](./models/engine/user.py)||

### 1.0.Engine structure

##|File|Description|Recommendations
---|---|---|---
1.0.0|[__init__.py](./models/engine/__init__.py)|initialization code for the package|files are required to make Python treat the directories as containing packages; this is done to prevent directories with a common name
1.0.1|[file_storage.py](./models/engine/file_storage.py)||

## 2.Tests file Structure and how to compile

All files, classes, functions must be tested with unit tests
```
guillaume@ubuntu:~/AirBnB$ python3 -m unittest discover tests
...................................................................................
...................................................................................
.......................
----------------------------------------------------------------------
Ran 189 tests in 13.135s

OK
guillaume@ubuntu:~/AirBnB$
```

Unit tests must also pass in non-interactive mode:

```
guillaume@ubuntu:~/AirBnB$ echo "python3 -m unittest discover tests" | bash
...................................................................................
...................................................................................
.......................
----------------------------------------------------------------------
Ran 189 tests in 13.135s

OK
guillaume@ubuntu:~/AirBnB$
```

##|File|Description|Recommendations
---|---|---|---
2.0|[test_models](./tests/test_models)||
2.1|[__init__.py](./tests/__init__.py)|initialization code for the package|files are required to make Python treat the directories as containing packages; this is done to prevent directories with a common name
2.2|[test_console.py](./tests/test_console.py)||

### 2.0.Test_models structure

##|File|Description|Recommendations
---|---|---|---
2.0.0|[test_engine](./tests/test_models/test_engine)||
2.0.1|[__init__.py](./tests/test_models/__init__.py)|initialization code for the package|files are required to make Python treat the directories as containing packages; this is done to prevent directories with a common name
2.0.2|[test_amenity.py](./tests/test_models/test_amenity.py)||
2.0.3|[test_base_model.py](./tests/test_models/test_base_model.py)||
2.0.4|[test_city.py](./tests/test_models/test_city.py)||
2.0.5|[test_place.py](./tests/test_models/test_place.py)||
2.0.6|[test_review.py](./tests/test_models/test_review.py)||
2.0.7|[test_state.py](./tests/test_models/test_state.py)||
2.0.8|[test_user.py](./tests/test_models/test_user.py)||

#### 2.0.0.Test_engine structure

##|File|Description|Recommendations
---|---|---|---
2.0.0.0|[__init__.py](./tests/test_models/test_engine/__init__.py)|initialization code for the package|files are required to make Python treat the directories as containing packages; this is done to prevent directories with a common name
2.0.0.1|[test_file_storage.py](./tests/test_models/test_engine/test_file_storage.py)||
