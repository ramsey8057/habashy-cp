from functions.database.database import execute_dml_query, execute_dql_query

def get_all_service_cards():
    query = f'''
    SELECT *
    FROM service_cards
    ORDER BY service_id
    '''
    return execute_dql_query(query)

def get_service_card(service_id):
    query = f'''
    SELECT *
    FROM service_cards
    WHERE service_id = {service_id}
    '''
    return execute_dql_query(query)

def update_service_card(service_id, service_image_path, service_title, service_description, service_link):
    query = f'''
    UPDATE service_cards
    SET
        service_image_path = '{service_image_path }',
        service_title = '{service_title}',
        service_description = '{service_description}',
        service_link = '{service_link}'
    WHERE service_id = {service_id}
    '''
    return (execute_dml_query(query) >= 1)

def update_service_card_without_img(service_id, service_title, service_description, service_link):
    query = f'''
    UPDATE service_cards
    SET
        service_title = '{service_title}',
        service_description = '{service_description}',
        service_link = '{service_link}'
    WHERE service_id = {service_id}
    '''
    return (execute_dml_query(query) >= 1)

def get_service_card_image_path(service_id):
    query = f'''
    SELECT service_image_path
    FROM service_cards
    WHERE service_id = {service_id}
    '''
    return execute_dql_query(query)[0][0]

