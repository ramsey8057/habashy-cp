from functions.database.database import execute_dml_query, execute_dql_query

def get_new_customer_id():
    query = f'''
    SELECT customer_id
    FROM customers
    ORDER BY customer_id DESC
    LIMIT 1
    '''
    res = execute_dql_query(query)
    if len(res) < 1:
        return 1
    else:
        return res[0][0] + 1

def get_all_customers():
    query = f'''
    SELECT *
    FROM customers
    ORDER BY customer_id
    '''
    return execute_dql_query(query)

def get_customer(customer_name):
    query = f'''
    SELECT *
    FROM customers
    WHERE customer_name = {customer_name}
    '''
    return execute_dql_query(query)

def delete_customer(customer_name):
    query = f'''
    DELETE
    FROM customers
    WHERE customer_name = '{customer_name}'
    '''
    return (execute_dml_query(query) >= 1)

def add_customer(customer_id, customer_name, customer_image_path):
    query = f'''
    INSERT INTO customers
    (
        customer_id,
        customer_image_path,
        customer_name
    )
    VALUES
    (
        {customer_id},
        '{customer_image_path}',
        '{customer_name}'
    )
    '''
    return (execute_dml_query(query) >= 1)

def update_customer(old_customer_name, customer_name, customer_image_path):
    query = f'''
    UPDATE customers
    SET
        customer_name = '{customer_name}',
        customer_image_path = '{customer_image_path}'
    WHERE customer_name = '{old_customer_name}'
    '''
    return (execute_dml_query(query) >= 1)

def update_customer_name(old_customer_name, customer_name):
    query = f'''
    UPDATE customers
    SET customer_name = '{customer_name}'
    WHERE customer_name = '{old_customer_name}'
    '''
    return (execute_dml_query(query) >= 1)

def get_customer_image_path(customer_name):
    query = f'''
    SELECT customer_image_path
    FROM customers
    WHERE customer_name = '{customer_name}'
    '''
    return execute_dql_query(query)[0][0]

