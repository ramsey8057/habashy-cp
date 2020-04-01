from functions.database.database import execute_dml_query, execute_dql_query

def get_all_service_cards():
    query = f'''
    SELECT *
    FROM service_cards
    '''
    return execute_dql_query(query)
