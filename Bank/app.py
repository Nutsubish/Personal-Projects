from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'nikoloznutsubidze'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)
    balance = db.Column(db.Float, default=0.0)
    sent_requests = db.relationship('FriendRequest', foreign_keys='FriendRequest.sender_id', backref='sender', lazy=True)
    received_requests = db.relationship('FriendRequest', foreign_keys='FriendRequest.receiver_id', backref='receiver', lazy=True)
    friendships = db.relationship('Friendship', primaryjoin="or_(User.id==Friendship.user_id, User.id==Friendship.friend_id)", lazy=True)

class FriendRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    receiver_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    status = db.Column(db.String(50), default='pending')  # 'accepted', 'rejected'

class Friendship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    friend_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    
    user = db.relationship('User', foreign_keys=[user_id], backref=db.backref('user_friendships', lazy='dynamic'))
    friend = db.relationship('User', foreign_keys=[friend_id], backref=db.backref('friend_friendships', lazy='dynamic'))

# Flask Routes
@app.route('/')
def index():
    if 'username' in session:
        user = User.query.filter_by(username=session['username']).first()
        if user:
            transactions = get_transactions(user.id)
            pending_requests = FriendRequest.query.filter_by(receiver_id=user.id, status='pending').all()
            return render_template('index.html', user=user, transactions=transactions, pending_requests=pending_requests)
        else:
            flash('User not found. Please log in again.', 'danger')
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['username'] = user.username
            return redirect(url_for('index'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if len(password) < 3:
            flash('Password must be at least 3 characters long', 'danger')
            return redirect(url_for('register'))
        
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user) # to add user in session
        db.session.commit()
        flash('Registration successful. Please log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/deposit', methods=['GET', 'POST'])
def deposit():
    if 'username' in session:
        if request.method == 'POST':
            amount = float(request.form['amount'])
            user = User.query.filter_by(username=session['username']).first()
            user.balance += amount
            db.session.commit()
            flash('Deposit Successful', 'success')
            return redirect(url_for('index'))
        return render_template('deposit.html')
    return redirect(url_for('login'))

@app.route('/withdraw', methods=['GET', 'POST'])
def withdraw():
    if 'username' in session:
        if request.method == 'POST':
            amount = float(request.form['amount'])
            user = User.query.filter_by(username=session['username']).first()
            if user.balance >= amount:
                user.balance -= amount
                db.session.commit()
                flash('Withdrawal Successful', 'success')
            else:
                flash('Insufficient Funds', 'danger')
            return redirect(url_for('index'))
        return render_template('withdraw.html')
    return redirect(url_for('login'))

@app.route('/send_friend_request', methods=['POST'])
def send_friend_request():
    if 'username' in session:
        receiver_username = request.form['username']
        receiver = User.query.filter_by(username=receiver_username).first()
        if receiver:
            sender = User.query.filter_by(username=session['username']).first()
            if not FriendRequest.query.filter_by(sender_id=sender.id, receiver_id=receiver.id).first():
                new_request = FriendRequest(sender_id=sender.id, receiver_id=receiver.id)
                db.session.add(new_request)
                db.session.commit()
                flash('Friend request sent', 'success')
            else:
                flash('Friend request already sent', 'danger')
        else:
            flash('No user with that username found', 'danger')
        return redirect(url_for('index'))
    return redirect(url_for('login'))

@app.route('/accept_friend_request/<int:request_id>', methods=['GET'])
def accept_friend_request(request_id):
    if 'username' in session:
        friend_request = FriendRequest.query.get(request_id)
        if friend_request and friend_request.status == 'pending':
            friend_request.status = 'accepted'
            new_friendship1 = Friendship(user_id=friend_request.sender_id, friend_id=friend_request.receiver_id)
            new_friendship2 = Friendship(user_id=friend_request.receiver_id, friend_id=friend_request.sender_id)
            db.session.add(new_friendship1)
            db.session.add(new_friendship2)
            db.session.commit()
            flash('Friend request accepted', 'success')
        return redirect(url_for('index'))
    return redirect(url_for('login'))

@app.route('/reject_friend_request/<int:request_id>', methods=['GET'])
def reject_friend_request(request_id):
    if 'username' in session:
        friend_request = FriendRequest.query.get(request_id)
        if friend_request and friend_request.status == 'pending':
            friend_request.status = 'rejected'
            db.session.commit()
            flash('Friend request rejected', 'success')
        return redirect(url_for('index'))
    return redirect(url_for('login'))

@app.route('/send_money', methods=['POST'])
def send_money():
    if 'username' in session:
        friend_username = request.form['username']
        amount = float(request.form['amount'])
        sender = User.query.filter_by(username=session['username']).first()
        receiver = User.query.filter_by(username=friend_username).first()
        if receiver:
            friendship = Friendship.query.filter_by(user_id=sender.id, friend_id=receiver.id).first()
            if friendship:
                if sender.balance >= amount:
                    sender.balance -= amount
                    receiver.balance += amount
                    db.session.commit()
                    flash('Money sent successfully', 'success')
                else:
                    flash('Insufficient funds', 'danger')
            else:
                flash('You are not friends with this user', 'danger')
        else:
            flash('No user with that username found', 'danger')
        return redirect(url_for('index'))
    return redirect(url_for('login'))

def get_transactions(user_id):
    transactions = []

    # Find all friendships where the user is either the sender or receiver
    sent_transactions = Friendship.query.filter_by(user_id=user_id).all()
    received_transactions = Friendship.query.filter_by(friend_id=user_id).all()

    
    for friendship in sent_transactions:
        friend = User.query.get(friendship.friend_id)
        if friend:
            transactions.append({
                'type': 'Sent money',
                'amount': 'N/A',  # Adjust based on actual data structure
                'timestamp': friendship.timestamp,
                'friend_username': friend.username,
            })

    # Iterate over received transactions
    for friendship in received_transactions:
        friend = User.query.get(friendship.user_id)
        if friend:
            transactions.append({
                'type': 'Received money',
                'amount': 'N/A',  # Adjust based on actual data structure
                'timestamp': friendship.timestamp,
                'friend_username': friend.username,
            })

    transactions.sort(key=lambda x: x['timestamp'], reverse=True)
    return transactions

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)




