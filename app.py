from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def increment():
    num = 0
    try:
        if request.headers['Authorization'] != "MpvMbdp8OUdayWwqVTubx0x7B5Y77tXOUjd84YOkAS9wycGFTJzGbpDeHp9V1kAQ":
            raise Exception("")
    except:
        return "Not found", 400
    with open("counter.txt", "r") as f:
        file = f.read()
        if file == '':
            num = 0
        else:
            num = int(file) + 1
    with open("counter.txt", "w") as w:
        print(num)
        w.write(str(num))
    return str(num)
