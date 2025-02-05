import mysql.connector
from config import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE

def get_db_connection():
    return mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE
    )

def fetch_relevant_data(query: str) -> list[str]:
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    search_query = """
        SELECT content 
        FROM documents 
        WHERE MATCH(content) AGAINST(%s IN NATURAL LANGUAGE MODE)
        LIMIT 5
    """
    cursor.execute(search_query, (query,))
    results = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    return [doc['content'] for doc in results]