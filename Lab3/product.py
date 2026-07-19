#!/usr/bin/python
# -*- coding: utf-8 -*-
import uuid

class Product:
    def __init__(self, name, price, brand, description, discount=0.0):
        self.product_id = str(uuid.uuid4())
        self.name = name
        self.price = price
        self.brand = brand
        self.discount = discount
        self.description = description
