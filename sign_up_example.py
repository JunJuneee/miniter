from flask import Flask, jsonify, request, current_app
from sqlalchemy import create_engine,text
import bcrypt

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

@app.route("/sign-up", methods=['POST']) 
def sign_up(): 
    new_user                = request.json
    new_user['password'] = bcrypt.hashpw(new_user['password'].encode('UTF-8'),bcrypt.gensalt())
    new_user_id = app.database.execute(text("""
        INSERT INTO users (
            name,
            email,
            profile,
            hashed_password
        ) VALUES (
            :name,
            :email,
            :profile,
            :password
        )
    """), user).lastrowid
    
    row = current_app.database.execute(text("""
        SELECT 
            id,
            name,
            email,
            profile
        FROM users
        WHERE id = :user_id
    """), {
        'user_id' : new_user_id 
    }).fetchone()

    created_user = {
        'id'      : row['id'],
        'name'    : row['name'],
        'email'   : row['email'],
        'profile' : row['profile']
    } if user else None

    return jsonify(created_user)


