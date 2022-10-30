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

#### AWS Lambda deploy:
To begin this exercise, it should be assumed that I currently already have the appropriate permissions in AWS.

Case 1: Deploy using the AWS Console.

In the AWS Lambda console

1. If the function does not exist I must go to create a function and configure it.
1.1. In the code section, add the Python function
1.2. Configure in the respective triggers when the function is going to be executed
1.3. Configure in the destinations section the expected response that the function should evaluate
1.4. Configure other extra details such as environment variables, tags, etc.
1.5. When everything is ready, I will click on the deploy button
1.6. Test the function on AWS

2. If the function already exists, I need to search for the function in the list of deployed functions
2.1. In the section that I want to update, add the new information
2.2. When everything is ready, I will click on the deploy button
2.3. Test the function on AWS

Case 2: Deploy using a CI/CD tool that facilitates deployment (for this case I will say that I will use GitHub Actions and that it is already properly configured with AWS),

1. Make sure that the .yml file that aws would use for the deployment is ready.

2. Make sure that the requirements.txt file has all the modules that the deployment needs to run the application in the cloud

3. Make sure the python function works properly before being deployed

4. Push to the branch that expects to execute the .yml file

5. Check that the deployment was successful in GitHub Actions

6. Test the function on AWS

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