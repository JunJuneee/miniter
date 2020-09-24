import bcrypt
import jwt

def create_app(test_config = None):
    app = Flask(__name__)

    if test_config is None:
        app.config.from_pyfile("config.py")
    else:
        app.config.update(test_config)

    database     = create_engine(app.config['DB_URL'], encoding = 'utf-8', max_overflow = 0)
    app.database = database

    return app

if __name__ == '__main__':
    app          = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)

@app.route('/login',methods=['POST'])
def login():
  credential      = request.json
  email           = credential['email']
  password        = credential['password']
  
  row = app.database.execute(text("""
      SELECT 
        id,
        hashed_password,
      FROM users
      WHERE email = :email
    """), {'email' : email }).fetchone()
  
  if row and bcrypt.checkpw(password.encode('UTF-8'),row['hashed_password'].encode('UTF-8')):
    user_id = row['id']
    payload = {     
          'user_id' : user_id,
          'exp'     : datetime.utcnow() + timedelta(seconds = 60 * 60 * 24)
      }
    token = jwt.encode(payload, app.config['JWT_SECRET_KEY'], 'HS256'
    return jsonify({        
          'access_token' : token.decode('UTF-8')
      })
    else:
      return '', 401



