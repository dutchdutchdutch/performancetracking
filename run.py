from tracker import app
import os

app.secret_key = os.urandom(24)
# app.run(debug=True) dev only
port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port= port)
