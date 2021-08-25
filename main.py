from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'MMCAXcUQxV'

@app.route("/")
def ingredients():
    conn = sqlite3.connect("storage.db")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM Ingredients")
    data = cur.fetchall()
    return render_template("ingredients.html", item=data)

@app.route("/supply")
def supply():
    conn = sqlite3.connect("storage.db")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM Ingredients")
    data = cur.fetchall()
    return render_template("supply.html", item=data)

@app.route("/supplies", methods=['POST'])
def supplies():
    if request.method == 'POST':
        supplier_id = request.form['supplier_id']
        supplier_name = request.form['supplier_name']
        supplier_contact = request.form['supplier_contact']
        supplier_address = request.form['supplier_address']
        unit = request.form['unit']
        unit_quantity = request.form['unit_quantity']
        quantity = request.form['quantity']
        cup_quantity = request.form['cup_quantity']
        price = request.form['price']

        with sqlite3.connect("storage.db") as conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO Ingredients (supplier_id, supplier_name, supplier_contact, supplier_address, unit, unit_quantity, quantity, cup_quantity, price, supply_datetime) VALUES (?,?,?,?,?,?,?,?,?,DATETIME())", (supplier_id, supplier_name, supplier_contact, supplier_address, unit, unit_quantity, quantity, cup_quantity, price))
            conn.commit()
            return redirect(url_for("supply"))

@app.route("/coffee")
def coffee():
    return render_template("coffee.html")

@app.route("/order", methods=['POST'])
def order():
    if request.method == 'POST':
        coffee_id = request.form.get('coffee_id')
        amount = request.form.get('amount')

        with sqlite3.connect("storage.db") as conn:
            cur = conn.cursor()
            if coffee_id == "SA":
                cur.execute("UPDATE Ingredients SET unit_quantity=unit_quantity-(100*?), cup_quantity=cup_quantity-? WHERE unit='Americano' AND quantity='Small'", (amount, amount))
                conn.commit()
                return redirect(url_for("coffee"))
            elif coffee_id == "MA":
                cur.execute("UPDATE Ingredients SET unit_quantity=unit_quantity-(200*?), cup_quantity=cup_quantity-? WHERE unit='Americano' AND quantity='Medium'", (amount, amount))
                conn.commit()
                return redirect(url_for("coffee"))
            elif coffee_id == "LA":
                cur.execute("UPDATE Ingredients SET unit_quantity=unit_quantity-(300*?), cup_quantity=cup_quantity-? WHERE unit='Americano' AND quantity='Large'", (amount, amount))
                conn.commit()
                return redirect(url_for("coffee"))
            elif coffee_id == "SC":
                cur.execute("UPDATE Ingredients SET unit_quantity=unit_quantity-(100*?), cup_quantity=cup_quantity-? WHERE unit='Cappuccino' AND quantity='Small'", (amount, amount))
                conn.commit()
                return redirect(url_for("coffee"))
            elif coffee_id == "MC":
                cur.execute("UPDATE Ingredients SET unit_quantity=unit_quantity-(200*?), cup_quantity=cup_quantity-? WHERE unit='Cappuccino' AND quantity='Medium'", (amount, amount))
                conn.commit()
                return redirect(url_for("coffee"))
            elif coffee_id == "LC":
                cur.execute("UPDATE Ingredients SET unit_quantity=unit_quantity-(300*?), cup_quantity=cup_quantity-? WHERE unit='Cappuccino' AND quantity='Large'", (amount, amount))
                conn.commit()
                return redirect(url_for("coffee"))
            elif coffee_id == "SE":
                cur.execute("UPDATE Ingredients SET unit_quantity=unit_quantity-(100*?), cup_quantity=cup_quantity-? WHERE unit='Espresso' AND quantity='Small'", (amount, amount))
                conn.commit()
                return redirect(url_for("coffee"))
            elif coffee_id == "ME":
                cur.execute("UPDATE Ingredients SET unit_quantity=unit_quantity-(200*?), cup_quantity=cup_quantity-? WHERE unit='Espresso' AND quantity='Medium'", (amount, amount))
                conn.commit()
                return redirect(url_for("coffee"))
            elif coffee_id == "LE":
                cur.execute("UPDATE Ingredients SET unit_quantity=unit_quantity-(300*?), cup_quantity=cup_quantity-? WHERE unit='Espresso' AND quantity='Large'", (amount, amount))
                conn.commit()
                return redirect(url_for("coffee"))

if __name__ ==  "__main__":
    app.run(debug=True)