from flask import Flask, flash, redirect, request, url_for, render_template
import models
from forms import edit_client, product_info, product_in_store, store_search, edit_product, add_product, delete_product, \
    add_delivery

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
    return render_template('edit_client.html', email=info[1], phone=info[2], firstname=info[3], lastname=info[4],
                           form=form)


@app.route('/client_info/<client_id>', methods=['GET', 'POST'])
def client_info_page(client_id):
    info = models.get_client_info(client_id)
    return render_template('client_info.html', info=info)


@app.route('/info_and_edit_cliet/<client_id>', methods=['GET', 'POST'])
def client_edit_and_info(client_id):
    info = models.get_client_info(client_id)
    return render_template('info_and_edit_client.html', info=info)


@app.route('/product_info')
def product_info_search_page():
    form = product_info.ProductInfotForm()
    if form.validate_on_submit():
        return redirect(f'/product_info/{form.product_id.data}')
    return render_template('product_search.html', form=form)


@app.route('/product_info/<product_id>', methods=['GET', 'POST'])
def product_info_page(product_id):
    info = models.get_product_info(product_id)
    manufacture_name = models.get_manufacture_name_by_id(info[2])
    category_name = models.get_category_name_by_id(info[3])
    return render_template('product_info.html', info=info, manufacture_name=manufacture_name[0],
                           category_name=category_name[0])


@app.route('/product_info_in_store')
def product_store_search():
    form = product_in_store.ProductInStoreForm()
    if form.validate_on_submit():
        return redirect(f'/product_info_in_store/{form.product_id}/{form.store_id}')
    return render_template('product_in_store_search.html', form=form)


@app.route('/product_info_in_store/<product_id>/<store_id>', methods=['GET', 'POST'])
def product_in_store_page(product_id, store_id):
    product_count = models.get_product_count_in_store(product_id, store_id)
    return render_template('product_in_store.html', product_id=product_id, store_id=store_id, count=product_count)


@app.route('/products_in_store')
def product_in_store_search():
    form = store_search.StoreSearchForm()
    if form.validate_on_submit():
        return redirect(f'/products_in_store/{form.store_id.data}')
    return render_template('store_search.html', form=form)


@app.route('/products_in_store/<store_id>', methods=['GET', 'POST'])
def products_in_store(store_id):
    products = models.get_products_in_store(store_id)
    res = []
    for el in products:
        manuf = models.get_manufacture_name_by_id(el[2])[0]
        categ = models.get_category_name_by_id(el[3])[0]
        res.append({
            'id': el[0],
            'name': el[1],
            'manufacture': manuf,
            'category': categ,
            'price': el[4]
        })
    return render_template('products_in_store.html', products=res)


@app.route('/admin')
def admin_page():
    clients = models.get_clients()
    products = models.get_products()
    return render_template('admin_main.html', clients=clients, products=products)


@app.route('/edit_product/<product_id>', methods=['GET', 'POST'])
def edit_product(product_id):
    info = models.get_product_info(product_id)
    form = edit_product.ProductEditForm()
    if form.validate_on_submit():
        models.edit_product_info(form.name.data, form.manufacture_id.data, form.category_id.data, form.price.data)
        redirect(f'/product_info/{product_id}')
    return render_template('edit_product.html', info=info, form=form)


@app.route('/add_product')
def add_product():
    form = add_product.AddProductForm()
    if form.validate_on_submit():
        models.add_product(form.name.data, form.manufacture_id.data, form.category_id.data, form.price.data)
        redirect('/admin')
    return render_template('add_product.html', form=form)


@app.route('/delete_product')
def delete_product():
    form = delete_product.DeleteProductForm()
    if form.validate_on_submit():
        models.delete_product(form.product_id.data)
        redirect('/admin')
    return render_template('delete_product.html', form=form)


@app.route('/deliveries')
def deliveries():
    form = store_search.StoreSearchForm()
    form1 = add_delivery.AddDeliveryForm()
    if form.validate_on_submit():
        res = []
        info = models.get_deliveries_by_store(form.store_id.data)
        for el in info:
            res.append({
                'product_id': el[0],
                'store_id': el[1],
                'delivery_date': el[2],
                'count': el[3]
            })
        return render_template('deliveries.html', form=form, form1=form, res=res)
    if form1.validate_on_submit():
        models.add_delivery(form1.product_id.data, form1.store_id.data, form1.delivery_date.data, form1.count.data)
        return render_template('deliveries.html', form=form, form1=form,
                               res=[{'product_id': '', 'store_id': '', 'delivery_date': '', 'count': ''}])
    return render_template('deliveries.html', form=form, form1=form,
                           res=[{'product_id': '', 'store_id': '', 'delivery_date': '', 'count': ''}])


if __name__ == '__main__':
    app.run(debug=True)
