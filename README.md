# Splitwise-Expense-sharing-app-using-Python-flask-

The Expense-Sharing Application is a Python-based backend for an expense-sharing system. This application allows users to add expenses, split them among different participants, and keep track of balances between users.

## Design Overview
The Expense-Sharing Application allows users to track expenses and split them among different participants. It supports three types of expenses: EQUAL, EXACT, and PERCENT. Users can add expenses, view balances, and receive notifications about their share of expenses.

## Model-View-Controller (MVC) pattern.

![Diagram](https://files.realpython.com/media/mvc_diagram_with_routes.e12c5b982ac8.png)

Architecture Diagram

## 1. Model
In this example, the User and ExpenseManager classes represent the model components.

* **User Class:** Represents individual users of the application. It contains attributes such as `user_id`, `name`, `email`, `mobile`, and `balance`. Users can update their balances and receive expense notifications.

* **ExpenseManager Class:** Manages users and expenses. It allows adding users, recording expenses, retrieving user information, and getting user balances.

## 2. View
In this code example, there isn't a separate view component as we're building a backend API. The API contracts specified in the README.md file act as a form of interface that frontend or client applications can use to interact with the system.

## 3. Controller
The controller is represented by the Flask application. It handles incoming HTTP requests, processes the data, and interacts with the model to perform necessary operations.

* **Add Expense Route:** This route (`/add_expense`) handles POST requests for adding expenses. It extracts the necessary information from the request, records the expense using the ExpenseManager, and sends notifications to participants.

* **Get User Balance Route:** This route (`/get_user_balance/<user_id>`) handles GET requests for retrieving user balances. It uses the ExpenseManager to fetch the user's balance.



## Features

- **Add User:**
  - Endpoint: `/add_user`
  - Method: POST
  - Request Body:
    ```json
    {
      "user_id": "string",
      "name": "string",
      "email": "string",
      "mobile": "string"
    }
    ```
  - Response:
    ```json
    {
      "message": "string"
    }
    ```

- **Add Expense:**
  - Endpoint: `/add_expense`
  - Method: POST
  - Request Body:
    ```json
    {
      "payer_id": "string",
      "amount": 1250.0,
      "participants": ["string"],
      "split_type": "string" (EQUALLY, PERCENTAGE, SHARE),
      "expense_name": "string",
      "notes": "string",
      "images": ["string"]
    }
    ```
  - Response:
    ```json
    {
      "message": "string"
    }
    ```

- **Get User Balance:**
  - Endpoint: `/get_user_balance/<user_id>`
  - Method: GET
  - Response:
    ```json
    {
      "balance": 560.0
    }
    ```

- **Get Passbook:**
  - Endpoint: `/get_passbook/<user_id>`
  - Method: GET
  - Response:
    ```json
    {
      "passbook": [
        {
          "expense_id": 1,
          "expense_name": "string",
          "payer_id": "string",
          "amount": 1250.0,
          "participants": ["string"],
          "split_type": "string" (EQUALLY, PERCENTAGE, SHARE),
          "notes": "string",
          "images": ["string"]
        },
        // Additional entries...
      ]
    }
    ```

## Implementation Details

- **Classes:**
  - `User`: Represents individual users with attributes such as `user_id`, `name`, `email`, `mobile`, and `balance`.
  - `Expense`: Represents individual expenses with additional details like `expense_name`, `notes`, and `images`.
  - `ExpenseManager`: Manages users and expenses, providing methods for adding users, recording expenses, and retrieving balances.

- **API Endpoints:**
  - `/add_user`: Add a new user to the system.
  - `/add_expense`: Record an expense with options for splitting and additional details.
  - `/get_user_balance/<user_id>`: Get the balance for a specific user.
  - `/get_passbook/<user_id>`: Get a detailed passbook of all transactions involving a user.

- **Email Notifications:**
  - Users receive email notifications asynchronously when added to an expense.
  - Weekly email summaries are sent to users, detailing the total amount owed.

## Setup and Usage

1. Install required dependencies: Flask, Flask-Mail.
2. Configure Flask-Mail with your email credentials.
3. Run the application using `python app.py`.


## Database Schema

The application uses a relational database with tables for `users` and `expenses`. See the [Database Schema](#database-schema) section for details.

