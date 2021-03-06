"""Application entry point."""
from twitterAnalytics import create_app

app = create_app()
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)