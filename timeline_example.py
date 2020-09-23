# -*- coding: utf-8 -*- 
from flask import Flask, jsonify, request 
from flask.json import JSONEncoder

if __name__ == '__main__':
    app          = Flask(__name__)
    app.run(host='0.0.0.0', port=5000, debug=True)
## Default JSON encoder는 set를 JSON으로 변환할 수 없다.
## 그럼으로 커스텀 엔코더를 작성해서 set을 list로 변환하여
## JSON으로 변환 가능하게 해주어야 한다.
class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)

        return JSONEncoder.default(self, obj)


app.json_encoder = CustomJSONEncoder

@app.route('/timeline/<int:user_id>', methods=['GET'])
def timeline(user_id):
  rows = app.database.execute(text("""
        SELECT 
          t.user_id,
          t.tweet
        FROM tweets t
        LEFT JOIN users_follow_list ufl ON ufl.user_id = :user_id
        WHERE t.user_id = :user_id 
        OR t.user_id = ufl.follow_user_id
    """), {
        'user_id' : user_id 
    }).fetchall()

  timeline= [{
      'user_id' : tweet['user_id'],
      'tweet'   : tweet['tweet']
  } for row in rows]
  return jsonify({
      'user_id' : tweet['user_id'],
      'tweet'   : tweet['tweet']
  })
