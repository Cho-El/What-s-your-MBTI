# flask 기본코드------------------------------
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
# 아래코드는 서버에 배포시
# client = MongoClient('mongodb://test:test@localhost', 27017) # Connection Setting시 유저 네임과 비밀번호를 입력해줘야되요 ex) MongoClient('mongodb://아이디:비번@localhost',27017)
db = client.mbti

# 성윤님 -----------------------------------------------------

# 병찬님 -----------------------------------------------------

# 민진님 -----------------------------------------------------

# [유저 정보 확인 API]
# 로그인된 유저만 call 할 수 있는 API입니다.
# 유효한 토큰을 줘야 올바른 결과를 얻어갈 수 있습니다. (그렇지 않으면 남의 장바구니라든가, 정보를 누구나 볼 수 있겠죠?)
@app.route('/api/nick', methods=['GET'])
def api_valid():
    token_receive = request.cookies.get('mytoken')
    # try / catch 문 : try 아래를 실행했다가, 에러가 있으면 except 구분으로 가라는 뜻
    try:
        # token을 시크릿키로 디코딩합니다.
        # 보실 수 있도록 payload를 print 해두었습니다. 우리가 로그인 시 넣은 그 payload와 같은 것이 나옵니다.
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        print(payload)

        # payload 안에 id가 들어있습니다. 이 id로 유저정보를 찾습니다.
        # 여기에선 그 예로 닉네임을 보내주겠습니다.
        userinfo = db.user.find_one({'id': payload['id']}, {'_id': 0})
        return jsonify({'result': 'success', 'nickname': userinfo['nick']})
    except jwt.ExpiredSignatureError:
        # 위를 실행했는데 만료시간이 지났으면 에러가 납니다.
        return jsonify({'result': 'fail', 'msg': '로그인 시간이 만료되었습니다.'})
    except jwt.exceptions.DecodeError:
        return jsonify({'result': 'fail', 'msg': '로그인 정보가 존재하지 않습니다.'})

# [특징 게시판 - 제목, 내용 가져오기 API]
@app.route('/api/mbti_features_posts', methods=['GET'])
def read_features():
    features = list(db.Features.find({'my_mbti_type':selected_mbti}))
    return jsonify({'all_features': features})

# [논의 게시판 - 삭제 API]
@app.route('/api/free_posts', methods=['DELETE'])
def delete_post():
    db.Posts.delete_one({'Posts._id': post_id})
    return jsonify({'msg': '삭제 완료!'})

# [논의 게시판 - 댓글 불러오기 API]
@app.route('/api/comments', methods=['GET'])
def read_comments():
    comments = list(db.Comments.find({'Posts._id': post_id}))
    return jsonify({'all_comments': comments})


# 수진님 -----------------------------------------------------

# 수민님 -----------------------------------------------------

# [논의 게시판 댓글 쓰기]
@app.route("/comment", methods=["GET"])
def comment_get():
    comment_list = list(db.comment.find({}, {'_id': False}))
    return jsonify({'comments': comment_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)