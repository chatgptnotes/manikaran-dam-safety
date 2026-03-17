from flask import Flask, render_template, request, jsonify
import os

app = Flask(
    __name__,
    template_folder=os.path.join(os.path.dirname(__file__), '..', 'templates'),
    static_folder=os.path.join(os.path.dirname(__file__), '..', 'public'),
    static_url_path=''
)

app.secret_key = os.environ.get('SECRET_KEY', 'dev-key-change-in-prod')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/solutions')
def solutions():
    return render_template('solutions.html')


@app.route('/technology')
def technology():
    return render_template('technology.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/api/enquiry', methods=['POST'])
def enquiry():
    data = request.get_json() if request.is_json else request.form.to_dict()
    name = data.get('name', '').strip()
    org = data.get('organization', '').strip()
    email = data.get('email', '').strip()
    phone = data.get('phone', '').strip()
    subject = data.get('subject', '').strip()
    message = data.get('message', '').strip()

    if not name or not email or not message:
        return jsonify({'success': False, 'error': 'Name, email, and message are required.'}), 400

    # In production: send email, store in DB, or forward to CRM
    print(f"[ENQUIRY] {name} | {org} | {email} | {phone} | {subject}")
    print(f"[MESSAGE] {message}")

    return jsonify({
        'success': True,
        'message': 'Thank you for your enquiry. Our team will get back to you within 24 hours.'
    })


if __name__ == '__main__':
    app.run(debug=True, port=5000)
