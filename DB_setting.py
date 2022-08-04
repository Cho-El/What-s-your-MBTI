import pymongo
from pymongo import MongoClient
import pymongoose
import collection
import collections

client = MongoClient('localhost', 27017)
db = client.mbti

# # 1. User 테이블
# doc1 = {'user_id':'m6595','user_pw':'1234', 'user_nickname':'두부', 'user_mbti':'ISFJ'}
#db.User.insert_one(doc1)

# ----------------------------------------

# # 2. Comment 테이블
# doc2 = {'user_id':'m6595','comment_content':'에이.... 절대 안돼'}
db.Comment.delete_many({})
db.Comment.insert_many([
    {"post_id":'1', "comment_id": "1", "user_id": "mvlkfm53", "user_nickname": '홍길동','user_mbti':'INTP',"comment_content":'쌉가능!!!!!!!!'},
    {"post_id":'1', "comment_id": "2", "user_id": "flflkg5", "user_nickname": '김철수','user_mbti':'INTJ',"comment_content":'예민함'},
    {"post_id":'1', "comment_id": "3", "user_id": "m6595", "user_nickname": '두부','user_mbti':'ESTJ',"comment_content":'이거가지고 왜 싸움'},
    {"post_id":'1', "comment_id": "4", "user_id": "ffmffl", "user_nickname": '조셉','user_mbti':'INTP',"comment_content":'완전 노상관'},
    {"post_id":'1', "comment_id": "5", "user_id": "mcdnkvr6", "user_nickname": '익명','user_mbti':'ISFJ',"comment_content":'근데 새우 까주는 건 안됨'},
    {"post_id":'1', "comment_id": "6", "user_id": "5d45v6", "user_nickname": '스파르타','user_mbti':'INTP',"comment_content":'깻잎 맛있겠다'},
    {"post_id":'1', "comment_id": "7", "user_id": "abdkrf", "user_nickname": '홍철','user_mbti':'INTP',"comment_content":'헐 댓글 진짜 놀랍다'},
    {"post_id":'1', "comment_id": "8", "user_id": "frkkpr", "user_nickname": '가나다','user_mbti':'INTJ',"comment_content":'이걸 저렇게 생각하는 사람들이 있다니'},
    {"post_id": '1', "comment_id": "3", "user_id": "m6595", "user_nickname": '두부', 'user_mbti': 'ESTJ',"comment_content": '다들 열정적이네'},
    {"post_id":'3', "comment_id": "9", "user_id": "dftwh", "user_nickname": 'monkey','user_mbti':'ESFP',"comment_content":'이걸? 엣프피 모여'},
    {"post_id":'2', "comment_id": "10", "user_id": "rbsfadff", "user_nickname": '신사동호랭이','user_mbti':'INTJ',"comment_content":'에이.... 절대 안돼'},
    {"post_id":'1', "comment_id": "11", "user_id": "badf", "user_nickname": '르탄이','user_mbti':'ISFJ',"comment_content":'흠'},
    {"post_id":'2', "comment_id": "12", "user_id": "daadbf", "user_nickname": '강호동','user_mbti':'INTP',"comment_content":'난 중립'},
    {"post_id":'1', "comment_id": "13", "user_id": "badfbadf", "user_nickname": '김르탄','user_mbti':'ISFJ',"comment_content":'10년 친구면 가능'},
    {"post_id":'4', "comment_id": "14", "user_id": "mvlkfm53", "user_nickname": '멍멍','user_mbti':'INTP',"comment_content":'그냥 셋이 만나지를 마'},
    {"post_id":'2', "comment_id": "15", "user_id": "sbgbbs", "user_nickname": '돼냥이','user_mbti':'ISFJ',"comment_content":'난 좀 반대'},
    {"post_id":'2', "comment_id": "16", "user_id": "dvsdlsdl", "user_nickname": '밥줘','user_mbti':'INTP',"comment_content":'그럼 난 찬성'},
    {"post_id":'5', "comment_id": "17", "user_id": "ereabrf", "user_nickname": '으르렁','user_mbti':'ESTJ',"comment_content":'이게 된다고?'},
    {"post_id":'3', "comment_id": "18", "user_id": "sdgb", "user_nickname": '밍수','user_mbti':'INTP',"comment_content":'뭐야 난 인팁이지만 공감 불가'},
    {"post_id":'7', "comment_id": "19", "user_id": "adf", "user_nickname": 'ㅇㅇ','user_mbti':'ESFP',"comment_content":'나도 안돼'},
    {"post_id":'4', "comment_id": "20", "user_id": "afdadfddf", "user_nickname": '공부하기싫다','user_mbti':'ESFP',"comment_content":'됨'}
    ])
