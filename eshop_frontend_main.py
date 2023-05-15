import eshop
import PySimpleGUI as sg

BUTTON_SIZE = (15, 1)
OPTION_BUTTON_SIZE = (20, 1)
buttons_layout = [
        [sg.Button("Add Customer", key="-ADD_CUSTOMER-", size=BUTTON_SIZE)],
        [sg.Button("Add Product", key="-ADD_PRODUCT-", size=BUTTON_SIZE)],
        [sg.Button("Add Status", key="-ADD_STATUS-", size=BUTTON_SIZE)],
        [sg.Button("Add Order", key="-ADD_ORDER-", size=BUTTON_SIZE)],
        [sg.Button("Options", key="-OPTIONS-", size=BUTTON_SIZE)],
        [sg.Button("Check orders", key="-ORDER_CHECK-", size=BUTTON_SIZE)],
        [sg.Button("Exit", key="-EXIT-")]
]

window = sg.Window("Main Menu", buttons_layout)

def addcustomer_layout():
    customer_layout = [
        [sg.Text("First Name: "), sg.Input(key="-FIRST_NAME-")],
        [sg.Text("Last Name: "), sg.Input(key="-LAST_NAME-")],
        [sg.Text("Email: "), sg.Input(key="-EMAIL-")],
        [sg.Button("Add Customer", key="-ADD_CUSTOMER-"), sg.Button("Back", key="-BACK-")]
    ]
    customer_window = sg.Window("Add Customer", customer_layout)
    while True:
        event, values = customer_window.read()
        if event == sg.WINDOW_CLOSED:
            break
        elif event == "-ADD_CUSTOMER-":
            first_name = values["-FIRST_NAME-"]
            last_name = values["-LAST_NAME-"]
            email = values["-EMAIL-"]
            eshop.add_customer(first_name, last_name, email)
            sg.popup("Customer added successfully!")
            customer_window.close()
        elif event == "-BACK-":
            customer_window.close()

def addstatus_layout():
    status_layout = [
        [sg.Text("Status Name: "), sg.Input(key="-STATUS_NAME-")],
        [sg.Button("Add Status", key="-ADD_STATUS-"), sg.Button("Back", key="-BACK-")]
    ]
    status_window = sg.Window("Add Status", status_layout)
    while True:
        event, values = status_window.read()
        if event == sg.WINDOW_CLOSED:
            break
        elif event == "-ADD_STATUS-":
            status_name = values["-STATUS_NAME-"]
            eshop.add_status(status_name)
            sg.popup("Status added successfully!")
            status_window.close()
        elif event == "-BACK-":
            status_window.close()

def addproduct_layout():
    product_layout = [
        [sg.Text("Product Name"), sg.Input(key="-PRODUCT_NAME-")],
        [sg.Text("Product Price"), sg.Input(key="-PRODUCT_PRICE-")],
        [sg.Button("Add Product", key="-ADD_PRODUCT-"), sg.Button("Back", key="-BACK-")]
    ]
    product_window = sg.Window("Add Customer", product_layout)
    while True:
        event, values = product_window.read()
        if event == sg.WINDOW_CLOSED:
            break
        elif event == "-ADD_PRODUCT-":
            product_name = values["-PRODUCT_NAME-"]
            product_price = float(values["-PRODUCT_PRICE-"])
            eshop.add_product(product_name, product_price)
            sg.popup("Product added successfully!")
            product_window.close()
        elif event == "-BACK-":
            product_window.close()

def addorder_layout():
    order_layout = [
        [sg.Text("Customer ID"), sg.Input(key="-CUSTOMER_ID-")],
        [sg.Text("Status ID"), sg.Input(key="-STATUS_ID-")],
        [sg.Button("Add Order", key="-ADD_ORDER-"), sg.Button("Back", key="-BACK-")]
    ]
    order_window = sg.Window("Add Order", order_layout)
    while True:
        event, values = order_window.read()
        if event == sg.WINDOW_CLOSED:
            break
        elif event == "-ADD_ORDER-":
            customer_id = int(values["-CUSTOMER_ID-"])
            status_id = int(values["-STATUS_ID-"])
            eshop.add_order(customer_id, status_id)
            sg.popup("Order added successfully!")
            order_window.close()
        elif event == "-BACK-":
            order_window.close()

