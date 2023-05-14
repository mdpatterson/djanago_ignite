from ..helpers.sql_helper import TableNames, Query, TestData
from pyignite import Client

def my_data_from_ignite(my_option):

    # establish connection
    # client = Client(username='ignite', password='ignite')
    client = Client()
    with client.connect('127.0.0.1', 10800):
        try:
            # create tables
            for query in [
                Query.COUNTRY_CREATE_TABLE,
                Query.CITY_CREATE_TABLE,
                Query.LANGUAGE_CREATE_TABLE,
            ]:
                client.sql(query)

            # create indices
            for query in [Query.CITY_CREATE_INDEX, Query.LANGUAGE_CREATE_INDEX]:
                client.sql(query)

            # load data
            for row in TestData.COUNTRY:
                client.sql(Query.COUNTRY_INSERT, query_args=row)

            for row in TestData.CITY:
                client.sql(Query.CITY_INSERT, query_args=row)

            for row in TestData.LANGUAGE:
                client.sql(Query.LANGUAGE_INSERT, query_args=row)

            # 10 most populated cities (with pagination)
            rows = []
            MY_SQL_STR = 'SELECT name, population FROM City ORDER BY population DESC LIMIT ' + my_option
            with client.sql(MY_SQL_STR) as cursor:
                #print('Most 10 populated cities:')
                for row in cursor:
                    rows.append(row)
        except:
            cleanuptables()

    return rows


def cleanuptables():
    # Clean up
    client = Client()
    with client.connect('127.0.0.1', 10800):
        for table_name in TableNames:
            result = client.sql(Query.DROP_TABLE.format(table_name.value))
        rows = "ERROR: cleaning up"

