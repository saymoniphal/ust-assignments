## Overview
This program reads inputs from file and perform the following concurrently:
- check word frequency
- check whether a given input is a valid password
- add value to queue, remove value from queue and display queue.

## Project structure
The project structure is as below:
<pre>
|-- README.md
|-- requirements.txt: #requirement file for required package to be installed for this program
|-- main.py
|-- src
    |-- word_frequency.py: #calculate words frequency(count) in a given string
    |-- test_word_frequency.py: #unit tests for word_frequency.py
    |-- check_pwd.py: #check password against certain predefined criterias
    |-- test_check_pwd.py: #unit tests for check_pwd.py
    |-- circular_queue.py: #implementation of circular queue using python dictionary
    |-- test_circular_queue.py: #unit tests for circular_queue.py
|-- data: #folder contains input files
    |--testfile.txt: #sample data as input to functions in main.py
</pre>

## Pre-requisite
pytest is used for unit tests each functions. The required `pytest` package is in `requirements.txt` file.
Run below command to install requirements:
```
pip install requirements.txt
```

## How to run project
#### Use Git to clone repository using via SSH:
Run command:
```
git clone git@github.com:saymoniphal/ust_assignments.git
```
#### Use github command CLI:
Run command:
```
gh repo clone saymoniphal/ust_assignments
```
#### Run program
Go to directory ust_assignments and run "main.py" script as follow:

- run with inputs from file
```
python3 main.py --filename data/testfile.txt
```
- run without any inputs from file
```
python3 main.py
```

#### Run unit tests
Each functions in src folder  has a unit test in test_*.py
Use pytest to run all unit test. Run below command:
```
pytest
```
Sample output:
````
moniphal@krypton:~/git-tree/ust_assignments$ pytest
================================================================================ test session starts =================================================================================
platform linux -- Python 3.11.2, pytest-7.2.1, pluggy-1.0.0+repack
rootdir: /home/moniphal/git-tree/ust_assignments
collected 14 items                                                                                                                                                                   

src/test_check_pwd.py ......                                                                                                                                                   [ 42%]
src/test_circular_queue.py .....                                                                                                                                               [ 78%]
src/test_word_frequency.py ...                                                                                                                                                 [100%]

================================================================================= 14 passed in 0.03s =================================================================================
```