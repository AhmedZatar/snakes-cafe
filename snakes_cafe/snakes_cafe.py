menulist=['wings', 'cookies', 'spring rolls', 'salmon', 'steak', 'meat tornado', 'a literal garden', 'ice Cream', 'cake', 'pie', 'coffee', 'tea', 'unicorn tears']

print(
    """
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************
Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************


    """
)
theOrderlist=[]
namesOfOrder=[]
def orderHandler():
    
    order=input('>')
    if order.lower() in menulist:
        theOrderlist.append(order)
        if order not in namesOfOrder:
            namesOfOrder.append(order)
        print(f'** {theOrderlist.count(order)} order of {order} have been added to your meal **')
        orderHandler()
    elif order.lower()=='quit':
        print('**Your order**')
        for x in namesOfOrder:
            print(f'{theOrderlist.count(x)} order of {x} ')
        print('**Thank you for visiting our Cafe**')
        print('**We are working on your order**')
    elif order.lower() not in menulist:
        print('**Your order is not in our menu**')
        orderHandler()

orderHandler()