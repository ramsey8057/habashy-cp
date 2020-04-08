from functions.database.database import execute_dml_query, execute_dql_query

def get_information():
    query = f'''
    SELECT *
    FROM information
    LIMIT 1
    '''
    return execute_dql_query(query)

def update_information(old_email, email, main_phone, other_phone, address, city, footer_description):
    query = f'''
    UPDATE information
    SET
        email = '{email}',
        main_phone = '{main_phone}',
        other_phone = '{other_phone}',
        address = '{address}',
        city = '{city}',
        footer_description = '{footer_description}'
    WHERE email = '{old_email}'
    '''
    return (execute_dml_query(query) >= 1)