def get_order_product_join():
    joined_table = eshop.get_order_product_join()
    order_rows = []
    for order_product, order, customer, status, product in joined_table:
        order_row = [order_product.order_id, product.product_name, order_product.quantity, customer.first_name, customer.last_name, customer.email, status.status_name, order.date]
        order_rows.append(order_row)
    layout = [
        [sg.Table(values=order_rows, headings=["Order ID", "Product Name", "Quantity", "Customer First Name", "Customer Last Name", "Customer Email", "Order Status", "Date"], num_rows=10, justification="left")],
        [sg.Button("Close")]
    ]
    window = sg.Window("Order Details", layout)
    while True:
        event, _ = window.read()
        if event == sg.WINDOW_CLOSED or event == "Close":
            break
    window.close()

def order_by_id_layout():
    order_layout = [
        [sg.Text("Enter order ID:"), sg.Input(key="-ORDER_ID-")],
        [sg.Button("Get Order", key="-GET_ORDER-")],
        [sg.Button("Back", key="-BACK-")]
    ]
    order_window = sg.Window("Order by ID", order_layout)
    while True:
        event, values = order_window.read()
        if event == sg.WINDOW_CLOSED or event == "-BACK-":
            break
        elif event == "-GET_ORDER-":
            order_id = int(values["-ORDER_ID-"])
            order = eshop.get_order(order_id)
            if order:
                order_info = f"Užsakymo informacija:\nUžsakymo ID: {order.id}\nData: {order.date}\nKlientas: {order.customer.first_name} {order.customer.last_name} {order.customer.email}\nStatusas: {order.status.status_name}"
                sg.popup(order_info, title="Order Information")
            else:
                sg.popup("Užsakymas nerastas!")

    order_window.close()

def change_order_layout():
    change_order_layout = [
        [sg.Text("Enter order ID:"), sg.Input(key="-NEW_ORDER_ID-")],
        [sg.Text("Enter new status ID:"), sg.Input(key="-NEW_STATUS_ID-")],
        [sg.Button("Change order", key="-CHANGE_ORDER-")],
        [sg.Button("Back", key="-BACK-")]
    ]
    window = sg.Window("Change Order Status", change_order_layout)
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == "-BACK-":
            break
        elif event == "-CHANGE_ORDER-":
            order_id = int(values["-NEW_ORDER_ID-"])
            new_status_id = int(values["-NEW_STATUS_ID-"])
            eshop.change_order_status(order_id, new_status_id)
            sg.popup("Order status changed successfully!")
            break

    window.close()

def products_to_order_layout():
    products_to_order_layout = [
        [sg.Text("Enter order ID:"), sg.Input(key="-ORDER_ID-")],
        [sg.Text("Enter product ID:"), sg.Input(key="-PRODUCT_ID-")],
        [sg.Text("Enter quantity:"), sg.Input(key="-QUANTITY-")],
        [sg.Button("Add product", key="-ADD_PRODUCT-")],
        [sg.Button("Back", key="-BACK-")] 
    ]
    window = sg.Window("Add Products to Order", products_to_order_layout)
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == "-BACK-":
            break
        elif event == "-ADD_PRODUCT-":
            order_id = int(values["-ORDER_ID-"])
            product_id = int(values["-PRODUCT_ID-"])
            quantity = int(values["-QUANTITY-"])
            eshop.add_products_to_order(order_id, product_id, quantity)
            sg.popup("Product added to order successfully!")
            break

    window.close()

def options_buttons():
    options_layout = [
        [sg.Button("Get order by ID", key="-ORDER_BY_ID-", size=OPTION_BUTTON_SIZE)],
        [sg.Button("Change order Status by ID", key="-CHANGE_ORDER-", size=OPTION_BUTTON_SIZE)],
        [sg.Button("Add products to order", key="-ADD_PRODUCTS_ORDER-", size=OPTION_BUTTON_SIZE)],
        [sg.Button("Exit", key="-EXIT-")]
    ]
    options_window = sg.Window("Options", options_layout)
    while True:
        event, values = options_window.read()
        if event == sg.WINDOW_CLOSED or event == "-EXIT-":
            break
        elif event == "-ORDER_BY_ID-":
            order_by_id_layout()
        elif event == "-CHANGE_ORDER-":
            change_order_layout()
        elif event == "-ADD_PRODUCTS_ORDER-":
            products_to_order_layout()

    options_window.close()
