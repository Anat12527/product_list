from sqlalchemy import create_engine
import pandas as pd
from datetime import datetime

engine = create_engine("mysql://root:newrootpassword@localhost/home_products_management")
excel_file = 'C:/Users/anatei/PycharmProjects/HelloWorld/FLASK_APP/product_lists.xlsx'
product_sheet = pd.read_excel(excel_file, sheet_name='list15-06-2020', header=None)
product_sheet2 = pd.read_excel(excel_file, sheet_name='list15-06-2020', header=None)
print(product_sheet.iloc[4, 5])
print(product_sheet.iloc[3, 1])

x = datetime.now()
y = datetime.now()
delta = y - (product_sheet.iloc[4, 5])
print(delta.days)

#def import_excel(sheet_name_l,dict_departments):
#  dict_products_by_department = dict()
#  engine = create_engine("mysql://root:newrootpassword@localhost/home_products_management")
#  names = ['Id_Product', 'Product_Name', 'Id_Department', 'Product_amount', 'Product_Notes', 'Date_Buy']
#  for num_department in dict_departments:
 #       Qall = QueriesMyDb(Products, dict_departments[num_department], Departments.department_name)
#        all_products_data = Qall.query_all_products()
#        if all_products_data:
#            dict_products_by_department[dict_departments[num_department]] = all_products_data
#  excel_file = 'C:/Users/anatei/PycharmProjects/HelloWorld/FLASK_APP/product_lists.xlsx'
#  len_prod_dict = len(dict_products_by_department)
#  product_sheet = pd.read_excel(excel_file, sheet_name=sheet_name_l,index_col=0, header=None,names=names)
#  product_sheet_s = product_sheet.sort_values(by=['Product_Name'], ascending=False)
#  product_sheet_s.iloc[:-(len_prod_dic+1)].to_sql(con=engine, name="products", if_exists='append',index=True)
#  return ("!!")

