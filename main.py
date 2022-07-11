#  Production server
from website import create_app
from waitress import serve

app = create_app()

if __name__ == "__main__":
    serve(app, port=8080)


"""
# Development server
from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(port=8080, debug=True)
"""
