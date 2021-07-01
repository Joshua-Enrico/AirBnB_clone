# Hbnb console

![airbnb_img](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210630%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210630T035621Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=96469635c43f46978fce60de40cc0f5ae7d3095d026fc36f76bbadb5fbb036f6)

The AirBnB clone project starts now until… the end of the first year. The goal of the project is to deploy on your server a simple copy of the AirBnB website.
After 4 months, you will have a complete web application composed by:

* A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
* A website (the front-end) that shows the final product to everybody: static and dynamic
* A database or files that store data (data = objects)
* An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

![steps](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/06fccc41df40ab8f9d49.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210701%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210701T003323Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=114311c3d3ee500da9c810064ec3a5bdf27f0357e307417615374a066b5427ef)

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

## Airbnb files structure

##|File|Description|Recommendations
---|---|---|---
0|[console.py](./console.py)|command interpreter to manage your AirBnB objects|Create a new object (ex: a new User or a new Place) ; Retrieve an; object from a file, a database etc… ; Do operations on objects (count, compute stats, etc…); Update attributes of an object; Destroy an object
1|[models](./models)|directory of class|-
2|[tests](./tests)|directory of tests of the console and classes|-

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

## 2.Tests file Structure

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
