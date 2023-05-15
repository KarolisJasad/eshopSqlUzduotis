import PySimpleGUI as sg
import eshop
import eshop_frontend_main

window = eshop_frontend_main.window

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "-EXIT-":
        break
    elif event == "-ADD_CUSTOMER-":
        eshop_frontend_main.addcustomer_layout()
    elif event == "-ADD_PRODUCT-":
        eshop_frontend_main.addproduct_layout()
    elif event == "-ADD_STATUS-":
        eshop_frontend_main.addstatus_layout()
    elif event == "-ADD_ORDER-":
        eshop_frontend_main.addorder_layout()
    elif event == "-ORDER_CHECK-":
        eshop_frontend_main.get_order_product_join()
    elif event == "-OPTIONS-":
        eshop_frontend_main.options_buttons()

window.close()