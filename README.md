# flask-rest-api

Python Flask CRUD API using SQL Alchemy and Marshmallow

# List of API's

1. Get all Products ( GET Request )

       http://127.0.0.1:5000/products
       
2. Get Product by id ( GET Request )

       http://127.0.0.1:5000/product/<id>
       
3. Create a Product ( POST Request )

       http://127.0.0.1:5000/product/     
   
     POST Request Body  
       
       {
            "name" :"Name_Of_Product",
            "description" : "Description",
            "price" : 250000,
            "quantity" : 1
       }
       
4. Delete a Product ( Delete Request )

       http://127.0.0.1:5000/product/<id>

5. Update a Product ( PUT Request )

       http://127.0.0.1:5000/product/<id>  
    PUT Request Body  
       
       {
            "name" :"Updated_Name",
            "description" : "Updated_Description",
            "price" : 250000,
            "quantity" : 1
       }
       
To run this API       

* Clone this repository 

* Create a virtual environment

      pip install virtualenv
      virtualenv venv
      source venv/bin/activate 

* Install Requirements - 

      pip install -r requirements.txt

* Run application        

      python app.py


* Test your API using CURL or POSTMAN
