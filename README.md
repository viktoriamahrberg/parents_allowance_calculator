# Parent's Allowance Calculator

## About

In Sweden, amongst other countries, a parental allowance is calculated based on your annual salary. 
**Background**
As a soon-to-be parent you may wonder how to financially structure your time on leave, in order to take care of your newborn. 
Sweden offers 420 days to be equally split between the parents but the allowance is based on each individual's income. When you plan your maternity or paternity leave you may want to know how much your on-leave income will be.

The allowance is in this app calculated on the Swedish structure where you get 80% of your annual gross salary, with 30% tax deducted on top of that.
This leaves you with your annual allowance.

Depending on how many days a month you want to take out, the calculations will give you your decided monthly allowance. 

## User Experience

### User Stories
* As a user I want to:
    * Find out about my total yearly allowance when going on maternity-/paternity leave
    * Find out how much I could get each month in order to plan my finances

## Features

## Input data

Input data features in terms of:
1. Input yearly gross salary
2. Input days per month to be on-leave
3. Input month to base calculations on

### Calculations

* calculate_annual_allowance fucntion is calculating the total yearly allowance 
* calculate_monthly_allowance function is calculating the requested monthly allowance

### Features to be implemented
Connect an API in form of Google Sheets which:
    * Collects the users data for the business owner
    * Analyse the users data for statistics

## Technologies Used

### Languages
    * [Python](https://www.python.org/)

### Frameworks, Deployment, Libraries
    * [GitHub](https://github.com/)
    * [Gitpod](https://gitpod.io/)

## Testing

### Functionality







--------------------



![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome Vikmah,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **August 17, 2021**

## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!