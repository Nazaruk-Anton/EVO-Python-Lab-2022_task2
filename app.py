from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    server_message = ''
    client_message = ''

    if request.method == 'POST':
        client_message = request.form.get('message')

    if client_message.lower() != '':
        with open('name_list.txt', 'r+') as file:
            if client_message not in file.read():
                server_message = request.form.get('message') + ' ' + 'Hello'
                file.write(f'{client_message}\n')
            else:
                server_message = f'Имя {client_message} уже есть'

    return render_template(
        'index.html',
        message=server_message,
    )

@app.route('/allclients', methods=['GET'])
def allclients():
    with open('name_list.txt', 'r') as file:
        clients = file.read()
    return clients
if __name__ == '__main__':
    app.run()