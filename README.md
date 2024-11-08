### 🧁 Sweet Server

REST API server designed for managing a confectionery business. It includes the necessary modules to handle all relevant information, such as stock, recipes, products, monthly fees, collaborators, customers, and sales.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Swagger](https://img.shields.io/badge/-Swagger-%23Clojure?style=for-the-badge&logo=swagger&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

### 🗃️ Essential Data Setup

The essential data can be found in the `storage/setup/` directory. This folder contains the following files:

- `default_categories.json` — A list of recipe category names.
- `default_collaborator.json` — An object containing default collaborator data (without remuneration).
- `default_payment_methods.json` — A list of accepted payment method names.
- `user.json` — An object containing the user's name.

These files contain default values, which can be customized as needed, as long as the format is respected.

### 🛠️ Installation and Configuration

To begin the server installation, make sure **Python 3.12** is installed on your system. You will also need to clone the source code using the following command:

```bash
git clone https://github.com/davidsantana06/sweet-server
```

Once you have the files, create a `.env` file based on the template provided in `.env.example`. In this file, specify the following fields:

- `SECRET_KEY` — A secret key, which should be long and contain multiple characters.
- `ALLOWED_HOSTS` — A space-separated list of addresses (or domains) allowed to make requests to the server.

Next, install the application dependencies with the following command:

```bash
pip install -r requirements.txt
```

Finally, start the server with:

```bash
flask --app app run
```

### 📚 Documentation

The API documentation is available in **Swagger** format. You can access it at the base URL of the application. For local testing, navigate to `http://localhost:5000/` in your browser to view the available endpoints and their possible interactions.

### ⚖️ License

This project uses the **MIT License**, which allows you to use and modify the code as you wish. The only requirement is to give proper credit, acknowledging the effort and time spent in building it.
