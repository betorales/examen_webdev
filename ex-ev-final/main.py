from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('HomePage.html')


@app.route('/ejercicio-1', methods=['POST', 'GET'])
def ejercicio_uno():
    age_user = paint_buckets = total_price = total_price_discount = 0
    name_user = discount_price = total_price_msg = total_price_discount_msg = discount_price_msg = user_msg = ' '
    discount_price_zero = 0

    if request.method == 'POST':
        name_user = request.form["name"]
        age_user = int(request.form["age"])
        paint_buckets = int(request.form['paint'])
        price = 9000
        total_price = paint_buckets * price
        total_price_msg = 'Total sin descuento: $' + str(total_price)
        user_msg = 'Nombre del cliente: ' + name_user

        if age_user >= 18 and age_user <= 30:
            discount_pct = 0.15
            discount_price = total_price * discount_pct
            discount_price_msg = 'El descuento es: $' + str(discount_price)
        elif age_user > 30:
            discount_pct = 0.25
            discount_price = total_price * discount_pct
            discount_price_msg = 'El descuento es: $' + str(discount_price)
        else:
            discount_price_zero = 0

        total_price_discount = total_price - discount_price
        total_price_discount_msg = 'El total a pagar es de: $' + str(total_price_discount)

    return render_template('EjercicioUno.html',
                           name_user=name_user,
                           age_user=age_user,
                           paint_buckets=paint_buckets,
                           total_price=total_price,
                           discount_price=discount_price,
                           total_price_discount=total_price_discount,
                           discount_price_zero=discount_price_zero,
                           total_price_msg=total_price_msg,
                           discount_price_msg=discount_price_msg,
                           total_price_discount_msg=total_price_discount_msg,
                           user_msg=user_msg)


@app.route('/ejercicio-2', methods=['POST', 'GET'])
def ejercicio_dos():
    admin_usn = 'juan'
    admin_pwd = 'admin'
    user_usn = 'pepe'
    user_pwd = 'user'
    show_msg = ''
    name_username = ''
    password_username = ''

    if request.method == 'POST':
        name_username = request.form['username']
        password_username = request.form['password']
        if name_username == admin_usn and password_username == admin_pwd:
            show_msg = f"Bienvenido Administrador {admin_usn}"
        elif name_username == user_usn and password_username == user_pwd:
            show_msg = f"Bienvenido Usuario {user_usn}"
        else:
            show_msg = "Usuario o contraseña incorrectos"

    return render_template('EjercicioDos.html',
                           show_msg=show_msg,
                           name_username=name_username,
                           password_username=password_username)
