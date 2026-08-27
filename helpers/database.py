db = "db"

def create_database_string(host, port):
    return f"{db}://{host}:{port}"
