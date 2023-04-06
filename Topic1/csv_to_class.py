"""
Program: csv_to_class.py
Author: Tony Ehlert
Last date modified: 4/6/2023

The purpose of this program is to import a .csv file and then assign the data contained within it to class objects
and then using methods to perform calculations on the data contain within the classes

The input is a .csv file containing Iowa census data and the required data needed to create and test objects created
The output is prints to the console of the total population of Iowa and the population/household of Dallas county
"""
import csv


class IowaCounty():
    """IowaCounty Class"""

    def __init__(self, rank, per_capita, med_hh_inc, med_fam_inc, pop, num_hh):
        self._rank = rank
        self._per_capita_income = per_capita
        self._med_hhold_income = med_hh_inc
        self._med_fam_income = med_fam_inc
        self._population = pop
        self._num_of_hhold = num_hh

    @property
    def rank(self):
        return self._rank

    @rank.setter
    def set_rank(self, rank):
        self.self._rank = rank

    @property
    def per_capita_income(self):
        return self._per_capita_income

    @per_capita_income.setter
    def set_per_capita_income(self, per_capita_income):
        self.self._per_capita_income = per_capita_income

    @property
    def med_hhold_income(self):
        return self._med_hhold_income

    @med_hhold_income.setter
    def set_med_hhold_income(self, med_hhold_income):
        self.self._med_hhold_income = med_hhold_income

    @property
    def med_fam_income(self):
        return self._med_fam_income

    @med_fam_income.setter
    def set_med_fam_income(self, med_fam_income):
        self.self._med_fam_income = med_fam_income

    @property
    def population(self):
        return self._population

    @population.setter
    def set_population(self, population):
        self.self._population = population

    @property
    def num_of_hhold(self):
        return self._num_of_hhold

    @num_of_hhold.setter
    def set_num_of_hhold(self, num_of_hhold):
        self.self._num_of_hhold = num_of_hhold

    def __str__(self):
        attributes = dir(self)
        str_string = self.__class__.__name__ + "("
        first = True
        for attr in attributes:
            if attr.startswith("__") and attr.endswith("__"):
                continue
            elif attr.startswith("set_") or attr.startswith("_"):
                continue
            if (first):
                first = False
            else:
                str_string += ", "

            str_string += attr + " = " + str(getattr(self, attr))

        str_string += ")"
        return str_string

    def __repr__(self):
        repr_str = "IowaCounty(" + str(self._rank)
        repr_str += ", " + str(self._per_capita_income)
        repr_str += ", " + str(self._med_hhold_income)
        repr_str += ", " + str(self._med_fam_income)
        repr_str += ", " + str(self._population)
        repr_str += ", " + str(self._num_of_hhold) + ")"
        return repr_str


def cnty_pop_per_household(counties, cnty_name):
    """
    This method accepts a dictionary of County objects and a string representing a county name,
    and then calculates and returns the population per household for the county

    :param counties: dictionary of County objects
    :param cnty_name: name of county
    :return: calculated population per household of county
    """
    return int(counties[cnty_name]._population.replace(',', '')) / int(
        counties[cnty_name]._num_of_hhold.replace(',', ''))


def total_population(counties):
    """
    This method accepts a dictionary of County objects and sums the population across all County objects within the
    dictionary

    :param counties: dictionary of County objects
    :return: total population of all County object within the dictionary
    """
    # create variable to hold running total of population
    total_pop = 0

    # loop through each object in dictionay and add population to running total
    for key, value in counties.items():
        total_pop += int(value._population.replace(',', ''))

    # return of the running total
    return total_pop


# driver
if __name__ == "__main__":
    # open the csv file
    with open(
            "C:\\Users\\te\OneDrive - AG Express\\CIS189 Python\\Module 12\\Iowa 2010 Census Data Population Income.csv") as csv_file:

        # create a csv reader object
        csv_reader = csv.reader(csv_file, delimiter=",")

        # set line count to 0
        line_count = 0

        # initialize an empty dictionary
        counties = {}

        # loop through records contained in csv_reader object
        for row in csv_reader:
            # skip first line in csv file due to it being a header
            if line_count == 0:
                line_count += 1
                continue
            # check for null rank, if true continue without creating object
            elif row[0] == '':
                line_count += 1
                continue
            counties[str(row[1])] = IowaCounty(row[0], row[2], row[3], row[4], row[5], row[6])

        # for key, value in counties.items():
        # print(key + ", Population = " +  str(value._population))

        # print the total population of Iowa
        print("Total Population in Iowa: " + str(total_population(counties)))

        # create variable to hold population per household for Dallas county
        dallas_cnty_pop_hh = cnty_pop_per_household(counties, "Dallas")

        # print formatted population per household for Dallas county
        print(f"Dallas County Population/Houshold: {dallas_cnty_pop_hh: .2f}")

        # test of __str__ method
        print(counties["Dallas"])

        # test of __repr__ method
        print(counties["Dallas"].__repr__())
