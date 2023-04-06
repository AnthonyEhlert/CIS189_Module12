"""
Program: customer_exceptions.py
Author: Tony Ehlert
Last date modified: 4/6/2023

The purpose of this program is to create custom exceptions to be used with the Customer class

The input is necessary data and code needed to create the custom exceptions and Customer class as well as the
necessary data to test the Customer objects and custom exceptions

The output is prints to console indicating which custom exception was raised
"""


class Customer:
    '''Customer Class'''

    # constructor
    def __init__(self, cust_id, lname, fname, phone_num):
        # define supersets for validation
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        id_characters = set("1234567890")
        phone_num_characters = set("1234567890-")

        # check cust_id for validity
        if not (id_characters.issuperset(cust_id)) or (int(cust_id) < 1000 or int(cust_id) > 9999):
            raise InvalidCustomerIdException

        # check phone_num for validity
        if not (phone_num_characters.issuperset(phone_num)):
            raise InvalidPhoneNumberFormat
        if len(phone_num) != 12:
            raise InvalidPhoneNumberFormat
        for i in range(12):
            if i in [3, 7]:
                if phone_num[i] != '-':
                    raise InvalidPhoneNumberFormat

        # check lname for validity
        if not (name_characters.issuperset(lname)):
            raise InvalidNameException

        # check fname for validity
        if not (name_characters.issuperset(fname)):
            raise InvalidNameException

        self._customer_id = cust_id
        self._last_name = lname
        self._first_name = fname
        self._phone_number = phone_num

    @property
    def customer_id(self):
        return self._customer_id

    @customer_id.setter
    def customer_id(self, value):
        id_characters = set("1234567890")
        if not id_characters.issuperset(value) or (int(value) < 1000 or int(value) > 9999):
            raise InvalidCustomerIdException
        self._customer_id = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        if not (name_characters.issuperset(value)):
            raise InvalidNameException
        self._last_name = value

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        if not (name_characters.issuperset(value)):
            raise InvalidNameException
        self._first_name = value

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_num(self, value):
        phone_num_characters = set("1234567890-")
        if not phone_num_characters.issuperset(value):
            raise InvalidPhoneNumberFormat
        if len(value) != 12:
            raise InvalidPhoneNumberFormat
        for i in range(12):
            if i in [3, 7]:
                if value[i] != '-':
                    raise InvalidPhoneNumberFormat
        self._phone_number = value

    def __str__(self):
        return self.customer_id + ": " + self.last_name + ", " + self.first_name + " Phone: " + self.phone_number

    def __repr__(self):
        return 'Customer({},{},{},{})'.format(self.customer_id, self.last_name, self.first_name, self.phone_number)

    def change_last_name(self, name):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        if not (name_characters.issuperset(name)):
            raise InvalidNameException
        self.last_name = name

    def change_first_name(self, name):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        if not (name_characters.issuperset(name)):
            raise InvalidNameException
        self.first_name = name

    def change_phone_number(self, number):
        phone_num_characters = set("1234567890-")
        if not phone_num_characters.issuperset(number):
            raise InvalidPhoneNumberFormat
        if len(number) != 12:
            raise InvalidPhoneNumberFormat
        for i in range(12):
            if i in [3, 7]:
                if number[i] != '-':
                    raise InvalidPhoneNumberFormat
        self.phone_number = number

    def display(self):
        return self.customer_id + ": " + self.last_name + ", " + self.first_name + " Phone: " + self.phone_number


# CUSTOM EXCEPTIONS
class InvalidCustomerIdException(Exception):
    """InvalidCustomerIdException is derived class of Exception base class"""
    pass


class InvalidNameException(Exception):
    """InvalidNameException is derived class of Exception base class"""
    pass


class InvalidPhoneNumberFormat(Exception):
    """InvalidPhoneNumberFormat is derived class of Exception base class"""
    pass


if __name__ == "__main__":
    # Valid customer
    customer_one = Customer('1234', 'Duck', 'Donald', '555-555-5555')

    # call __str__ and __repr__
    print(customer_one)
    print(customer_one.__repr__())

    # Invalid phone format
    try:
        customer_two = Customer('1234', 'Duck', 'Donald', '(555)555-5555')
    except InvalidPhoneNumberFormat:
        print("InvalidPhoneNumberFormat raised, phone_number: (515)555-5555, customer not created")

    # Invalid customer_id with alpha characters
    try:
        customer_two = Customer('ABC', 'Duck', 'Donald', '555-555-5555')  # all required
    except InvalidCustomerIdException:
        print("InvalidCustomerIdException raised, customer_id: 'ABC', customer not created")

    # Invalid customer_id with id outside of 1000-9999
    try:
        customer_two = Customer('999', 'Duck', 'Donald', '555-555-5555')  # all required
    except InvalidCustomerIdException:
        print("InvalidCustomerIdException raised, customer_id: '999', customer not created")

    # Invalid last_name
    try:
        customer_two = Customer('1234', '1', 'Donald', '555-555-5555')
    except InvalidNameException:
        print("InvalidNameException raised, last_name: '1', customer not created")

    # Invalid first_name
    try:
        customer_two = Customer('1234', 'Duck', '2', '555-555-5555')  # all required
    except InvalidNameException:
        print("InvalidNameException raised, first_name: '2', customer not created")

    # garbage collection
    del (customer_one)
