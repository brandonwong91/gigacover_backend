# gigacover_backend
To create a RESTful API with Python and postgres DB on a customer model and their birthdays

1.  Create Database Model in postgres  
    customers with data attributes of:    
    name  
    date of birth  
    updated_time  
  
2.  Build a RESTful API App:  
    With endpoints that allows CRUD actions  
    Postman collection : https://www.getpostman.com/collections/b894c678fdd8923d53a4  
    Additional task to query to get the names of the youngest customers  
      
3.  Deployment on a Cloud Hosting Service:  
    I have chosen Amazon EC2 for a linux machine to deploy the app  
    and also chosen Amazon RDB to start the postgres database too.
    Currently hosting at : http://18.222.127.78/

### Setting Up  
1.  pip install requirements.txt - this will include all the required dependancies  
2.  For local hosting, app.run() is used  
3.  For the cloud hosting, app.run(host="0.0.0.0",port:80) is required for the flask framework to connect with the host.  

### Note
1.  For Delete and Update actions, I decided to use the names of the customers as identifiers for the database, hence the names can be case sensitive, and to avoid user entering the wrong names, only the queried list of names are allowed.
2.  For the Youngest action, I initially thought it is to show the youngest customer by order, but since the task is to obtain the youngest customers, I will based on the youngest year of the database and everyone in that year. This is just my intepretation of the task.
3.  Accessing the cloud hosting database, I have to remove some security settings for the connection to pass through. I am unable to implement the JWT token as required, would like to study more on this section.
