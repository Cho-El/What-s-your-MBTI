from pymongo import MongoClient

# 0. 로컬 테스트용
client = MongoClient('localhost', 27017)
# 1. 서버에 배포시 - Github 업로드
# client = MongoClient('43.200.170.125', 27017, username="test", password="test")
db = client.mbti


# # 1. User 테이블
# 회원가입 하면 DB에 추가되니 -> 세팅 필요 없음
# User 테이블 초기화
# db.User.delete_many({})

# # ----------------------------------------

# # 2. Feature 테이블 추가
def db_setting():
    # Feature 테이블 초기화
    # db.Feature.delete_many({})
    # Feature 테이블에 데이터 넣기
    db.Feature.insert_many([
        # 1. ISTJ
        {"feature_mbti": 'ISTJ', "like": 199, "feature_content": '청렴결백함'},
        {"feature_mbti": 'ISTJ', "like": 54, "feature_content": '논리적임'},
        {"feature_mbti": 'ISTJ', "like": 4, "feature_content": '헌신적으로 임무를 수행함'},
        {"feature_mbti": 'ISTJ', "like": 54, "feature_content": '책임감이 강함'},
        {"feature_mbti": 'ISTJ', "like": 204, "feature_content": '목표 달성을 위해 시간과 에너지를 허투루 쓰지 않음'},
        {"feature_mbti": 'ISTJ', "like": 398, "feature_content": '필요한 업무를 정확하고 신중히 처리함'},
        {"feature_mbti": 'ISTJ', "like": 420, "feature_content": '내가 생각해도 나는 군대와 같이 전통, 질서가 중요한 조직에 잘 어울림'},
        {"feature_mbti": 'ISTJ', "like": 21, "feature_content": '매우 성실함'},
        {"feature_mbti": 'ISTJ', "like": 417, "feature_content": '가정에 충실함'},

        # 2. ISFJ
        {"feature_mbti":'ISFJ', "like": 199, "feature_content": '자기 자신에게 엄격함'},
        {"feature_mbti":'ISFJ', "like": 54, "feature_content": '책임감과 인내심이 강함'},
        {"feature_mbti":'ISFJ', "like": 4, "feature_content": '해결사'},
        {"feature_mbti":'ISFJ', "like": 54, "feature_content": '완벽주의자'},
        {"feature_mbti":'ISFJ', "like": 204, "feature_content": '개인 시간 방해받는 것을 정말 싫어함'},
        {"feature_mbti":'ISFJ', "like": 398, "feature_content": '남에게 피해 주는 것을 싫어함'},
        {"feature_mbti":'ISFJ', "like": 420, "feature_content": '예의 바른 성격'},
        {"feature_mbti":'ISFJ', "like": 21, "feature_content": '공감 능력이 뛰어남'},
        {"feature_mbti":'ISFJ', "like": 417, "feature_content": '반복적인 일에 최적임'},

        # 3. INFJ
        {"feature_mbti": 'INFJ', "like": 199, "feature_content": '인내심이 많음'},
        {"feature_mbti": 'INFJ', "like": 54, "feature_content": '통찰력과 직관력이 뛰어남'},
        {"feature_mbti": 'INFJ', "like": 4, "feature_content": '화합을 추구함'},
        {"feature_mbti": 'INFJ', "like": 54, "feature_content": '창의력이 좋음'},
        {"feature_mbti": 'INFJ', "like": 204, "feature_content": '강한 직관력으로 타인에게 말없이 영향을 끼침'},
        {"feature_mbti": 'INFJ', "like": 398, "feature_content": '자기 내부의 갈등이 많고 복잡함'},
        {"feature_mbti": 'INFJ', "like": 420, "feature_content": '내적 독립심이 강함'},
        {"feature_mbti": 'INFJ', "like": 21, "feature_content": '나무보다 숲을 보는 편'},
        {"feature_mbti": 'INFJ', "like": 417, "feature_content": '풍부하고 감성적인 내면이 있음'},

        # 4. INTJ
        {"feature_mbti": 'INTJ', "like": 199, "feature_content": '지식을 향한 갈증이 있음'},
        {"feature_mbti": 'INTJ', "like": 54, "feature_content": '어릴때 "책벌레"라는 소리를 자주 들음'},
        {"feature_mbti": 'INTJ', "like": 4, "feature_content": '지붕을 뚫는 자존감'},
        {"feature_mbti": 'INTJ', "like": 54, "feature_content": '규칙과 법규는 질색'},
        {"feature_mbti": 'INTJ', "like": 204, "feature_content": '모든 걸 이해하려고 함'},
        {"feature_mbti": 'INTJ', "like": 398, "feature_content": '수학 좋아함'},
        {"feature_mbti": 'INTJ', "like": 420, "feature_content": '직설적임'},
        {"feature_mbti": 'INTJ', "like": 21, "feature_content": '비밀이 많음'},
        {"feature_mbti": 'INTJ', "like": 417, "feature_content": '고집 셈'},

        # 5. ISTP
        {"feature_mbti": 'ISTP', "like": 199, "feature_content": '의심 많음'},
        {"feature_mbti": 'ISTP', "like": 54, "feature_content": '솔직하고 직선적'},
        {"feature_mbti": 'ISTP', "like": 4, "feature_content": '자기 주장 강함'},
        {"feature_mbti": 'ISTP', "like": 54, "feature_content": '사람 많은 곳 싫어함'},
        {"feature_mbti": 'ISTP', "like": 204, "feature_content": '틀에 박힌 일상 좋아함'},
        {"feature_mbti": 'ISTP', "like": 398, "feature_content": '뭐든 잘하고 싶어함'},
        {"feature_mbti": 'ISTP', "like": 420, "feature_content": '창의적임'},
        {"feature_mbti": 'ISTP', "like": 21, "feature_content": '과묵함'},
        {"feature_mbti": 'ISTP', "like": 417, "feature_content": '혼자 일함'},

        # 6. ISFP
        {"feature_mbti": 'ISFP', "like": 199, "feature_content": '독립적임'},
        {"feature_mbti": 'ISFP', "like": 54, "feature_content": '겸손함'},
        {"feature_mbti": 'ISFP', "like": 4, "feature_content": '몽상가'},
        {"feature_mbti": 'ISFP', "like": 54, "feature_content": '신중함'},
        {"feature_mbti": 'ISFP', "like": 204, "feature_content": '사람 많은 곳 싫어함'},
        {"feature_mbti": 'ISFP', "like": 398, "feature_content": '잘 들어줌'},
        {"feature_mbti": 'ISFP', "like": 420, "feature_content": '까칠해보이지만 여림'},
        {"feature_mbti": 'ISFP', "like": 21, "feature_content": '낙천적'},
        {"feature_mbti": 'ISFP', "like": 417, "feature_content": '평판 신경 안 쓰고 하고 싶은 거 함'},

        # 7. INFP
        {"feature_mbti": 'INFP', "like": 199, "feature_content": '생각이 너무 많음'},
        {"feature_mbti": 'INFP', "like": 54, "feature_content": '뛰어난 공감능력'},
        {"feature_mbti": 'INFP', "like": 4, "feature_content": '단체 생활보단 혼자 있는 게 좋음'},
        {"feature_mbti": 'INFP', "like": 54, "feature_content": '스스로를 아싸라 생각함'},
        {"feature_mbti": 'INFP', "like": 204, "feature_content": '감성적임'},
        {"feature_mbti": 'INFP', "like": 398, "feature_content": '사람들에게 관심이 많음'},
        {"feature_mbti": 'INFP', "like": 420, "feature_content": '예술 혹은 글쓰기에 뛰어남'},
        {"feature_mbti": 'INFP', "like": 21, "feature_content": '상처 받기 쉬움'},
        {"feature_mbti": 'INFP', "like": 417, "feature_content": '몽상가'},

        # 8. INTP
        {"feature_mbti": 'INTP', "like": 199, "feature_content": '아이디어만 오백만개'},
        {"feature_mbti": 'INTP', "like": 54, "feature_content": '중립적임'},
        {"feature_mbti": 'INTP', "like": 4, "feature_content": '의심이 많음'},
        {"feature_mbti": 'INTP', "like": 54, "feature_content": '가끔 무례함'},
        {"feature_mbti": 'INTP', "like": 204, "feature_content": '맨날 딴 생각 중'},
        {"feature_mbti": 'INTP', "like": 398, "feature_content": '\'왜?\''},
        {"feature_mbti": 'INTP', "like": 420, "feature_content": '공감하지만 지지하지 않음'},
        {"feature_mbti": 'INTP', "like": 21, "feature_content": '너무 솔직함'},
        {"feature_mbti": 'INTP', "like": 417, "feature_content": '깊고 좁은 인간관계'},

        # 9. ESTP
        {"feature_mbti": 'ESTP', "like": 199, "feature_content": '자기 주장이 강함'},
        {"feature_mbti": 'ESTP', "like": 54, "feature_content": '관종임'},
        {"feature_mbti": 'ESTP', "like": 4, "feature_content": '도전을 사랑함'},
        {"feature_mbti": 'ESTP', "like": 54, "feature_content": '금방 질림'},
        {"feature_mbti": 'ESTP', "like": 204, "feature_content": '솔직하고 직설적'},
        {"feature_mbti": 'ESTP', "like": 398, "feature_content": '자존심이 강함'},
        {"feature_mbti": 'ESTP', "like": 420, "feature_content": '낙천주의자'},
        {"feature_mbti": 'ESTP', "like": 21, "feature_content": '핵인싸'},
        {"feature_mbti": 'ESTP', "like": 417, "feature_content": 'YOLO'},

        # 10. ESFP
        {"feature_mbti": 'ESFP', "like": 199, "feature_content": '사랑꾼'},
        {"feature_mbti": 'ESFP', "like": 54, "feature_content": '자유로움'},
        {"feature_mbti": 'ESFP', "like": 4, "feature_content": '도전정신이 강함'},
        {"feature_mbti": 'ESFP', "like": 54, "feature_content": '친목 좋아함'},
        {"feature_mbti": 'ESFP', "like": 204, "feature_content": '아이디어가 넘침'},
        {"feature_mbti": 'ESFP', "like": 398, "feature_content": '핵인싸'},
        {"feature_mbti": 'ESFP', "like": 420, "feature_content": '현재를 즐김'},
        {"feature_mbti": 'ESFP', "like": 21, "feature_content": '매우 열정적임'},
        {"feature_mbti": 'ESFP', "like": 417, "feature_content": '아이디어가 넘침'},

        # 11. ENFP
        {"feature_mbti": 'ENFP', "like": 199, "feature_content": '사람들을 알고 싶어함'},
        {"feature_mbti": 'ENFP', "like": 54, "feature_content": '금방 질림'},
        {"feature_mbti": 'ENFP', "like": 4, "feature_content": '퍼주는 것 좋아함'},
        {"feature_mbti": 'ENFP', "like": 54, "feature_content": '잘 흥분하고 별남'},
        {"feature_mbti": 'ENFP', "like": 204, "feature_content": '모순덩어리'},
        {"feature_mbti": 'ENFP', "like": 398, "feature_content": '모든 걸 시도하려 함'},
        {"feature_mbti": 'ENFP', "like": 420, "feature_content": '촉이 좋음'},
        {"feature_mbti": 'ENFP', "like": 21, "feature_content": '감성적임'},
        {"feature_mbti": 'ENFP', "like": 417, "feature_content": '정의로움'},

        # 12. ENTP
        {"feature_mbti": 'ENTP', "like": 199, "feature_content": '지나치게 솔직함'},
        {"feature_mbti": 'ENTP', "like": 54, "feature_content": '시끄러움'},
        {"feature_mbti": 'ENTP', "like": 4, "feature_content": '\'내말이 맞지\''},
        {"feature_mbti": 'ENTP', "like": 54, "feature_content": '공감능력 없음'},
        {"feature_mbti": 'ENTP', "like": 204, "feature_content": '아이디어가 넘침'},
        {"feature_mbti": 'ENTP', "like": 398, "feature_content": '말을 잘함'},
        {"feature_mbti": 'ENTP', "like": 420, "feature_content": '반항아'},
        {"feature_mbti": 'ENTP', "like": 21, "feature_content": '\'난 항상 옳아\''},
        {"feature_mbti": 'ENTP', "like": 417, "feature_content": '관종임'},

        # 13. ESTJ
        {"feature_mbti": 'ENTP', "like": 199, "feature_content": '단계적으로 계획을 세움'},
        {"feature_mbti": 'ENTP', "like": 54, "feature_content": '설명충'},
        {"feature_mbti": 'ENTP', "like": 4, "feature_content": '특이한 흥미'},
        {"feature_mbti": 'ENTP', "like": 54, "feature_content": '체계적임'},
        {"feature_mbti": 'ENTP', "like": 204, "feature_content": '기억력이 좋음'},
        {"feature_mbti": 'ENTP', "like": 398, "feature_content": '솔직함'},
        {"feature_mbti": 'ENTP', "like": 420, "feature_content": '감정표현에 서툼'},
        {"feature_mbti": 'ENTP', "like": 21, "feature_content": '디테일을 중시함'},
        {"feature_mbti": 'ENTP', "like": 417, "feature_content": '무질서를 싫어함'},

        # 14. ESFJ
        {"feature_mbti": 'ESFJ', "like": 199, "feature_content": '지식을 얻고자 함'},
        {"feature_mbti": 'ESFJ', "like": 54, "feature_content": '예의 바르고 친절함'},
        {"feature_mbti": 'ESFJ', "like": 4, "feature_content": '설명충'},
        {"feature_mbti": 'ESFJ', "like": 54, "feature_content": '본투비 리더'},
        {"feature_mbti": 'ESFJ', "like": 204, "feature_content": '핵인싸'},
        {"feature_mbti": 'ESFJ', "like": 398, "feature_content": '배려심이 있음'},
        {"feature_mbti": 'ESFJ', "like": 420, "feature_content": '완벽주의자임'},
        {"feature_mbti": 'ESFJ', "like": 21, "feature_content": '철벽 잘 침'},
        {"feature_mbti": 'ESFJ', "like": 417, "feature_content": '책임감이 있음'},

        # 15. ENFJ
        {"feature_mbti": 'ENFJ', "like": 199, "feature_content": '고집쟁이'},
        {"feature_mbti": 'ENFJ', "like": 54, "feature_content": '본투비 리더'},
        {"feature_mbti": 'ENFJ', "like": 4, "feature_content": '사람을 알고싶어함'},
        {"feature_mbti": 'ENFJ', "like": 54, "feature_content": '정이 넘침'},
        {"feature_mbti": 'ENFJ', "like": 204, "feature_content": '의리가 강함'},
        {"feature_mbti": 'ENFJ', "like": 398, "feature_content": '옳은 일을 하고 싶어함'},
        {"feature_mbti": 'ENFJ', "like": 420, "feature_content": '완벽주의자이자 이상주의자'},
        {"feature_mbti": 'ENFJ', "like": 21, "feature_content": '과한 열정'},
        {"feature_mbti": 'ENFJ', "like": 417, "feature_content": '임기응변에 강함'},

        # 16. ENTJ
        {"feature_mbti": 'ENTJ', "like": 199, "feature_content": '자존감이 높음'},
        {"feature_mbti": 'ENTJ', "like": 54, "feature_content": '논쟁에서 인정사정 없음'},
        {"feature_mbti": 'ENTJ', "like": 4, "feature_content": '효율적인 것 좋아함'},
        {"feature_mbti": 'ENTJ', "like": 54, "feature_content": '이겨야 직성이 풀림'},
        {"feature_mbti": 'ENTJ', "like": 204, "feature_content": '변화를 좋아함'},
        {"feature_mbti": 'ENTJ', "like": 398, "feature_content": '너무 솔직함'},
        {"feature_mbti": 'ENTJ', "like": 420, "feature_content": '통찰력이 있음'},
        {"feature_mbti": 'ENTJ', "like": 21, "feature_content": '모 아니면 도'},
        {"feature_mbti": 'ENTJ', "like": 417, "feature_content": '리더 기질'},
    ])
