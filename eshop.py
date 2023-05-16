from sqlalchemy import create_engine, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import DeclarativeBase, mapped_column, relationship, sessionmaker
from datetime import datetime
from typing import Any
import PySimpleGUI as sg

db_engine = create_engine('sqlite:///eshop.db')
Session = sessionmaker(bind=db_engine)
session = Session()

class Base(DeclarativeBase):
    pass

class OrderProduct(Base):
    __tablename__='order_product'
    id = mapped_column(Integer, primary_key=True)
    order_id = mapped_column("order_id", Integer, ForeignKey('order.id'))
    product_id = mapped_column("product_id", Integer, ForeignKey('product.id'))
    quantity = mapped_column("quantity", Integer)
    order = relationship("Order", back_populates="order_products")
    product = relationship("Product")

class Product(Base):
    __tablename__='product'
    id = mapped_column(Integer, primary_key=True)
    product_name = mapped_column("product_name", String(50))
    product_price = mapped_column("product_price", Float(50))
    order_products = relationship("OrderProduct", back_populates="product")

class Order(Base):
    __tablename__='order'
    id = mapped_column(Integer, primary_key=True)
    customer_id = mapped_column('customer_id', Integer, ForeignKey('customer.id'))
    date = mapped_column('date', String(50))
    status_id = mapped_column('status_id', ForeignKey('status.id'))
    customer = relationship("Customer", back_populates="orders")
    status = relationship("Status", back_populates="orders")
    order_products = relationship("OrderProduct", back_populates="order")

class Status(Base):
    __tablename__='status'
    id = mapped_column(Integer, primary_key=True)
    status_name = mapped_column('stats_name', String(50))
    orders = relationship("Order", back_populates="status")

class Customer(Base):
    __tablename__='customer'
    id = mapped_column(Integer,primary_key=True)
    first_name = mapped_column('first_name', String(50))
    last_name = mapped_column('last_name', String(50))
    email = mapped_column('email', String(50))
    orders = relationship("Order", back_populates="customer")

def add_customer(first_name, last_name, email):
    # first_name = input("Enter customer's first name: ")
    # last_name = input("Enter customer's last name: ")
    # email = input("Enter customer's email: ")
    customer = Customer(first_name=first_name, last_name=last_name, email=email)
    session.add(customer)
    session.commit()
    print(f"Pirkėjas {first_name} pridėtas!")

def add_product(product_name, product_price):
    product = Product(product_name=product_name, product_price=product_price)
    session.add(product)
    session.commit()
    print(f"Prekė pavaidinimu: {product_name} pridėtas sėkmingai!")

def add_status(status_name):
    status = Status(status_name=status_name)
    session.add(status)
    session.commit()
    print("Statusas pridėtas!")

def add_order(customer_id, status_id):
    order = Order(customer_id=customer_id, date=datetime.now().strftime("%Y-%m-%d"), status_id=status_id)
    session.add(order)
    session.commit()
    print("Užsakymas pridėtas")

# Užsakymas pagal ID

def get_order(order_id):
    order = session.get(Order, order_id)
    return order
    # if order:
    #     print("Užsakymo informacija:")
    #     print(f"Užsakymo ID: {order.id}")
    #     print(f"Data: {order.date}")
    #     print(f"Klientas: {order.customer.first_name} {order.customer.last_name} {order.customer.email}")
    #     print(f"Statusas: {order.status.status_name}")
    # else:
    #     print("Užsakymas nerastas!")

def change_order_status(order_id, new_status_id):
    order = session.get(Order, order_id)
    if order:
        order.status_id = new_status_id
        session.commit()

def add_products_to_order(order_id, product_id, quantity):
    order = session.get(Order, order_id)
    if order:
        product = session.get(Product, product_id)
        if product:
            order_product = OrderProduct(order_id=order_id, product_id=product_id, quantity=quantity)
            session.add(order_product)
            session.commit()

def get_order_product_join():
    query = session.query(OrderProduct, Order, Customer, Status, Product).select_from(OrderProduct).join(Order).join(Customer).join(Status).join(Product)
    joined_table = query.all()
    return joined_table

# def print_menu():
#     print("1. Add Customer")
#     print("2. Add Product")
#     print("3. Add Status")
#     print("4. Add Order")
#     print("5. Add Products to Order")
#     print("6. Get Order by ID")
#     print("7. Change Order Status")
#     print("8. Check all orders")
#     print("9. Exit")

# get_order_product_join()

# add_customer("Mindaugas", "Turauskas", "mindturaus@gmail.com")
# add_product("Pele", 39)
# add_status("Parduotas")
# add_status("Neparduotas")
# add_status("Išsiųstas")
# add_order(1,3)

# get_order(1)
# change_order_status(1,1)
# get_order(1)
# add_products_to_order(3, 3, 5)

# Base.metadata.create_all(db_engine)
# testas

# while True:
#     print_menu()
#     choice = input("Enter your choice: ")

#     if choice == "1":
#         add_customer()
#     elif choice == "2":
#         add_product()
#     elif choice == "3":
#         add_status()
#     elif choice == "4":
#         add_order()
#     elif choice == "5":
#         add_products_to_order()
#     elif choice == "6":
#         get_order()
#     elif choice == "7":
#         change_order_status()
#     elif choice == "8":
#         get_order_product_join()
#     elif choice == "9":
#         break
#     else:
#         print("Invalid choice. Please try again.")
