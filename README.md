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
