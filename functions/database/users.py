from functions.database.database import execute_dml_query, execute_dql_query

def get_new_user_id():
    query = f'''
    SELECT user_id
    FROM users
    ORDER BY user_id DESC
    LIMIT 1
    '''
    return (execute_dql_query(query)[0][0] + 1)

def check_username_and_password(username, password):
    query = f'''
    SELECT *
    FROM users
    WHERE username = '{username}'
    AND password = '{password}'
    '''
    return (len(execute_dql_query(query)) >= 1)

def log_user_in(username, password):
    query = f'''
    UPDATE users
    SET is_logged_in = TRUE
    WHERE username = '{username}'
    AND password = '{password}'
    AND is_logged_in = FALSE
    '''
    return (execute_dml_query(query) >= 1)

def add_user(username, password, is_admin):
    query = f'''
    INSERT INTO users
    (
        user_id,
        username,
        password,
        is_admin
    )
    VALUES
    (
        {get_new_user_id()},
        '{username}',
        '{password}',
        {is_admin}
    )
    '''
    return (execute_dml_query(query) >= 1)

def update_current_user_password(username, password):
    query = f'''
    UPDATE users
    SET password = '{password}'
    WHERE username = '{username}'
    AND is_logged_in = TRUE
    '''
    return (execute_dml_query(query) >= 1)

def get_all_users():
    query = '''
    SELECT user_id, username, is_admin
    FROM users
    WHERE user_id > 0
    ORDER BY user_id
    '''
    return execute_dql_query(query)

def delete_user(username):
    query = f'''
    DELETE FROM users
    WHERE username = '{username}'
    AND user_id > 0
    AND is_logged_in = FALSE
    '''
    return (execute_dml_query(query) >= 1)
    
def check_is_admin(username):
    query = f'''
    SELECT is_admin
    FROM users
    WHERE username = '{username}'
    '''
    return execute_dql_query(query)

def log_user_out(username, password):
    query = f'''
    UPDATE users
    SET is_logged_in = FALSE
    WHERE username = '{username}'
    AND PASSWORD = '{password}'
    AND is_logged_in = TRUE
    '''
    return (execute_dml_query(query) >= 1)

def check_if_user_available(username):
    query = f'''
    SELECT user_id
    FROM users
    WHERE username = '{username}'
    '''
    return (len(execute_dql_query(query)) <= 0)

def get_user_data(username):
    query = f'''
    SELECT username, is_admin
    FROM users
    WHERE username = '{username}'
    '''
    return execute_dql_query(query)

def edit_user_with_password(old_username, username, password, is_admin):
    query = f'''
    UPDATE users
    SET
        username = '{username}',
        password = '{password}',
        is_admin = {is_admin}
    WHERE username = '{old_username}'
    AND is_logged_in = FALSE
    '''
    return (execute_dml_query(query) >= 1)

def edit_user_without_password(old_username, username, is_admin):
    query = f'''
    UPDATE users
    SET
        username = '{username}',
        is_admin = {is_admin}
    WHERE username = '{old_username}'
    AND is_logged_in = FALSE
    '''
    return (execute_dml_query(query) >= 1)
