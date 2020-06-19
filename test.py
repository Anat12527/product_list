import unittest

import pandas as pd
from ex_4 import app, QueriesMyDb, Products, Departments
from sqlalchemy import create_engine


class MyQueriesTestClass(unittest.TestCase):
    # checks that  filtering by name
    def test_query_filter_name(self):
        query1 = QueriesMyDb(Products, "milk", Products.product_name)
        product_record = query1.query_filter_name()
        self.assertEqual(product_record.product_name, "milk")

    def test_filter_products_by_dept_name(self):
        # checks filtering products by department name.
        query2 = QueriesMyDb(Departments, "Dairy", Departments.department_name)
        department_record = query2.query_filter_name()
        query3 = QueriesMyDb(Products, "Dairy", Departments.department_name)
        all_products_data_by_dept = query3.filter_products_by_dept_name()
        self.assertEqual(all_products_data_by_dept[0].department_id, department_record.department_id)


class MysheetTestclass(unittest.TestCase):
    engine = create_engine("mysql://root:newrootpassword@localhost/home_products_management")

    def setUp(self):
        self.file1 = 'C:/Users/anatei/PycharmProjects/HelloWorld/FLASK_APP/product_lists.xlsx'
        self.sheet_name = 'list15-06-2020'
        self.col_row = 3, 1

    def test_export_import_list_val1(self):
        # checks the cell value compared to the database.
        product_sheet = pd.read_excel(self.file1, sheet_name=self.sheet_name, header=None)
        query1 = QueriesMyDb(Products, "milk", Products.product_name)
        product_record = query1.query_filter_name()
        self.assertEqual(product_sheet.iloc[self.col_row], product_record.product_name)

    def test_exoort_import_list_val2(self):
        # checks the cell value department id compared to the database.
        product_sheet = pd.read_excel(self.file1, sheet_name=self.sheet_name, header=None)
        query1 = QueriesMyDb(Products, "milk", Products.product_name)
        product_record = query1.query_filter_name()
        product_record.department_id
        self.assertEqual(product_sheet.iloc[3, 2], product_record.department_id)


class Mytestapp(unittest.TestCase):

    def test_log(self):
        tester = app.test_client(self)
        response = tester.get('/log', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # checks that the log in page loads as expected.
    def test_main_route_requires_login(self):
        tester = app.test_client(self)
        response = tester.get('/log', follow_redirects=True)
        self.assertIn(b'welcom', response.data)

    # checks that the user must be logged in order to load index_products.
    def test_logged_users(self):
        tester = app.test_client(self)
        response = tester.get('/index_products', follow_redirects=True)
        self.assertIn(b'You must login in order to access the app', response.data)


if __name__ == '__main__':
    unittest.main()
