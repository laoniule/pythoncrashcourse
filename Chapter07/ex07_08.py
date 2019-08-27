#!/usr/bin/python

sandwich_orders = ["鸡蛋三明治", "三文鱼三明治", "火腿三明治"]
finished_sandwiches = []

print(sandwich_orders)

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(sandwich_orders)
    finished_sandwiches.append(sandwich)

print(finished_sandwiches)
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)
