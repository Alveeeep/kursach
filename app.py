from flask import Flask, flash, redirect, request, url_for, render_template
import models
from forms import edit_client

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Kursovaya'


@app.route('/')
def main_page():
    return render_template('index.html')


@app.route('/stuff')
def stuff_page():
    clients = models.get_clients()
    return render_template('stuff_main.html', clients=clients)

@app.route('/edit_client/<client_id>', methods=['GET', 'POST'])
def edit_client_page(client_id):
    info = models.get_client_info(client_id)
    form = edit_client.ClientEditForm()
    if form.validate_on_submit():
        models.edit_client_info(client_id, form.email.data, form.phone.data, form.firstname.data, form.lastname.data)
        return redirect('/stuff')
    print(form.errors)
    return render_template('edit_client.html', email=info[1], phone=info[2], firstname=info[3], lastname=info[4], form=form)


if __name__ == '__main__':
    app.run(debug=True)
