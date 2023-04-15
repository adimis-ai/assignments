from flask import Flask, request, jsonify
from pydantic import BaseModel, ValidationError
from typing import Optional

app = Flask(__name__)

# Define a Pydantic model for input validation
class InputPayload(BaseModel):
    input_string: str
    optional_comment: Optional[str] = None

@app.route('/reverse_string', methods=['POST'])
def reverse_string():
    try:
        # Validate the request JSON payload using the Pydantic model
        data = InputPayload.parse_raw(request.data)
    except ValidationError as e:
        return jsonify({'error': 'Invalid JSON payload', 'details': e.json()}), 400

    input_string = data.input_string
    reversed_string = input_string[::-1]

    return jsonify({'reversed_string': reversed_string}), 200

if __name__ == '__main__':
    app.run(debug=True)
