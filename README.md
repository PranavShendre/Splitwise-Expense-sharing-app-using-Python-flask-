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
      "user_id": "u1",
      "name": "User1",
      "email": "user1@gmail.com",
      "mobile": "6543298723"
    }
    ```
  - Response:
    ```json
    {
      "message": "User Added Successfully!"
    }
    ```

- **Add Expense:**
  - Endpoint: `/add_expense`
  - Method: POST
  - Request Body:
    ```json
    {
      "payer_id": "u1",
      "amount": 1250.0,
      "participants": ["u1","u2","u3"],
      "split_type": "string" (EQUALLY, PERCENTAGE, SHARE),
      "expense_name": "Electicity Bill",
      "notes": "string",
      "images": ["string"]
    }
    ```
  - Response:
    ```json
    {
      "message": "Expense recorded successfully!"
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
          "expense_name": "Electricity Bill",
          "payer_id": "u1",
          "amount": 1250.0,
          "participants": ["u1","u2","u3"],
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

The application uses a relational database with tables for `users` and `expenses`.
# Database Schema

The Expense-Sharing Application uses a relational database with two main tables: `users` and `expenses`.

## `users` Table

| Field     | Type         | Description                       |
|-----------|--------------|-----------------------------------|
| user_id   | VARCHAR(50)  | Unique identifier for the user.    |
| name      | VARCHAR(100) | Name of the user.                  |
| email     | VARCHAR(255) | Email address of the user.         |
| mobile    | VARCHAR(20)  | Mobile number of the user.         |
| balance   | DECIMAL(10,2)| Current balance of the user.       |

## `expenses` Table

| Field           | Type         | Description                                      |
|-----------------|--------------|--------------------------------------------------|
| expense_id      | INT          | Unique identifier for the expense.               |
| payer_id        | VARCHAR(50)  | User ID of the person who paid for the expense.  |
| amount          | DECIMAL(10,2)| Total amount of the expense.                     |
| split_type      | VARCHAR(20)  | Type of expense splitting (EQUALLY, PERCENTAGE, SHARE).|
| expense_name    | VARCHAR(255) | Name or description of the expense.              |
| notes           | TEXT         | Additional notes related to the expense.        |
| images          | JSON         | JSON array of image URLs or file paths associated with the expense. |
| created_at      | TIMESTAMP    | Timestamp indicating when the expense was recorded. |










