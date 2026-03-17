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
    email = data.get('email', '').strip()
    message = data.get('message', '').strip()

    if not name or not email or not message:
        return jsonify({'success': False, 'error': 'Name, email, and message are required.'}), 400

    org = data.get('organization', '').strip()
    phone = data.get('phone', '').strip()
    subject = data.get('subject', '').strip()

    print(f"[ENQUIRY] {name} | {org} | {email} | {phone} | {subject}")
    print(f"[MESSAGE] {message}")

    return jsonify({
        'success': True,
        'message': 'Thank you for your enquiry. Our team will get back to you within 24 hours.'
    })


@app.route('/api/ai-hero', methods=['GET'])
def ai_hero():
    """Use Gemini to generate dynamic hero content — rotating facts and insights."""
    api_key = os.environ.get('GEMINI_API_KEY', '')
    if not api_key:
        return jsonify({
            'success': True,
            'insight': 'Protecting India\'s 5,334 large dams with intelligent, real-time monitoring.',
            'fact': 'Less than 15% of India\'s dams have adequate safety instrumentation.'
        })

    try:
        import google.generativeai as genai
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-2.0-flash')

        prompt = """Generate a single JSON object with exactly two fields for a dam safety technology company's website hero section:

1. "insight" — A powerful, poetic one-liner (under 15 words) about dam safety, water infrastructure, or protecting lives through technology. Make it evocative and different each time. Examples of tone: "Where sensors meet safety", "Every drop monitored, every life protected", "The silent guardians of a billion lives".

2. "fact" — A compelling real statistic or fact about dam safety in India (under 25 words). Use real data: India has 5,334 large dams, Dam Safety Act 2021, 1,137 dams over 50 years old, <15% have monitoring, 35-45% canal water loss, etc.

Return ONLY the JSON object, no markdown, no code blocks."""

        response = model.generate_content(
            prompt,
            generation_config={
                'max_output_tokens': 200,
                'temperature': 1.0,
            }
        )

        import json
        text = response.text.strip()
        if text.startswith('```'):
            text = text.split('\n', 1)[1].rsplit('```', 1)[0].strip()

        data = json.loads(text)
        return jsonify({
            'success': True,
            'insight': data.get('insight', 'Intelligent monitoring for India\'s critical infrastructure.'),
            'fact': data.get('fact', 'Over 5,334 large dams in India need continuous safety monitoring.')
        })

    except Exception as e:
        print(f"[AI-HERO ERROR] {e}")
        return jsonify({
            'success': True,
            'insight': 'Where technology meets water safety.',
            'fact': 'India\'s Dam Safety Act 2021 mandates real-time monitoring for all large dams.'
        })


if __name__ == '__main__':
    app.run(debug=True, port=5000)
