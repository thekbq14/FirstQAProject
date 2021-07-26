# FirstQAProject - Athletic Scoreboard

**Introduction**

**Objective**

The objective of this project was to create a functioning CRUD (Create, Read, Update and Delete) Application in Python, using the Flask Micro-framework. Alongside, this other requirements are needed, such as a Tracking board, be that on either Trello or Jira, a relational database with at least one many to one database being produced. A risk assessment, automated tests, version source control through GitHub, clear documentation and finally testing, this could be either through integration tests on Selenium which uses a web driver to input results into forms, and/or Unit testing through Pytest which requires coding the desired outcome of a function. 

**Proposal**

My proposal for this is an athletic scoreboard. This is designed from the athletes point of view, where all of their scores from the events, distances, time, stadiums, surface that they've completed is displayed and done so digitally. Athletes can create new events, distances, time, stadiums and surfaces to the scoreboard as this will happen when they compete more. They can update any information that is wrong or outdated. Users also have the option to delete anything that they don't want to be displayed either. More importantly all these information can be read on there screens too.

**Diagrams**

**Risk Assessment**

![image](https://user-images.githubusercontent.com/57040413/126936103-f83ea507-6a87-41e1-b14d-cc3767fc92e8.png)
![image](https://user-images.githubusercontent.com/57040413/126936155-e2375e7a-94a7-4e06-a8e1-8825034f6e5b.png)
![image](https://user-images.githubusercontent.com/57040413/126936182-473f927f-56da-4479-9ea0-54c6178bf3cc.png)
![image](https://user-images.githubusercontent.com/57040413/126936223-f8518cd1-54aa-478b-8d6e-dec13d482eef.png)


**Continous Integration**

![Continuous Integration](https://user-images.githubusercontent.com/57040413/126934322-29c9f6d6-4a9a-4e38-b3a5-8d983d88ecf6.png)

Continous Integration is used in my project because it creates an integrated environment to development as everything is synced together. It also is rapid as well, because things such as files can be saved to VCS very quickly such as GitHub, at the same time this will allow automated testing in Jenkins.

**ERD**

![Simple Athletes](https://user-images.githubusercontent.com/57040413/126933916-b15e95db-599b-425f-bda1-c4035a00481a.png)

![Before Athletes (1)](https://user-images.githubusercontent.com/57040413/126934150-e4129c39-c35b-4336-aaa0-9c4e21e53c02.png)

![Athletes (1)](https://user-images.githubusercontent.com/57040413/126934190-353f2474-e9b8-4ee9-9bc1-f44ebd77d134.png)

My ERD is used to show the relationship between the different databases that are used. This is important so the database can be structured and planned better. For example in an ERD can show a many to one relationship or many to many relationship. Examples used above is many to many relationship. I have also decided to simplify the ERD, the bottom being the original one was pretty complex and confusing, but I have now only got one one to many relationship which is the minimum required for the project. It will also make the application easier to use as there are less options.

**Tracking Board**

https://trello.com/b/nVOIu7Pt/agile-sprint-board

Trello was used as a tracking board instead of Jira, due to it being lightweight and visually nice on the eye. A tracking board is also important as it makes sure that everything is being produced on time.

**Development**

**Application**

![image](https://user-images.githubusercontent.com/57040413/126936535-6fe1488d-4c8e-49d3-ab6e-113fa7886006.png)

On the application, first page the user will see is the home page. This has been designed in the mind that the user's have already logged in and that this what they first see. What they will be able to see is a list off all the different times, stadiums, events, surfaces and distances they have completed at. Users can update and change their screen by adding for example "/createevent/championships" and this will add a row containing championships. From here uses can then update the row for example by "/updatedistance/5000" to add to the length the person has ran in. Finally if a person wants to leave or stop doing a particular distance they can "/delete/idnumber" the id number referring to the number on the list the distance that one doesn't want to do anymore.

**Testing**

**Unit Testing**

![image](https://user-images.githubusercontent.com/57040413/126936292-d5b50544-3a5e-4434-9190-910e623de763.png)
![image](https://user-images.githubusercontent.com/57040413/126937797-47bbd3f5-6cbb-44f0-ac8a-9128856416a1.png)




Unit Testing was done so by testing each functions separately and seeing the results that was printed off and test to see if an exepected response to the assertion happens. These are run by the developer by using the "python3 -m pytest" command to test to see if the test will pass or not. Another similar command that can be used is "python3 -m pytest tests --cov=application --cov-report term-missing", this is done to test to see how much of the code are covered by the tests, this is sorted out by the higher the percentage the more code that are covered by the tests created. Another way that this can be done is through Jenkins which will run through a Git Webhook this will enable tests run automatically after every Git push.

**Integration Tests**

Integration Tests are used to test the whole program as a whole compared to just a function in Unit testing. Selenium can be used, this is done through installing it through requirements.txt on Visual Studio Code. This simulates a user go through the website by filling forms and clicking buttons. These can also be automated through Jenkins. This wasn't used in my application due to the fact that there was no buttons or forms used. Next time an application is created, more time will be given to allow forms and buttons to be produced and hence allow integration tests.

**Conclusion/Future Improvements**

Overall, do feel like that the program was a success, as at the end of the day it works and does what is required by the stackholders and users. However, if done again a lot of changes could be done to it, such as adding buttons and making the Application look more neat and tidy, this could have been done by adding CSS to add colour or just href  functions for buttons. This in turn would have made the selenium tests worthwhile to have been done as they need buttons and WTForms to work or be used to the best of there ability.
