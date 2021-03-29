"""
    Autograde Lesson 3 assignment
    Run pytest
    Run cobverage and linitng using standard batch file
    Student should submit an empty database

"""

import pytest

import random

from src import basic_operations as l


@pytest.fixture
def _add_customers():
    return iter([  # adding iter
        ("123", "Name", "Lastname", "Address", "phone", "email", "active", 999),
        ("456", "Name", "Lastname", "Address", "phone", "email", "inactive", 10),
        ("123", "Name", "Lastname", "Address", "phone", "email", "active", 999),
        ("789", "Name", "Lastname", "Address", "phone", "email", "active", 0),
        ("345", "Name", "Lastname", "Address", "phone", "email", "active", -10),
        ("0123", "Name", "Lastname", "Address", "phone", "email", "active", 999),
        ("777", "Name", "Lastname", "Address", "phone", "email", "active", 999)
    ])


@pytest.fixture
def _search_customers():  # needs to del with database
    return iter(
        [("998", "Name", "Lastname", "Address", "phone", "email", "active", 999),
         ("997", "Name", "Lastname", "Address", "phone", "email", "inactive", 10)])


@pytest.fixture
def _delete_customers():  # needs to del with database
    return [
        ("898", "Name", "Lastname", "Address", "phone", "email", "active", 999),
        ("897", "Name", "Lastname", "Address", "phone", "email", "inactive", 10)
    ]


@pytest.fixture
def _update_customer_credit():  # needs to del with database
    return [
        ("798", "Name", "Lastname", "Address", "phone", "email", "active", 999),
        ("797", "Name", "Lastname", "Address", "phone", "email", "inactive", 10),
        ("796", "Name", "Lastname", "Address", "phone", "email", "inactive", -99)
    ]


@pytest.fixture
def _list_active_customers():
    return random_whatever()

    # return [
    #     ("598", "Name", "Lastname", "Address", "phone", "email", "active", 999),
    #     ("597", "Name", "Lastname", "Address", "phone", "email", "inactive", 10),
    #     ("596", "Name", "Lastname", "Address", "phone", "email", "inactive", 99),
    #     ("595", "Name", "Lastname", "Address", "phone", "email", "active", 999),
    #     ("594", "Name", "Lastname", "Address", "phone", "email", "active", 10),
    #     ("593", "Name", "Lastname", "Address", "phone", "email", "active", 99)
    # ]


def random_whatever(count=10):
    i = 0
    while i < count:
        customer = [str(random.randint(0, 1000)), "Name", "Lastname", "Address", "phone", "email",
                    random.choice(['active', 'inactive']), random.randint(0, 1000)]
        yield customer
        i += 1


def test_list_active_customers(_list_active_customers):
    """ actives """
    active_count = 0

    for customer in _list_active_customers:
        if customer[-2] == 'active':
            active_count += 1
        l.add_customer(customer[0],
                       customer[1],
                       customer[2],
                       customer[3],
                       customer[4],
                       customer[5],
                       customer[6],
                       customer[7]
                       )
    actives = l.list_active_customers()

    assert actives == active_count

    for customer in _list_active_customers:
        l.delete_customer(customer[0])


def test_add_customer(_add_customers):
    """ additions """
    while True:
        try:
            customer = next(_add_customers)
        except StopIteration:
            break
        l.add_customer(customer[0],
                       customer[1],
                       customer[2],
                       customer[3],
                       customer[4],
                       customer[5],
                       customer[6],
                       customer[7]
                       )
        added = l.search_customer(customer[0])
        assert added["name"] == customer[1]
        assert added["lastname"] == customer[2]
        assert added["email"] == customer[5]
        assert added["phone_number"] == customer[4]
        l.delete_customer(customer[0])


def test_search_customer(_search_customers):
    """ search """
    while True:
        try:
            customer = next(_search_customers)
            # if customer == _search_customers[-1]:
            #     break

        except StopIteration:
            break
        l.add_customer(customer[0],
                       customer[1],
                       customer[2],
                       customer[3],
                       customer[4],
                       customer[5],
                       customer[6],
                       customer[7])

        result = l.search_customer(customer[1][1])
        assert result == {}

        result = l.search_customer(customer[0])
        assert result["name"] == customer[1]
        assert result["lastname"] == customer[2]
        assert result["email"] == customer[5]
        assert result["phone_number"] == customer[4]

        l.delete_customer(customer[0])


def test_delete_customer(_delete_customers):
    """ delete """
    for customer in _delete_customers:
        l.add_customer(customer[0],
                       customer[1],
                       customer[2],
                       customer[3],
                       customer[4],
                       customer[5],
                       customer[6],
                       customer[7]
                       )

        response = l.delete_customer(customer[0])
        assert response is True

        deleted = l.search_customer(customer[0])
        assert deleted == {}


def test_update_customer_credit(_update_customer_credit):
    """ update """
    for customer in _update_customer_credit:
        l.add_customer(customer[0],
                       customer[1],
                       customer[2],
                       customer[3],
                       customer[4],
                       customer[5],
                       customer[6],
                       customer[7]
                       )

    l.update_customer_credit("798", 0)
    l.update_customer_credit("797", 1000)
    l.update_customer_credit("797", -42)
    l.update_customer_credit("796", 500)
    with pytest.raises(ValueError) as excinfo:
        l.update_customer_credit("00100", 1000) # error
        assert 'NoCustomer'  in str(excinfo.value)