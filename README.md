# Images Dataset Builder

**Image Dataset Builder** is an open source tool that you can use to build your own images datasets using a python web crawler.

- [Installation](#installation)
- [Usage](#usage)


***
## Installation
```
git clone GITHUB_LINK_HERE
cd folder-master/
pip install -r requirements.txt
```

***
## Usage

Download 100 images of human faces & 100 images of roads:
```
python3 main.py -s "Human Faces", "Roads" -n 100
```

**Options**
| Option               |Description |Example|
|----------------------|------------|-|
|``-h`` ``--help``     | Show help message. | ``-h``
|``-s`` ``--search``   | Select one or multiple classes to search. | ``-s "classe1", "classe2"...``
|``-n`` ``--number``   | Select number of element(s) to search per class.<br>If not specified, default value will be **100**.| ``-n 150``
|``-o`` ``--output``   | Select the output folder path.<br>If not specified, default value will be ``./Output/`` | ``-o path/to/folder/``
|``-d`` ``--dispatch`` | Dispatch downloaded files in different folders according to selected classes.<br> Will create a folder for each specified class, changing spaces by dots. | ``-d``


***
