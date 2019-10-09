# MarioSavesPrincess
Mario and the princess are trapped in a square grid (N*N), Mario needs to reach the princess with minimum number of steps (shortest paths), while avoiding any obstacles

# Requirements
- flask
- jsonify
- flask_sqlalchemy 
- datetime
- werkzeug

# How to Execute
```python run.py```<br/>

## Task List
- First task : Mario saving the princess
- Second task : API and Database
- Third task : Interactive App

# Results
# Task 1 
Takes two arguments ***glen*** and ***grid***, Validates and returns all possible short paths. </br>
The ***glen*** refers to the size of the grid, and the ***grid*** is a string.
### How to execute
* $ python pathFinder.py --glen <> --grid  <'' '' ''> </br>
Example, </br>
``` $ python pathFinder.py --glen 3 --grid '--m' '-x-' '-p-' ``` </br>
```[('DOWN', 'DOWN', 'LEFT')]```

# Task 2
## Endpoints 1
Solution to first task
#### /mario/<<int:glen>>/< grid>
The ***glen*** refers to the size of the grid, and the ***grid*** is a string of comma separate rows. <br/>

* /mario/3/--m,-x-,-p-
 ```json
[
  [
    "DOWN",  
    "DOWN", 
    "RIGHT"
  ]
]
```

* /mario/4/--m-,-xx-,--p-,-x--
```json
[
  [
    "RIGHT", 
    "DOWN", 
    "DOWN", 
    "LEFT"
  ]
]
```

## Endpoints 2
Viewpoint for all logs in the database.
#### /log
This will return a json object of all the rows in the api database.

```json
[
    [
    "grid_map": "['---m', '---p', '----', '-x--']", 
    "grid_size": "4", 
    "short_path(s)": "[('DOWN',)]", 
    "time_log": "Tue, 08 Oct 2019 20:59:57 GMT"
  ], 
  [
    "grid_map": "['---m', '---x', '----', '-x-p']", 
    "grid_size": "4", 
    "short_path(s)": "[('LEFT', 'DOWN', 'DOWN', 'DOWN', 'RIGHT'), ('LEFT', 'DOWN', 'DOWN', 'RIGHT', 'DOWN')]", 
    "time_log": "Tue, 08 Oct 2019 21:00:12 GMT"
  ], 
  [
    "grid_map": "['--m', '-x-', '--p']", 
    "grid_size": "3", 
    "short_path(s)": "[('DOWN', 'DOWN')]", 
    "time_log": "Tue, 08 Oct 2019 21:03:43 GMT"
  ]
]
``` 

# Task 3
I tried using some HTML+JS+CSS to make it little interactive.
Here, 
1. Enter the grid size int the text box.

![1](https://user-images.githubusercontent.com/45611729/66444501-62055f00-ea3b-11e9-8c6f-b94749403b5e.PNG)

2. Click on "Click here for Grid Details"

![2](https://user-images.githubusercontent.com/45611729/66444583-ab55ae80-ea3b-11e9-8655-b588d53307a6.PNG)

3. After filling, hit submit.

4. It will take you to gui solution page.

![3](https://user-images.githubusercontent.com/45611729/66444614-c58f8c80-ea3b-11e9-8c1c-aefa7d4da0ba.PNG)

