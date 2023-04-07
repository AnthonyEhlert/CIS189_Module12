"""
Program: test_customer_exceptions.py
Author: Tony Ehlert
Last date modified: 4/6/2023

The purpose of this program is to test the custom exceptions contained in teh customer_exceptions.py file
The input is the necessary data and code to create unit tests to test the custom exceptions
The output is testing results
"""
import unittest

from custom_exceptions.customer_exceptions import *


class CustomerExceptionsTestCase(unittest.TestCase):
    def setUp(self):
        self.customer = Customer('1234', 'Duck', 'Donald', '515-555-1234')

    def tearDown(self):
        del self.customer

    def test_valid_customer_id(self):
        self.assertEqual(self.customer.customer_id, '1234')

    def test_valid_last_name(self):
        self.assertEqual(self.customer.last_name, 'Duck')

    def test_valid_first_name(self):
        self.assertEqual(self.customer.first_name, 'Donald')

    def test_valid_phone_number(self):
        self.assertEqual(self.customer.phone_number, '515-555-1234')

    def test_invalid_customer_id(self):
        with self.assertRaises(InvalidCustomerIdException):
            customer = Customer('999', 'Duck', 'Donald', '515-555-1234')
        with self.assertRaises(InvalidCustomerIdException):
            customer = Customer('99999', 'Duck', 'Donald', '515-555-1234')
        with self.assertRaises(InvalidCustomerIdException):
            customer = Customer('abc', 'Duck', 'Donald', '515-555-1234')

    def test_invalid_last_name(self):
        with self.assertRaises(InvalidNameException):
            customer = Customer('1234', '1', 'Donald', '515-555-1234')

    def test_invalid_first_name(self):
        with self.assertRaises(InvalidNameException):
            customer = Customer('1234', 'Duck', '1', '515-555-1234')

    def test_invalid_phone_number(self):
        with self.assertRaises(InvalidPhoneNumberFormat):
            customer = Customer('1234', 'Duck', '1', '(515)-555-1234')

    def test_str(self):
        self.assertEqual(self.customer.__str__(), '1234: Duck, Donald Phone: 515-555-1234')


if __name__ == '__main__':
    CustomerExceptionsTestCase.main()