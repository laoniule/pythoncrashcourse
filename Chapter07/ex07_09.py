#!/usr/bin/python

sandwich_orders = ["五香烟熏牛肉","鸡蛋三明治","五香烟熏牛肉","三文鱼三明治", "火腿三明治","五香烟熏牛肉"]
finished_sandwiches = []

print(sandwich_orders)

while "五香烟熏牛肉" in sandwich_orders:
    sandwich_orders.remove("五香烟熏牛肉")
    
    print(sandwich_orders)


