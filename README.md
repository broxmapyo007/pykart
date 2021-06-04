# pykart Module
  This module will be helpful for Web scraping data of product from an E-commerce site [flipkart].
  Product data like name,rating,price,discount.
  This way data gathering for product will become easy.
  Need 3 extra module :request,bs4,prettytable to get successfull output.

## Installation
Run the following to install:
```python
pip install pykart
```

##Usage
```python
import pykart as fk

product=input("Product name : ")
fop=fk.pykart(product) #flipkart_op

if fop:
    fop.pg_title()
    c=fop.pg_count()
    print("\n Results found per page : ",c[1],"to",c[3]," Total matches :",c[5])
    #data into table format on command line
    fop.product_details()
    #create control for next,previous page moments
    while True:
        pg_no=input("[Next Page] n | [previous pg] b | [save scrap code] save :")
        if pg_no.lower()=="n":
            fop.next_pg()
        elif pg_no.lower()=="b":
            fop.prev_pg()
        elif pg_no.lower()=="save":
            fop.save_code()
        else:
            print("end")
            break
    #product data in list
    fop.pg_ls()
```

# Developing pykart
To install pykart,along with the tools you need to develop and run tests,run the following in your virtualenv:
```bash
$ pip install -e .[dev]
```

## License
(c) 2021 Adesh Dangi
GNU GENERAL PUBLIC LICENSE 2007

This repository is licensed under the GNU license,
See LICENSE for details.
