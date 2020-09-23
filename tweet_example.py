# -*- coding: utf-8 -*- 
from flask import Flask, jsonify, request 

if __name__ == '__main__':
  app = Flask(__name__)
  app.run(host='0.0.0.0', port=5000, debug=True)

@app.route('/tweet', methods=['POST'])
def tweet():
  user_tweet = request.json
  tweet = user_tweet['tweet']

  if len(tweet) > 300:
      return '300자를 초과했습니다', 400
  
  app.database.execute(text("""
        INSERT INTO tweets (
            user_id,
            tweet
        ) VALUES (
            :id,
            :tweet
        )
    """), user_tweet)
  
  return '', 200