
## SplitWise Expense Sharing Application Backend in Python with flask framework

from flask import Flask, request, jsonify
from flask_mail import Mail, Message

app = Flask(__name__)

# app.Config['MAIL_SERVER'] = 'smtp.gmail.com'
# app.Config['MAIL_PORT'] = 465
# app.Config['MAIL_USERNAME'] = 'splitwise@gmail.com'
# app.Config['MAIL_PASSWORD'] =  'splitwise'
# app.Config['MAIL_USE_TLS'] = False
# app.Config['MAIL_USE_SSL'] = True

mail = Mail(app)

# Model
class User:
    def __init__(self, user_id, name, email,mobile):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.mobile = mobile
        self.balance = 0
        
    def update_balance(self, ammount):
        self.balance += ammount

    def get_balance(self):
        return round(self.balance, 2)
    
    # def send_expense_notification(self, total_amout):
    #     msg = Message('Expense Notification', sender='splitwise@gmail.com',recipients= [self.email])
    #     msg.body = f'You have been added to an expense. You owed {total_amout:.2f} INR.'
    #     mail.send(msg)


class Expense:
    def __init__(self, expense_id, payer_id, amount, participants, split_type, expense_name=None, notes=None, images=None):
        self.expense_id = expense_id
        self.payer_id = payer_id
        self.amount = amount
        self.participants = participants
        self.split_type = split_type
        self.expense_name = expense_name
        self.notes = notes
        self.images = images


class ExpenseManager:
    def __init__(self):
        self.users = {}

    def add_user(self, user_id, name, email, mobile):
        if user_id not in self.users:
            self.users[user_id] = User(user_id, name, email, mobile)

    def record_expense(self,payer_id, amount, participants, split_type, expense_name=None, notes=None, images=None):
        expense_id = len(self.expenses) + 1
        expense = Expense(expense_id, payer_id, amount, participants, split_type, expense_name, notes, images)
        self.expenses.append(expense)
        
        payer = self.users.get(payer_id)

        if not payer:
            raise ValueError(f'User {payer_id} does not exist.')
        
        total_participants = len(participants)

        if split_type == "EQUALLY":
            each_share = amount/total_participants

            for participant_id in participants:
                participant = self.users.get(participant_id)
                if participant:
                    participant.update_balance(-each_share)
                    payer.update_balance(each_share)
                else:
                    raise ValueError(f'User {participant_id} does not exists.')
        elif split_type == 'PERCENTAGE':
            total_percentage = sum(participants)

            for i,participant_id in enumerate(participants):
                percentage_share = amount * (participant_id / total_percentage)

                if i == payer_id:
                    payer.update_balance(-percentage_share)
                else:
                    participant = self.users.get(participant_id)
                    if participant:
                        participant.update_balance(percentage_share)
                    else:
                        raise ValueError(f"User {participant_id} does not exist.")
        elif split_type == "SHARE":
            for i, participant_id in enumerate(participants):
                share = participants[i]
                share_amount = amount * share / sum(participants)

                if i == payer_id:
                    payer.update_balance(-share_amount)
                else:
                    participant = self.users.get(participant_id)
                    if participant:
                        participant.update_balance(share_amount)
                    else:
                        raise ValueError(f"User {participant_id} does not exist.")
        else:
            raise ValueError("Invalid split type. Use 'EQUALLY', 'PERCENTAGE', or 'SHARE'.")



    def get_user(self,user_id):
        user = self.users.get(user_id)
        if user:
            return user
        else:
            raise ValueError(f'User {user_id} does not exists.')
        

    def get_user_balance(self,user_id):
        user = self.users.get(user_id)
        if user:
            return user.get_balance()
        else:
            raise ValueError(f'User {user_id} does not exists.')
        
    def get_passbook(self, user_id):
        passbook = []
        for expense in self.expenses:
            if user_id == expense.payer_id or user_id in expense.participants:
                passbook.append({
                    "expense_id": expense.expense_id,
                    "expense_name": expense.expense_name,
                    "payer_id": expense.payer_id,
                    "amount": expense.amount,
                    "participants": expense.participants,
                    "split_type": expense.split_type,
                    "notes": expense.notes,
                    "images": expense.images
                })
        return passbook




# Defining API routes or Http endpoints

expenseManager = ExpenseManager()

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.json

    user_id = data['user_id']
    name = data['name']
    email = data['email']
    mobile = data['mobile']

    expenseManager.add_user(user_id, name, email, mobile)

    return jsonify({'messsage':'User Added Successfully.'}),200

@app.route('/add_expense', methods=['POST'])
def add_expense():
    data = request.json

    payer_id = data['payer_id']
    amount = float(data['amount'])
    participants = data['participants']
    split_type = data['split_type']
    expense_name = data.get('expense_name')
    notes = data.get('notes')
    images = data.get('images')


    expenseManager.record_expense(payer_id,amount, participants, split_type,expense_name, notes, images)

    payer = expenseManager.get_user(payer_id)
    total_amount = round(amount/len(participants),2)

    for participant_id in participants:
        participant = expenseManager.get_user(participant_id)
        # participant.send_expense_notification((total_amount))

    return jsonify({'message':'Expense recorded successfully.'}),200

@app.route('/get_user_balance/<user_id>', methods=['GET'])
def get_user_balance(user_id):
    balance = expenseManager.get_user_balance(user_id)
    return jsonify({'balance': balance}),200

@app.route('/get_passbook/<user_id>', methods=['GET'])
def get_passbook(user_id):
    passbook = expenseManager.get_passbook(user_id)
    return jsonify({'passbook': passbook}), 200


if __name__ == '__main__':
    app.run(debug=True)








