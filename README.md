### 🧁 Sweet Server

Sweet Server is a REST API server designed for managing a confectionery business. It includes the necessary modules to handle all relevant information, such as stock, recipes, products, monthly fees, collaborators, customers, and sales.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

### 🛠️ Installation and Configuration

To begin the server installation, ensure that **Python 3.12** is installed on your system. You will also need the source code, which can be cloned using the following command:

```bash
git clone https://github.com/davidsantana06/sweet-server
```

Once you have the files, create a `.env` file based on the template provided in `.env.example`. In this file, specify the following fields:

- `SECRET_KEY` - Server secret key, which should be long and contain multiple characters;
- `ALLOWED_HOSTS` - A list of addresses (or domains) allowed to make requests to the server, separated by space.

Next, install the application dependencies using the command:

```bash
pip install -r requirements.txt
```

Finally, start the server with:

```bash
flask --app app run
```

This process can be performed within a virtual environment.

#### 🗃️ Essential Data Creation

The essential data can be found in `storage\setup\`. This file contains the following keys:

- `default_categories.json` - A list containing the names of recipe categories;
- `default_collaborator.json` - An object with the default collaborator data, without remuneration.
- `default_payment_methods.json` - A list containing the names of accepted payment methods;
- `user.json` - An object containing the the user's name.

The keys have their default values and can be customized as needed, as long as the format is respected.

### 📚 Docs

The documentation is generated in the Swagger format using Flask-RESTx and is available at the base URL (`/`). For local testing, access `http://localhost:5000/`.

### ⚖️ License

This project adopts the **MIT License**, which allows you to use and make modifications to the code as you wish. The only thing I ask is that proper credit is given, acknowledging the effort and time I invested in building it.
