# flask 기본코드------------------------------
from flask import Flask, render_template, jsonify, request, redirect, url_for
app = Flask(__name__)

import jwt
import datetime
import hashlib
from werkzeug.utils import secure_filename
from datetime import datetime, timedelta

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
# 아래코드는 서버에 배포시
#client = MongoClient('mongodb://test:test@localhost', 27017) # Connection Setting시 유저 네임과 비밀번호를 입력해줘야되요 ex) MongoClient('mongodb://아이디:비번@localhost',27017)
db = client.mbti

# HTML 보여주기 - 수민 + 민진 -------------------------------------
@app.route('/')
def home():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        return render_template('feature_post.html')
    except jwt.ExpiredSignatureError:
        return redirect(url_for("start", msg="로그인 시간이 만료되었습니다."))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("start", msg="로그인 정보가 존재하지 않습니다."))

@app.route('/start')
def start():
    msg = request.args.get("msg")
    return render_template('sign_up.html', msg=msg)

@app.route('/discussion')
def discussion():
    post_num = "0"
    return render_template('discussion_post.html', post_num = post_num)


# 성윤님 -----------------------------------------------------
@app.route('/discussion_post_comments')
def discussion_post_comments():
    return render_template('discussion_post_comments.html')

@app.route('/api/free_posts', methods = ['GET'])
def get_free_posts():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        free_posts = list(db.free_posts.find({}))
        # posts = list(db.posts.find({}).sort("date", -1).limit(20))
        print(free_posts)
        for free_post in free_posts:
            free_post['_id'] = str(free_post['_id'] )
            free_post['user_id'] = str(free_post['user_id'])
            free_post['post_title'] = str(free_post['post_title'])
            free_post['post_content'] = str(free_post['post_content'])
            print(free_post['post_title'], free_post['post_content'])

        return jsonify({"result": "success", "msg": "포스팅을 가져왔습니다.", "free_posts": free_posts})
    except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
        return redirect(url_for("home"))

@app.route('/api/update_like', methods = ['POST'])
def update_like():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.users.find_one({"user_id": payload["id"]})
        feature_post_id_receive = request.form["feature_post_id_give"]
        type_receive = request.form["type_give"]
        action_receive = request.form["action_give"]
        doc = {
            "feature_post_id": feature_post_id_receive,
            "user_id": user_info["user_id"],
            "type": type_receive
        }
        if action_receive == "like":
            db.likes.insert_one(doc)
        else:
            db.likes.delete_one(doc)
        like = db.likes.count_documents({"post_id": feature_post_id_receive})
        return jsonify({"result": "success", 'msg': 'updated', "like": like})
    except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
        return redirect(url_for("home"))

# 병찬님 -----------------------------------------------------
@app.route('/discussion_post_add')
def discussion_post_add():
    return render_template('discussion_post_add.html')

@app.route('/discussion_post_back')
def discussion_back():
    return render_template('discussion_post.html')


@app.route('/discussion_post_complete')
def discussion_post():
    return render_template('discussion_post.html')

@app.route("/api/mbti_features_posts", methods=["POST"])
def board_post():
    token_receive = request.cookies.get('mytoken')

    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms = ['HS256'])
        user_info = payload["id"]
        post_title_receive = request.form['post_title_give']
        post_content_receive = request.form['post_content_give']

        doc = {
            'user_id': user_info,
            'post_title': post_title_receive,
            'post_content': post_content_receive
        }
        db.free_posts.insert_one(doc)
        return jsonify({"result":"success",'msg':"성공"})
    except(jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
        return redirect(url_for("home"))

# 민진님 -----------------------------------------------------

# < 특징 게시판 - 선택한 MBTI의 특징들 가져오기 API >
@app.route('/api/mbti_features_posts', methods=['GET'])
def select_mbti_feature():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        mbti_receive = request.form['mbti_give']
        print(mbti_receive)
        features = list(db.Feature.find({'feature_mbti': mbti_receive},{'_id':False}).sort('like', -1))

        for feature in features:
            feature["_id"] = str(feature["_id"])
            feature["like"] = db.likes.count_documents({"feature_id": feature["_id"], "type": "heart"})
            feature["heart_by_me"] = bool(db.likes.find_one({"feature_id": feature["_id"], "type": "heart", "user_id": payload['id']}))
            feature["feature_content"] = str(feature["feature_content"])
            feature["mbti"] = mbti_receive

        return jsonify({'the_mbti_features': features, 'msg': f'{mbti_receive}의 특징으로 이동합니다.'})
    except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
        return redirect(url_for("home"))

# < 논의 게시판 - 포스트 삭제 API >
@app.route('/api/free_posts', methods=['DELETE'])
def delete_post():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        post_id_receive = request.form['post_id_give']
        db.Post.delete_one({'user_id': payload['id'], 'Post._id': post_id_receive})
        return jsonify({'msg': '삭제 완료!'})
    except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
        return redirect(url_for("home"))

# < 논의 게시판 - 댓글 불러오기 API >
@app.route('/api/comments', methods=['GET'])
def show_comments():
    post_id = request.args.get('post_id')
    comments = list(db.Comment.find({'': post_id}))
    return jsonify({'all_comments': comments})

# 수진님 -----------------------------------------------------

app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config['UPLOAD_FOLDER'] = "./static/profile_pics"

SECRET_KEY = 'SPARTA'

# 로그인 API
@app.route('/api/login', methods=['POST'])
def log_in():
    username_receive = request.form['username_give']
    password_receive = request.form['password_give']

    pw_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()
    result = db.User.find_one({'user_id': username_receive, 'user_pw': pw_hash})

    if result is not None:
        payload = {
         'id': username_receive,
         'exp': datetime.utcnow() + timedelta(seconds=60 * 60 * 24)  # 로그인 24시간 유지
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        return jsonify({'result': 'success', 'token': token})
    # 찾지 못하면
    else:
        return jsonify({'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'})

# 회원가입 API
@app.route('/api/signup/save', methods=['POST'])
def sign_up():
    username_receive = request.form['username_give']
    password_receive = request.form['password_give']
    nickname_receive = request.form['nickname_give']
    mbti_receive = request.form['mbti_give']
    password_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()
    doc = {
        "user_id": username_receive,                               # 아이디
        "user_pw": password_hash,                                  # 비밀번호
        "user_nickname": nickname_receive,                          # 닉네임
        "user_mbti": mbti_receive                                  # mbti
    }
    db.User.insert_one(doc)
    return jsonify({'result': 'success'})

# 중복확인 API
@app.route('/api/signup/check_dup', methods=['POST'])
def check_dup():
    username_receive = request.form['username_give']
    exists = bool(db.User.find_one({"user_id": username_receive}))
    # print(value_receive, type_receive, exists)
    return jsonify({'result': 'success', 'exists': exists})

# 수민님 -----------------------------------------------------
# [논의 게시판 게시글 수정 바로 가기]
@app.route('/discussion/post/comments')
def discussion_page():
    return render_template('discussion_post_add.html')

# [논의 게시판 댓글 쓰기]
@app.route("/comment", methods=["POST"])
def comment_post():
    comment_receive = request.form['comment_give']

    doc = {
        'comment': comment_receive
    }

    db.Comment.insert_one(doc)

    return jsonify({'msg': '등록 완료!'})


@app.route("/comment", methods=["GET"])
def comment_get():
    comment_list = list(db.Comment.find({}, {'_id': False}))
    return jsonify({'comments': comment_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)