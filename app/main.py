import os
import uuid
from datetime import datetime, timezone
from flask import Flask, jsonify, request
from werkzeug.exceptions import BadRequest

app = Flask(__name__)
appointments = {}  # Demonstration-only in-memory store; replace with a managed DB before production.

@app.get('/healthz')
def health():
    return jsonify(status='ok'), 200

@app.get('/readyz')
def ready():
    return jsonify(status='ready'), 200

@app.get('/appointments')
def list_appointments():
    return jsonify(appointments=list(appointments.values())), 200

@app.post('/appointments')
def create_appointment():
    payload = request.get_json(silent=True)
    if not isinstance(payload, dict):
        raise BadRequest('JSON object required')
    patient_ref = payload.get('patient_ref')
    starts_at = payload.get('starts_at')
    if not isinstance(patient_ref, str) or not patient_ref.strip() or not isinstance(starts_at, str):
        raise BadRequest('patient_ref and starts_at are required strings')
    try:
        timestamp = datetime.fromisoformat(starts_at.replace('Z', '+00:00'))
        if timestamp.tzinfo is None:
            raise ValueError('Timezone required')
    except ValueError:
        raise BadRequest('starts_at must be an ISO-8601 timestamp with timezone')
    record = {'id': str(uuid.uuid4()), 'patient_ref': patient_ref, 'starts_at': timestamp.astimezone(timezone.utc).isoformat()}
    appointments[record['id']] = record
    return jsonify(record), 201

@app.errorhandler(BadRequest)
def bad_request(err):
    return jsonify(error=str(err.description)), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', '8080')))
