from flask import Flask, jsonify
from sqlalchemy import create_engine, text
from sqlalchemy.engine.url import URL

app = Flask(__name__)

url = URL.create(
    drivername="cockroachdb+psycopg2",
    username="bilal",
    password="EZxkc0CLbQOwinppgIjPqg",
    host="odyesseydb-5950.7s5.aws-ap-south-1.cockroachlabs.cloud",
    port=26257,
    database="trackingTest",
    query={"sslmode": "require", "options": "--cluster=odyesseydb-5950"}
)

engine = create_engine(
    url,
    connect_args={"application_name": "status-tracker"},
    execution_options={"isolation_level": "AUTOCOMMIT"},
)

@app.route("/")
def home():
    return "✅ Status Emailing API is Live!"

@app.route("/tracking/<id>")
def order_tracking(id):
    with engine.connect() as conn:
        query = text('SELECT * FROM tracking WHERE "jobId" = :jobId')
        result = conn.execute(query, {"jobId": id}).fetchone()

    if not result:
        return jsonify({"error": f"No tracking found for Order ID {id}"}), 404

    tracking_data = {
        "order_id": result["jobNo"],
        "client": result["client"],
        "status": result["status"],
    }

    return jsonify(tracking_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
