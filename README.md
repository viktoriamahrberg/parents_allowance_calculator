# Parent's Allowance Calculator
A calculator generating your monthly parental allowance

![Am I responsive](/readme_content/am_I_responsive.png)

## About

In Sweden, amongst other countries, a parental allowance is calculated based on your annual salary. 

**Background:**
As a soon-to-be parent you may wonder how to financially structure your time on leave, in order to take care of your newborn. 
Sweden offers 420 days to be equally split between the parents but the allowance is based on each individual's income. When you plan your maternity or paternity leave you may want to know how much your on-leave income will be.

The allowance is in this app calculated on the Swedish structure where you get 80% of your annual gross salary, with 30% tax deducted on top of that.
This leaves you with your annual allowance.

Depending on how many days a month you want to take out, the calculations will give you your decided monthly allowance. 

The live link can be found here - [Parent's Allowance Calculator](http://parents-allowance-calculation.herokuapp.com/)

## Flowchart
![Flowchart](/readme_content/parent_allowance_flowchart.png)

## User Experience

### User Stories
* As a user I want to:
    * Find out about my total yearly allowance when going on maternity-/paternity leave
    * Find out how much I could get each month in order to plan my finances

## Features

### Input data

Input data features in terms of:
1. Input yearly gross salary

![Input salary](/readme_content/input_yearly_income.png)

2. Input days per month to be on-leave

![Input days](readme_content/input_days.png)

3. Input month to base calculations on

![Input month](/readme_content/input_month.png)

### Calculations

* Calculates the total yearly allowance 
* Calculates the monthly allowance based on users input days

### Features to be implemented
Connect an API in form of Google Sheets which:
* Collects the users data for the business owner
* Analyse the users data for statistics

Have a print or download your results option in the end of the program for user to hold on to.

## Technologies Used

### Languages
* [Python](https://www.python.org/)

### Frameworks, Deployment, Libraries
* [GitHub](https://github.com/)
* [Gitpod](https://gitpod.io/)

### Other
* [Lucidchart](https://www.lucidchart.com/pages/)

## Testing

### Functionality
* I used the deployed site to manually entering correct and incorrect data to see how my program responded. 
* I used the bug feature with breakpoints in Gitpod
* Frequently add print() in my functions to follow my code and values behaviour 

### Validator Testing
* I ran through my file in [PEP8 Online](http://pep8online.com/). No errors occured. 

![PEP8 validator](/readme_content/pep8_validator.png)


## Issues found during development

1.
I had issues with the while loop in get_income_data function and the data then being sent to validation_function, however I did not manage to get the return value be passed on to the calculation function in the very end of the program. 

![Functions](/readme_content/validate_data_function.png)

I at first solved this with a controversal function called [Walrus Operator](https://realpython.com/python-walrus-operator/) which in short assigns a value to a variable and then returns that value and was introduced to me by a Slack member. This code however was not passed the validation test in PEP8, so I wanted to re-write it.

![Walrus in commit](/readme_content/walrus_commit.png)

I went through the Love Sandwiches codes, went back several times to the While Loop / Try-Except and If statements on CI, asked the Slack community and researched online. 
I tried to troubleshoot to see where the value gone missing:

![None_value](/readme_content/none_value.png)

![Error message](/readme_content/error_message.png)

Finally I came to the conclusion to merge the two functions and write everything in get_data_function. Perhaps one would say that was a short-cut but I managed to solve the problem by myself. 

![Solution](/readme_content/solution.png)

2.
A Slack-member in peer-code-review found an error that I had missed, when entering a non-digit character.

![Error message](/readme_content/type_error.png)

He gave suggestion to try and insert an empty string before asking for input from user to clear out the user's input after each wrong run. I tried this back and fourth but could not make it work in my instance. 

![Empty string loop](/readme_content/empty_string_loop.png)

I then found the link on [StackOverflow](https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response) about asking user's input until valid response and took inspiration from there and tried to run the program until I got it right.

![Function result](/readme_content/function_result.png)


## Deployment

I followed below steps when deploying my project to Heroku, based on Code Institute instructions:

1. Remove un-needed import features in run.py file
2. Add to requirements.txt file:
    - pip3 freeze > requirements.txt
    - Commit changes to Github:
    - git commit -m "Add requirements for deployment”

In HEROKU after creating account:
1. "Create new App"
2. Give the App a unique name and enter region
3. Click on "Create App"
4. Click on "Settings" on your new App Dashboard
5. Scroll down to Config Vars where in my instance I only inserted KEY: PORT and VALUE: 8000 since I have no creds.json files to add.
6. Press Add-button
7. Scroll down to Buildpacks and press the icon for Python, click Save Changes, then press the icon for Nodejs and save changes. These Buildpacks need to be in below order:
    - Python
	- NodeJS
8. Go to Deploy section tab and scroll down to Deployment Method. I connected to my Github pages and could thereafter search for my Github Repository "Parents Allowance Calculator" and then click connect. 
9. Scroll down to Automatic and Manual Deploys sections. I clicked on Automatic Deployment so that my changes that I push to github automatically updates in Heroku. 
10. Then in the Manual Deploy section, press Deploy Branch
11. After project has been deployed successfully I clicked the View-button to see the program run in the terminal. 


## Credits

Special thank you to Dave Horrocks for his support in Slack and the Slack community that volontereed and gave thorough feedback on my Peer Code Review post. 

Below resources were used to improve my skills and find assistance:
* [StackOverflow](https://stackoverflow.com/questions/287871/how-to-print-colored-text-to-the-terminal) - Print Colored text

* [StackOverflow](https://stackoverflow.com/questions/3944655/testing-user-input-against-a-list-in-python) - Test user input against a list (my months)

* [StackOverflow](https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response) - Asking user for input
* [Code Institute - Love Sandwiches](https://github.com/Code-Institute-Solutions/love-sandwiches-p5-sourcecode/blob/master/02-accessing-user-data/02-validating-our-data-part-1/run.py) -
While Loop for input days 

* [FreeCodeCamp](https://www.freecodecamp.org/news/the-python-sleep-function-how-to-make-python-wait-a-few-seconds-before-continuing-with-example-commands/) - Delay print in the end of program with Sleep function








