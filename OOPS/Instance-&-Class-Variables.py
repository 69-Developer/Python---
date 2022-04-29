class Apple_productprice:

    priceofIphone13promax = 129990
    iphone_store = 'Ghali Colony, Gadhinglaj'

Ritik = Apple_productprice()
Jash = Apple_productprice()

Ritik.buyingstore = 'House of Mobile , Gadhinglaj'
Jash.buyingstore = 'World of Mobile, Gadhinglaj'

Ritik.buyingprice = 125000
Ritik.buyingprice = 124000

print(Ritik.buyingstore)
print(Jash.buyingstore)

# print(Apple_productprice.priceofIphone13promax)
Ritik.priceofIphone13promax = 200000
# print(Apple_productprice.priceofIphone13promax)

# An Object cannot change the class variable and only class can change its variable

print(Apple_productprice.priceofIphone13promax)
Apple_productprice.priceofIphone13promax = 150000
print(Apple_productprice.priceofIphone13promax)

# When you try to change the varaible in the class by using Object it create an instance of the particular object

# To prove 

print(Apple_productprice.__dict__)
print(Ritik.__dict__)
Ritik.priceofIphone13promax = 100000
print(Ritik.__dict__)