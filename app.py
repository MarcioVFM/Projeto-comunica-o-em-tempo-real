from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/oayments/pix', methods=['POST'])
def create_payment_pix():
    return jsonify({'message':'The payment as been created'})

@app.route('/payments/pix/confirmation', methods=['POST'])
def pix_confirmation():
    return jsonify ({'message':'The payment as been confirmed'})

@app.route('/payments/pix/<int:payment_id>', methods=['GET'])
def payment_pix_page(payment_id):
    return 'payment pix'

if __name__ == '__main__':
    app.run(debug=True)