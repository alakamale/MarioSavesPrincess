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

## Endpoints 3
I tried using some HTML+JS+CSS to make it little interactive.
Here, 
1. Enter the grid size int the text box.
2. Click on "Click here for Grid Details"
3. After filling, hit submit.
4. It will take you to gui solution page.
