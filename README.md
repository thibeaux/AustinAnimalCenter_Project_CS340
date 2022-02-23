### Assignment questions
Q: How do you write programs that are maintainable, readable, and adaptable? Especially consider your work on the CRUD Python module from Project One, which you used to connect the dashboard widgets to the database in Project Two. What were the advantages of working in this way? How else could you use this CRUD Python module in the future?

A: The way that i make my programs maintainable is through the use of classes, functions, and using good naming schemes. This allows the code to be more modular and readable. The other way is making python modules that provide functionlity to the webpages. In the future I could add to this module with some more advanced querying and I could use this to create more pages for this web application.

Q: How do you approach a problem as a computer scientist? Consider how you approached the database or dashboard requirements that Grazioso Salvare requested. How did your approach to this project differ from previous assignments in other courses? What techniques or strategies would you use in the future to create databases to meet other client requests?

A: I broke up the project into sections. First I learned how to use MongoDB, then I made the python module, and finally I assembled the front end web page using the Dash framework. I'd say the main thing that helped my problem solve was the use of the official documentation for the framework and for MongoDB. When I was new to programming, I didn't really see much value in reading the official documentation carefully and kind of just went at the project looking for preassembled code. Not totally off, but now, I can start to see a sense of maturity when approaching projects and taking time to see how the creators of the framework or API intended you to use the project and to understand how the solutions work. 

Q: What do computer scientists do, and why does it matter? How would your work on this type of project help a company, like Grazioso Salvare, to do their work better?

A: A computer scientist is someone who takes real world problems and tries to solve it using computers. It is a specialized area, but can be very broad. One way to help a copany like Grazioso Salvre is to help them gather and organzie data from thier area. Once this is obtained the company can use a bit of data analysis to help them better understand and find trends that may be to thier benefit. Furthermore, we can utilize this large amount of data to help them find perfect matches for te animals they are looking for and make predictions on what dogs are going to be successful. 


## **About the Project/Project Title**
The project allows a user to work with a database containing animals from all of the surrounding Austin area’s animal shelters using a GUI. The middleware provides CRUD functionality in python that allows the front end to query data. When all of this comes together, you get a web interface that enables functionality for filtering, visualization using a table, a map of the animal’s location, and a pie chart break down. 

