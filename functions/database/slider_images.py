from functions.database.database import execute_dml_query, execute_dql_query

def get_new_slider_image_id():
    query = f'''
    SELECT element_id
    FROM slider_images
    ORDER BY element_id DESC
    LIMIT 1
    '''
    res = execute_dql_query(query)
    if len(res) < 1:
        return 1
    else:
        return res[0][0] + 1

def add_slider_image(path, title, description, slider):
    query = f'''
    INSERT INTO slider_images
    (
        element_id,
        element_image_path,
        element_title,
        element_description,
        element_slider
    )
    VALUES
    (
        {get_new_slider_image_id()},
        '{path}',
        '{title}',
        '{description}',
        '{slider}'
    )
    '''
    return (execute_dml_query(query) >= 1)

def get_all_slider_images():
    query = '''
    SELECT *
    FROM slider_images
    ORDER BY element_id
    '''
    return execute_dql_query(query)

def get_slider_image_by_id(element_id):
    query = f'''
    SELECT *
    FROM slider_images
    WHERE element_id = {element_id}
    ORDER BY element_id
    '''
    return execute_dql_query(query)

def delete_slider_image(slider_image_id):
    query = f'''
    DELETE FROM slider_images
    WHERE element_id = {slider_image_id}
    '''
    return (execute_dml_query(query) >= 1)

def get_slider_img_image_path(image_slider_id):
    query = f'''
    SELECT element_image_path
    FROM slider_images
    WHERE element_id = {image_slider_id}
    '''
    return execute_dql_query(query)[0][0]

