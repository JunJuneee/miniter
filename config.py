db = {
  'user' : 'root',
  'password' : 'password',
  'host' : 'localhost',
  'port' : 3306,
  'database' : 'miniter'
}

# 접속할 db url
DB_URL = f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}"
JWT_SECRET_KEY = 'secret_key'