MongoDB was used as the database because its cheaper to scale the project with MogoDB. This can be done by sharding, which allowing the project to scale horizontally. As said from [mongodb.com](https://www.mongodb.com/developer/article/top-4-reasons-to-use-mongodb/#:~:text=%20The%20Top%204%20Reasons%20Why%20You%20Should,Sometimes%20the%20changes%20are%20simple%20and...%20More%20) “Sharding is a method for distributing data across multiple servers. When your database exceeds the capacity of its current server, you can begin sharding and split it over two servers.”  It is easier and faster to optimize the database with the use of indexing. 

We are using the Dash framework to help us build our dashboard because of the out-of-the-box tools that come with it. Dash provides good looking, easy to implement, and easy to customize GUI tools like a dropdown menu, graphs, tables, etc. 

## **Challenges**
Some of the challenges that were faced were overcoming the learning curve for the Dash framework. It is a well thought out framework that works well, just takes some getting used to. 

Other challenges were integrating the queries and how to format them for our python CRUD module in AnimalShelterClient.py. This took a little bit of practical debugging practice and applying some logical analysis on how inputs need to enter the dictionary parameter for the readAll function found in the module. Specifically it was integrating the MongoDB operators like ‘$in’ or ‘$gte’. These must be formatted as a string so it can be passed and read by the pymongo api. 

## **Motivation**
This project exists to help the Grazioso Salvare company to track down and find potential candidates for the different types of rescue dogs that they train. Instead of the company to hand comb the entire data set, the application allows for them to custom query dogs that meet their specification. 

## **Getting Started**
To get this project working you will need a few things:

- Jupyter Notebook to run and edit the code in
- Python3
- The AnimalShelterClient.py for the middleware
- The AustinAnimalShelterFrontEnd.ipynb file for the web application
- A logo as a png
- Dash framework
- Plotly module
- Dash leaflet module
- MongoDB 
- A terminal to work in
- MongoDB user with valid credentials  

## **Installation**
1. Download MongoDB
1. Download python
1. Download the source files
1. Pip install the following:
   1. Dash framework
   1. Plotly module
   1. Dash Leaflet module needs to be installed
   1. Pip install pandas
   1. Pip install pymongo module
   1. Pip install numpy
   1. Pip install any other modules that may be needed for your code
1. Download Juptyer Notebook


## **Usage**
When you have everything installed, start by importing your data set by running this command

TO IMPORT A CSV FILE :

`General format: mongoimport --port=37231 --db=AAC --collection=animals --type=csv --headerline --file=aac\_shelter\_outcomes.csv`

Now start your MongoDB server with this command: 

`/usr/local/bin/mongod\_ctl start-noauth`  This is if you don’t already have a user account

`/usr/local/bin/mongod\_ctl start` If you do have a user account already

See these resources for creating an account

[Use SCRAM to Authenticate Clients — MongoDB Manual](https://docs.mongodb.com/manual/tutorial/configure-scram-client-authentication/#std-label-create-user-admin)

<https://docs.mongodb.com/manual/tutorial/create-users/#std-label-create-users>

From there you can start and run your web application.

When you run the code you will be able to see the main start up page with no filters applied. 

![image](https://user-images.githubusercontent.com/22525956/155253251-1d5c5702-a860-4576-8051-5deabe8213d6.png)

![image](https://user-images.githubusercontent.com/22525956/155253278-47279878-eca1-4de6-88be-2570128493a7.png)

Now you may notice some sorting functionality built into the table. Feel free to play around with it. It may serve you some good when trying to narrow down your candidate options. 

Now at the top. Notice the long dropdown menu above the table. It is set to reset by default. Go ahead and set it to something else by clicking it and selecting an option. You should see your screen update in the table, pie chart, and map when you do this as demonstrated here. Also hover your mouse over the map where the pin point is and click on the pin. You should see relevant details show up.

![image](https://user-images.githubusercontent.com/22525956/155253315-1897e933-1b06-404b-912e-8f6ce3f81397.png)


You can also hover over the pie graph as well to display data.

![image](https://user-images.githubusercontent.com/22525956/155253325-e3136316-b928-4448-88ec-0daf08e58615.png)

Here are the other options:

![image](https://user-images.githubusercontent.com/22525956/155253359-6d8e5fe1-c01d-4b76-9db6-ba757f45ae68.png)

![image](https://user-images.githubusercontent.com/22525956/155253367-b51a8fd9-201d-4215-a675-8af82bd4f726.png)




## **Roadmap/Features (Optional)**
In the future, we need to make the map more dynamic to user input by allowing the user to select a row and having the map update depending on what row is selected.

## **Resources**
Dash. (n.d.). Retrieved February 18, 2022, from https://dash-leaflet.herokuapp.com/ 

For map functionality

*Introduction: Dash for python documentation*. Plotly. (n.d.). Retrieved February 18, 2022, from https://dash.plotly.com/introduction 

*MongoDB Atlas: Cloud Document Database*. MongoDB. (n.d.). Retrieved February 18, 2022, from https://www.mongodb.com/cloud/atlas/lp/try2?utm\_source=bing&utm\_campaign=mdb\_bs\_americas\_united\_states\_search\_core\_brand\_atlas\_desktop&utm\_term=mongodb&utm\_medium=cpc\_paid\_search&utm\_ad=e&utm\_ad\_campaign\_id=415204521&adgroup=1208363748749201&msclkid=a2603ff46b141fe70b2c5dfb61a66fab 

Schaefer, L. (2022, February 12). *The top 4 reasons why you should use mongodb*. MongoDB. Retrieved February 18, 2022, from https://www.mongodb.com/developer/article/top-4-reasons-to-use-mongodb/#:~:text=%20The%20Top%204%20Reasons%20Why%20You%20Should,Sometimes%20the%20changes%20are%20simple%20and...%20More%20 

*Welcome to Python.org*. Python.org. (n.d.). Retrieved February 18, 2022, from https://www.python.org/ 


## **Contact**
Brandon Thibeaux

Last updated: 2/17/2022


