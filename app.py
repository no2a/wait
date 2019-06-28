import time

from flask import Flask, request, Response


app = Flask(__name__)
app.debug = True


def countdown(count):
    while count > 0:
        yield '%d\n' % count
        count -= 1
        time.sleep(1)
    yield '%d\n' % count


@app.route('/')
def hello_world():
    wait = int(request.args.get('wait', '0'))
    return Response(countdown(wait))


if __name__ == '__main__':
    app.run(host='0.0.0.0')
