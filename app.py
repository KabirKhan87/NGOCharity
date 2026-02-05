from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/causes')
def causes():
    return render_template('causes.html')

@app.route('/causes/<int:cause_id>')
def causes_detail(cause_id):
    # You can create a causes_detail.html template for individual cause pages
    # For now, redirect to main causes page
    return redirect(url_for('causes'))

@app.route('/service')
def service():
    return render_template('service.html')

@app.route('/donate')
def donate():
    return render_template('donate.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/testimonial')
def testimonial():
    return render_template('testimonial.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/contact/submit', methods=['POST'])
def contact_submit():
    # Handle contact form submission
    name = request.form.get('name')
    email = request.form.get('email')
    subject = request.form.get('subject')
    message = request.form.get('message')
    
    # Process the contact form (you can add database logic here)
    print(f"Contact form submitted: {name}, {email}, {subject}")
    
    # Redirect back to contact page or show success message
    return redirect(url_for('contact'))

@app.route('/404')
def not_found():
    return render_template('404.html')

@app.route('/process_donation', methods=['POST'])
def process_donation():
    # Handle donation processing
    name = request.form.get('name')
    email = request.form.get('email')
    amount = request.form.get('amount')
    cause = request.form.get('cause')
    
    # Process the donation (you can add payment processing logic here)
    print(f"Donation received: {name}, {email}, ${amount}, {cause}")
    
    # Redirect to thank you page or show success message
    return redirect(url_for('donate'))

@app.route('/subscribe', methods=['POST'])
def subscribe():
    # Handle newsletter subscription
    email = request.form.get('email')
    
    # Process the subscription (you can add database logic here)
    print(f"Newsletter subscription: {email}")
    
    # Return success response
    return "Subscribed successfully"

# Add error handler for 404 pages
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run()