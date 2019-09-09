from apps import init_app

app = init_app("dev")

@app.route("/")
def index():
    return "hello world"

if __name__ == "__main__":
    app.manager.run()


