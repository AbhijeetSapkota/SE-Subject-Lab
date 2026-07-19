from flask import Flask, render_template, request, redirect, url_for, session, flash
from retailer import Retailer
from consumer import Consumer
from product import Product
from tab import Tab
from tabEntry import TabEntry
from review import Review
from query import Query

app = Flask(__name__)
app.secret_key = 'super_secret_key'

# In-memory "Database"
db = {
    'users': {}, # username -> User object
    'retailers': [],
    'consumers': []
}

# Add some dummy data
r1 = Retailer('retailer1', 'password123', 'John Shopkeeper', '1234567890', 'Johns Mart', 'Downtown')
r1.inventory.addItem(Product('Sugar', 2.50, 'SweetBrand', '1kg Sugar packet'))
r1.inventory.addItem(Product('Salt', 1.00, 'SaltyBrand', '1kg Salt packet'))
db['users']['retailer1'] = r1
db['retailers'].append(r1)

c1 = Consumer('consumer1', 'password123', 'Alice Shopper', '0987654321', 'Downtown')
db['users']['consumer1'] = c1
db['consumers'].append(c1)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = db['users'].get(username)
        if user and user.login(password):
            session['username'] = username
            session['user_type'] = 'retailer' if isinstance(user, Retailer) else 'consumer'
            flash('Logged in successfully!', 'success')
            if session['user_type'] == 'retailer':
                return redirect(url_for('retailer_dashboard'))
            else:
                return redirect(url_for('consumer_dashboard'))
        else:
            flash('Invalid credentials', 'error')
            
    return render_template('auth.html', action='Login')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user_type = request.form['user_type']
        username = request.form['username']
        password = request.form['password']
        personal_info = request.form['personal_info']
        contact_info = request.form['contact_info']
        
        if username in db['users']:
            flash('Username already exists', 'error')
            return redirect(url_for('register'))
            
        if user_type == 'retailer':
            shop_name = request.form.get('shop_name', '')
            shop_location = request.form.get('shop_location', '')
            user = Retailer(username, password, personal_info, contact_info, shop_name, shop_location)
            db['retailers'].append(user)
        else:
            gps_location = request.form.get('gps_location', '')
            user = Consumer(username, password, personal_info, contact_info, gps_location)
            db['consumers'].append(user)
            
        db['users'][username] = user
        flash('Registration successful. Please login.', 'success')
        return redirect(url_for('login'))
        
    return render_template('auth.html', action='Register')

@app.route('/logout')
def logout():
    session.clear()
    flash('Logged out.', 'info')
    return redirect(url_for('index'))

@app.route('/retailer_dashboard', methods=['GET', 'POST'])
def retailer_dashboard():
    if session.get('user_type') != 'retailer':
        return redirect(url_for('login'))
    retailer = db['users'][session['username']]
    
    if request.method == 'POST':
        name = request.form['name']
        price = float(request.form['price'])
        brand = request.form['brand']
        description = request.form['description']
        retailer.inventory.addItem(Product(name, price, brand, description))
        flash('Product added successfully', 'success')
        
    return render_template('retailer_dashboard.html', retailer=retailer)

@app.route('/consumer_dashboard')
def consumer_dashboard():
    if session.get('user_type') != 'consumer':
        return redirect(url_for('login'))
    consumer = db['users'][session['username']]
    
    query = request.args.get('q', '')
    results = []
    if query:
        results = consumer.searchItems(query, db['retailers'])
        
    return render_template('consumer_dashboard.html', consumer=consumer, query=query, results=results)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
