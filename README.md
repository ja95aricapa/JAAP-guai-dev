# JAAP-guai-dev

#### Github:
<https://github.com/ja95aricapa/JAAP-guai-dev>

#### Description:
It is created to obtain a list of pairs of numbers that, when added, give the same value entered as the parameter to be evaluated.

#### Explanation:
The key to this function is in the difference between the entered number (sum_) and the value of the element that is at index n.

Since, if the sum of these two numbers returns to the value of sum_, it can be assumed that they are a suitable pair of numbers.

I used a hash table to store the values ​​of the list if the value difference is in the map, it means that it is a suitable pair with the current element.

Note: to avoid key duplicates in the map, I counted the frequency of each element in the list

#### LAMBDA:


#### Environment:
This project is interpreted/tested on Ubuntu 22 LTS using python3.9

#### Installation:
* Clone this repository: `git@github.com:ja95aricapa/JAAP-guai-dev.git`
* Activate virtualenv: `source venv/bin/activate`
* Activate local server: `python3 app.py`
* Open the web app in a browser: `http://0.0.0.0:8000/docs`

#### Bugs:
No known bugs at this time.

#### Authors:
Jaime Aricapa - [Github](https://github.com/ja95aricapa)

#### License:
Public Domain. No copy write protection.