# # ----------------------------------------

# # # 3. free_posts 테이블

# 3-1. free_posts 테이블 초기화
# db.free_posts.delete_many({})

# 3-2. free_posts 테이블 데이터 세팅 틀
# db.free_posts.insert_many([
#     {"post_id":'', "user_id": "m_6595", "post_title": '깻잎논쟁', "post_content":'내 친구가 깻잎 떼는 것을 나의 이성친구가 도와줘도 되는가?' },
#     {"post_id":'', "user_id": "m_6595", "post_title": '롱패딩 논쟁', "post_content":'내 이성친구가 남/여사친의 롱패딩 지퍼를 올려줘도 되는가?' },
#     {"post_id":'', "user_id": "m_6595", "post_title": '"멍때리기"란?', "post_content":'멍때리기란, 아무 생각을 하지 않는 것인가? 잡생각을 하고 있는 것인가?' },
#     {"post_id":'', "user_id": "m_6595", "post_title": '"나 교통사고 났어"에 대한 대답은?', "post_content":''},
#     {"post_id":'', "user_id": "m_6595", "post_title": '영희와 철수, 누가 더 나쁜가?', "post_content":'나 도와주려다 내 과제에 커피를 쏟은 영희 vs 내 과제를 몰래 사진찍어간 철수'},
#     {"post_id":'', "user_id": "m_6595", "post_title": '시험에 떨어진 친구에게', "post_content":'가장 먼저 해줄 말은?'},
#     {"post_id":'', "user_id": "m_6595", "post_title": '"사과"하면 떠오르는 것은?', "post_content":'무엇인가?'},
#     {"post_id":'', "user_id": "m_6595", "post_title": '여행 가기 전 준비과정', "post_content":'여행 가기 전 모든 프로세스'},
#     {"post_id":'', "user_id": "m_6595", "post_title": '가끔 어떤 망상해?', "post_content":'말 그대로 어떤 망상함?'},
#     ])

