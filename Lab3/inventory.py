#!/usr/bin/python
# -*- coding: utf-8 -*-

class Inventory:
    def __init__(self, inventory_id):
        self.inventory_id = inventory_id
        self.products = []

    def addItem(self, product):
        self.products.append(product)

    def deleteItem(self, product_id):
        self.products = [p for p in self.products if p.product_id != product_id]

    def updateItem(self, product_id, details):
        for p in self.products:
            if p.product_id == product_id:
                for key, value in details.items():
                    if hasattr(p, key):
                        setattr(p, key, value)
                break

    def getItems(self):
        return self.products
