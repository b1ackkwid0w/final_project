# final_project

Note: Immediate updates to reservations.txt file may not be available due to Docker Container version update. Documentation suggests file mounting to solve issue. References attached:
https://github.com/docker/for-win/issues/5530
https://docs.docker.com/storage/bind-mounts/

Project: Trip Reservation System
Project Objectives
To further gain experience and develop skill working with Docker and Flask, or another language/platform chosen by the scrum team.
To further develop team chemistry and communication skill.
To further develop skill using agile project management and Jira
Description
In this project you will develop a web application using Flask in Docker or using a programming language/platform of the scrum team's choosing. This project will be similar to your project 3a as you will be able to use the same framework to build this application.

Scenario
You and a number of IT students are going to a ski trip/hackathon over winter break in Colorado. To manage sign ups, the program has asked your team to create a simple web based reservation system so that students can reserve their seats on the bus. Students will be charged different amounts based on the seat they pick. You will be provided with a pricing chart for the seating.

Video Demo


Requirements
Create a menu-driven reservation system using Flask Python, or another language with the ability to load and save reservations data to/from a file. The application should also allow an administrator to login to the admin portal where they can view the bus seating chart and see the total sales. The bus can seat up to 48 people, 12 rows of 4 seats each.

Your application will need to have the following functionality:

A. Create a seating chart and load the initial reservations
B. Display the main menu that asks the user whether they want to reserve a seat or log in as an administrator
C. If the user selects the admin login option they are taken to a page with a form to login. Information the user provides:
admin username
admin password
D. If the user successfully logs in a seating chart is displayed along with the total sales collected.
E. If the user selects the the reservation option they are taken to a page with a form to reserve a seat. Information the user provides
first name
last name
seat row
seat column
F. Display a flight chart
G. Calculate and get the total sales for the flight when the user successfully logs in as an admin
H. Create and print a reservation code for the user when the user successfully makes a reservation
I. Save the reservation in formation the reservation.txt (first name, seat row, seat column, e_ticket number)
J. Each page should have a link to the main option page.
Cost Matrix: You will need pricing a matrix to calculate sales for the flight. The following python function will create a 12 x 4 cost matrix which represents the cost of each seat on the flight. You should use this code in your project.

'''
Function to generate cost matrix for flights
Input: none
Output: Returns a 12 x 4 matrix of prices
'''
def get_cost_matrix():
    cost_matrix = [[100, 75, 50, 100] for row in range(12)]
    return cost_matrix
Note: If you develop in a language other than python you will have to implement the same same pricing scheme.

Project Tasks
Download the project Code for this project
Develop your application
What to Submit
Download the project Code
Download Project Code Download Download Project Code

The docker-compose command will create a container named "bus-trip-4320" for the application and set the working folder for the project as well. The application will be visible at http://0.0.0.0:5002/ (Links to an external site.) when running. 

Developing The Application
Each scrum team can decide to develop the application using Flask/Python or another language such or a LAMP or a MEAN stack. The scrum master must communicate to the professor which language/platform the team will be using to determine if it is appropriate. Regardless of the platform, the application must meet the requirements listed above.

What to submit
Create a scrum project in Jira: Create a scrum project in Jira and add the professor as a team member to the project (culmerk@missouri.edu). The team can organize its sprints as it sees fit.

Submit:

a pdf report to Canvas which should include
Screenshots of your scrum dashboard during the process, especially through each of your sprints
Screenshots of your burndown chart(s)
A summary of the team’s communication plan
A “lessons learned” section
A link to a Github repository to download the completed project
Choose a submission type
