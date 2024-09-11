### 🧁 Sweet Server

Sweet Server is a REST API server designed for managing a confectionery business. It includes the necessary modules to handle all relevant information, such as stock, recipes, products, monthly fees, employees, customers, and sales.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)


#### 🛠️ Installation and Configuration

To begin the server installation, you need to have Python 3.9+ installed along with the source code, which can be cloned using the command **`git clone https://github.com/davidsantana06/sweet-server`**.

With the files in hand, create a `.env` file with the same fields present in `.env.example`. In this file, you should specify the following fields:

* HOST - IP address;
* PORT - Access port;
* SECRET_KEY - Server secret key should be long and contain multiple characters;
* DEBUG - Indicator to start the application in debug mode (`1`) or not (`0`).

Next, install the application dependencies using the command **`pip install -r requirements.txt`**. This process can be done in a virtual environment.

Finally, the server can be started with the command **`python run.py`**.


##### 🗃️ Essential Data Creation

The essential data can be found in `storage\setup.json`. This file contains the following keys:

* "category_names" - A list containing the names of recipe categories;
* "payment_method_names" - A list containing the names of accepted payment methods;
* "default_labor_data" - An object with the default employee data, without remuneration.

The keys have their default values and can be customized as needed, as long as the format is respected.


#### 📚 Documentation

Coming soon...