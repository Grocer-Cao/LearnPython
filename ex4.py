# coding: utf-8
# cars 汽车数量
cars = 100
# space_in_a_car 车内空间
space_in_a_car = 4.0
# drivers 司机数量
drivers = 30
# passsengers 乘客数量
passsengers = 90
# cars_not_driven 未使用的汽车数
cars_not_driven = cars - drivers
# cars_driven 已使用的汽车数
cars_driven = drivers
# carpool_capacity 汽车的总承载能力
carpool_capacity = cars_driven * space_in_a_car
# average_passengers_per_car 汽车平均承载量
average_passengers_per_car = passsengers / cars_driven

# ++++++++++++++++++++++++++附加题++++++++++++++++++++++++++++++
# average_passengers_per_car = car_pool_capacity / passenger
#
# 第20行错误原因，car_pool_capacity与passenger都未定义，
# 程序员在输入变量名时输入了错误的名字，导致出现这一错误，通过IDE
# 可以及时发现这类错误，或者通过编译提示信息来查找和发现该错误
# 正确的输入方式见第27行：
#
# average_passengers_per_car = carpool_capacity / passsengers
#
#
# 1、4.0作为space_in_a_car没有必要,因为车内空间以人为单位时不可
#     能出现小数
# -------------------------------------------------------------

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty car today."
print "We can transport", carpool_capacity, "people today."
print "We have", passsengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
