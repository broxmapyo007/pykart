try:
    import requests as rq  # request url pages
    from requests import *
    from bs4 import BeautifulSoup  # get elements,value,tags...
    from prettytable import PrettyTable
    import os,sys
except Exception as err:
    print(err)
    print("\nThis package require : request,bs4,prettytable")
    for i in ("requests","bs4","prettytable"):
        print(f"pip install {i}")
    print("\n")

# _________________________________

class pykart:
    def __init__(self,product):
        print("-" * 50, "\nProduct Details from python- Web Scrapping \n\t\t website : Flipkart....")

        #defaul flipkart search url
        self.url = "https://www.flipkart.com/search?q="
        self.product = product
        print("Product : ",self.product)
        self.search_url = self.url+self.product.replace(" ","%20")
        print("Search url :",self.search_url)
        #page URL
        self.pg = "&page=" # = pageno.
        self.soup=False;self.pg_no=1
        self.page_request(self.search_url)
        self.pg_ls=[]
    def page_request(self,url):
        try:
            product_page = get(url)  # .text
            pg_html = product_page.text
            if product_page.status_code == 200:
                self.bs4_soup(pg_html)
            else:
                raise Exception
        except:
            print("Network problem OR page loading Error re-try.")
            self.new_pro()
        return "Page status :"+str(product_page.status_code)
    def bs4_soup(self,pg_html):
        #bs4 help to find and explore pg_html
        if len(pg_html)>100:
                self.soup=BeautifulSoup(pg_html,"lxml")
                return "soup formed"
        else:
            return "Wrong page html"
    def pg_title(self):
        # title of page
        if self.soup:
            print("\n \t\t Page Title :", self.soup.title.text,"\n")
        else:
            print("request page/product first")
        return ""
    def save_code(self):
        fname=f"Product_{self.product}_code.txt"
        fp = open(fname, "w+")
        if self.soup:
            x=self.soup.prettify()
            fp.write(str(self.soup.title) + "\n")
            for i in range(x.index("<body>"), len(x) + 1):
                try:
                    s = x[i]
                    fp.write(s)
                except Exception as er:
                    #'charmap' codec can't encode character '\u20b9' in position 0: character maps to <undefined>
                    continue

            print(f"Page_body code saved in {fname}.")
        else:
            print("No page code Found...")
        fp.close()
    def pg_count(self):
        try:
            if self.soup:
                result_count = self.soup.find(class_="_10Ermr")
                c=result_count.text.split()
                return c
            else:
                raise Exception
        except:
            return "No request Product Match"
    def product_details(self):
        """types: modal :   s1Q9rs,_4rR01T,IRpwTa
        a. _4ddWXP #box view vertical > s1Q9rs
        b. _3pLy-c row #horizontal > _4rR01T
        c. _2B099V  #wearing >IRpwTa
        d.
        """
        if self.soup:
            type=["_4ddWXP","_3pLy-c row","_2B099V"]
            if self.soup.find("div",class_=type[0]):
                # print("t1")
                self.pro_det(type[0],"s1Q9rs");#self.type0()
            elif self.soup.find("div",class_=type[1]):
                # print("t2")
                self.pro_det(type[1],"_4rR01T");#self.type1()
            elif self.soup.find("div",class_=type[2]):
                # print("t3")
                self.pro_det(type[2],"IRpwTa");#self.type2()
            else:
                print("search new product ...")
    def pro_det(self,box,mod):
        try:
            print("\n\tProduct details table...")
            if self.soup:
                models = self.soup.findAll("div",class_=box)
                field = ["Sr no.","Model ","Rating","Buying price","original price","discount"]
                self.products=[];ix=0;
                for i in models:
                    ix+=1;data=["","","","","",""]
                    #model
                    data.pop(0)
                    data.insert(0,len(models)-(len(models)-ix))
                    if i.find(class_=mod):
                        p_model=i.find(class_=mod)
                        data.pop(1)
                        data.insert(1,p_model.text)
                    #rating
                    if i.find(class_="_3LWZlK"):
                        p_rating = i.find(class_="_3LWZlK")
                        data.pop(2)
                        data.insert(2,p_rating.text)
                    #Price
                    if i.find(class_="_30jeq3"):
                        b_price=i.find(class_="_30jeq3")
                        data.pop(3)
                        data.insert(3,(b_price.text)[1:])
                    if i.find(class_="_3I9_wc"):
                        o_price=i.find(class_="_3I9_wc")
                        data.pop(4)
                        data.insert(4,(o_price.text)[1:])
                    #discount percentage
                    if i.find(class_="_3Ay6Sb"):
                        p_dicount=i.find(class_="_3Ay6Sb")
                        data.pop(5)
                        data.insert(5,p_dicount.text)
                    self.products.append(data)
                print(self.form_tb(self.products,field))
            else:
                raise Exception
        except Exception as e:
            print("No request Product",e)
    def pg_ls(self):
        return self.pg_ls
    def form_tb(self,data,fields):
        if data and fields:
            self.pg_ls.extend(data)
            x = PrettyTable()
            x.field_names = fields
            for i in data:
                x.add_row(list(i))
            return x
        else:
            return "No datas / fields found"
    def next_pg(self):
        try:
            self.pg_no+=1
            new_url=self.search_url+self.pg+str(self.pg_no)
            print(" urls : ",new_url)
            self.page_request(new_url)
            self.pg_count()
            self.product_details()
        except:
            print("Wrong something try again.")
            self.next_pg()
    def prev_pg(self):
        try:
            if self.pg_no<2:
                print("\nAlready on First page.\n")
                return
            self.pg_no-=1
            new_url=self.search_url+self.pg+str(self.pg_no)
            print(" urls : ",new_url)
            self.page_request(new_url)
            self.pg_count()
            self.product_details()
        except:
            print("Wrong something try again.")
            self.next_pg()
