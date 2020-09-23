from flask import Flask, jsonify, request 
from flask.json import JSONEncoder



## Default JSON encoder는 set를 JSON으로 변환할 수 없다.
## 그럼으로 커스텀 엔코더를 작성해서 set을 list로 변환하여
## JSON으로 변환 가능하게 해주어야 한다.
class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)

        return JSONEncoder.default(self, obj)

@app.route('/follow', methods=['POST'])
def follow():
  user_to_follow = request.json
  follow = user_to_follow['follow']

  app.database.execute(text("""
        INSERT INTO users_follow_list (
            user_id,
            follow_user_id
        ) VALUES (
            :id,
            :follow
        )
    """), user_to_follow)
  
  return '', 200


@app.route('/unfollow', methods=['POST'])
def unfollow():
  user_to_unfollow = request.json
  unfollow = user_to_follow['follow']


  app.database.execute(text("""
        DELETE FROM users_follow_list
        WHERE user_id = :id
        AND follow_user_id = :unfollow
    """), user_to_unfollow)

  return '', 200
   