# ----------------------------------------

# # 3. free_posts 테이블
db.free_posts.delete_many({})
db.free_posts.insert_many([
    {"post_id":'1', "user_id": "m_6595", "post_title": '깻잎논쟁', "post_content":'내 친구가 깻잎 떼는 것을 나의 이성친구가 도와줘도 되는가?' },
    {"post_id":'2', "user_id": "m_6595", "post_title": '롱패딩 논쟁', "post_content":'내 이성친구가 남/여사친의 롱패딩 지퍼를 올려줘도 되는가?' },
    {"post_id":'3', "user_id": "m_6595", "post_title": '"멍때리기"란?', "post_content":'멍때리기란, 아무 생각을 하지 않는 것인가? 잡생각을 하고 있는 것인가?' },
    {"post_id":'4', "user_id": "m_6595", "post_title": '"나 교통사고 났어"에 대한 대답은?', "post_content":''},
    {"post_id":'5', "user_id": "m_6595", "post_title": '영희와 철수, 누가 더 나쁜가?', "post_content":'나 도와주려다 내 과제에 커피를 쏟은 영희 vs 내 과제를 몰래 사진찍어간 철수'},
    {"post_id":'6', "user_id": "m_6595", "post_title": '시험에 떨어진 친구에게', "post_content":'가장 먼저 해줄 말은?'},
    {"post_id":'7', "user_id": "m_6595", "post_title": '"사과"하면 떠오르는 것은?', "post_content":'무엇인가?'},
    {"post_id":'8', "user_id": "m_6595", "post_title": '여행 가기 전 준비과정', "post_content":'여행 가기 전 모든 프로세스'},
    {"post_id":'9', "user_id": "m_6595", "post_title": '가끔 어떤 망상해?', "post_content":'말 그대로 어떤 망상함?'},
    ])

# ----------------------------------------

# 4. Feature 테이블
db.Feature.delete_many({})
db.Feature.insert_many([
    {"feature_mbti":'ISFJ', "like": 199, "feature_content": '자기 자신에게 엄격함'},
    {"feature_mbti":'ISFJ', "like": 199, "feature_content": '자기 자신에게 엄격함'},
    {"feature_mbti":'ISFJ', "like": 199, "feature_content": '자기 자신에게 엄격함'},
    {"feature_mbti":'ISFJ', "like": 199, "feature_content": '자기 자신에게 엄격함'},
    {"feature_mbti":'ISFJ', "like": 199, "feature_content": '자기 자신에게 엄격함'},
    {"feature_mbti":'ISFJ', "like": 199, "feature_content": '자기 자신에게 엄격함'},
    {"feature_mbti":'ISFJ', "like": 199, "feature_content": '자기 자신에게 엄격함'},
    {"feature_mbti":'ISFJ', "like": 199, "feature_content": '자기 자신에게 엄격함'},
    {"feature_mbti":'ISFJ', "like": 199, "feature_content": '자기 자신에게 엄격함'},
    {"feature_mbti":'ISFJ', "like": 199, "feature_content": '자기 자신에게 엄격함'},
    {"feature_mbti":'ISFJ', "like": 199, "feature_content": '자기 자신에게 엄격함'}
    ])