# # ----------------------------------------

# # # 4. Comment 테이블

# 4-1. comment 테이블 초기화
# db.Comment.delete_many({})

# 4-2. comment 테이블 데이터 세팅 틀
# db.Comment.insert_many([
#     {"post_id":'62ee472a7909c222c092aedb', "user_id": "mvlkfm53", "user_nickname": '홍길동','user_mbti':'INTP',"comment_content":'쌉가능!!!!!!!!'},
#     {"post_id":'62ee472a7909c222c092aedb', "user_id": "flflkg5", "user_nickname": '김철수','user_mbti':'INTJ',"comment_content":'예민함'},
#     {"post_id":'62ee472a7909c222c092aedb', "user_id": "m6595", "user_nickname": '두부','user_mbti':'ESTJ',"comment_content":'이거가지고 왜 싸움'},
#     {"post_id":'62ee472a7909c222c092aedb', "user_id": "ffmffl", "user_nickname": '조셉','user_mbti':'INTP',"comment_content":'완전 노상관'},
#     {"post_id":'62ee472a7909c222c092aedb', "user_id": "mcdnkvr6", "user_nickname": '익명','user_mbti':'ISFJ',"comment_content":'근데 새우 까주는 건 안됨'},
#     {"post_id":'62ee472a7909c222c092aedb', "user_id": "5d45v6", "user_nickname": '스파르타','user_mbti':'INTP',"comment_content":'깻잎 맛있겠다'},
#     {"post_id":'62ee472a7909c222c092aedb', "user_id": "abdkrf", "user_nickname": '홍철','user_mbti':'INTP',"comment_content":'헐 댓글 진짜 놀랍다'},
#     {"post_id":'62ee472a7909c222c092aedb', "user_id": "frkkpr", "user_nickname": '가나다','user_mbti':'INTJ',"comment_content":'이걸 저렇게 생각하는 사람들이 있다니'},
#     {"post_id": '62ee472a7909c222c092aedb', "user_id": "m6595", "user_nickname": '두부', 'user_mbti': 'ESTJ',"comment_content": '다들 열정적이네'},
#     {"post_id":'',"user_id": "dftwh", "user_nickname": 'monkey','user_mbti':'ESFP',"comment_content":'이걸? 엣프피 모여'},
#     {"post_id":'', "user_id": "rbsfadff", "user_nickname": '신사동호랭이','user_mbti':'INTJ',"comment_content":'에이.... 절대 안돼'},
#     {"post_id":'', "user_id": "badf", "user_nickname": '르탄이','user_mbti':'ISFJ',"comment_content":'흠'},
#     {"post_id":'', "user_id": "daadbf", "user_nickname": '강호동','user_mbti':'INTP',"comment_content":'난 중립'},
#     {"post_id":'', "user_id": "badfbadf", "user_nickname": '김르탄','user_mbti':'ISFJ',"comment_content":'10년 친구면 가능'},
#     {"post_id":'62ee472a7909c222c092aedb', "user_id": "mvlkfm53", "user_nickname": '멍멍','user_mbti':'INTP',"comment_content":'그냥 셋이 만나지를 마'},
#     {"post_id":'', "user_id": "sbgbbs", "user_nickname": '돼냥이','user_mbti':'ISFJ',"comment_content":'난 좀 반대'},
#     {"post_id":'', "user_id": "dvsdlsdl", "user_nickname": '밥줘','user_mbti':'INTP',"comment_content":'그럼 난 찬성'},
#     {"post_id":''', "user_id": "ereabrf", "user_nickname": '으르렁','user_mbti':'ESTJ',"comment_content":'이게 된다고?'},
#     {"post_id":'', "user_id": "sdgb", "user_nickname": '밍수','user_mbti':'INTP',"comment_content":'뭐야 난 인팁이지만 공감 불가'},
#     {"post_id":'', "user_id": "adf", "user_nickname": 'ㅇㅇ','user_mbti':'ESFP',"comment_content":'나도 안돼'},
#     {"post_id":'', "user_id": "afdadfddf", "user_nickname": '공부하기싫다','user_mbti':'ESFP',"comment_content":'됨'}
#     ]


