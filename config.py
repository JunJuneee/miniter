db = {
  'user' : 'root',
  'password' : 'password',
  'host' : 'localhost',
  'port' : 3306,
  'database' : 'miniter'
}

# 접속할 db url
DB_URL = "mysql+mysqlconnector://root:password@localhost:3306/miniter"
# DB_URL = f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}"
# 이상하게 아래 url로 하면 애러가 뜬다
