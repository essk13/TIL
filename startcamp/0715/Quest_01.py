# SW_Cp_2주차_04
# Mission : list & dict

movie = {
    'movieInfo': {
        'movieNm': '광해, 왕이 된 남자',
        'movieNmEn': 'Masquerade',
        'showTm': '131',
        'prdtYear': '2012',
        'openDt': '20120913',
        'typeNm': '장편',
        'nations': [{'nationNm': '한국'}],
        'genres': [{'genreNm': '사극'}, {'genreNm': '드라마'}],
        'directors': [{'peopleNm': '추창민', 'peopleNmEn': 'CHOO Chang-min'}],
        'actors': [
            {'peopleNm': '이병헌', 'peopleNmEn': 'LEE Byung-hun', 'cast': '광해/하선'},
            {'peopleNm': '류승룡', 'peopleNmEn': 'RYU Seung-ryong', 'cast': '허균'},
            {'peopleNm': '한효주', 'peopleNmEn': 'HAN Hyo-joo', 'cast': '중전'},
        ],
    }
}

# 1. 영화의 제목을 출력하시오.
movie_info = movie['movieInfo']
# movie_name = movie_info['movieNm']
# print(movie_name)

# or

print((movie['movieInfo'])['movieNm'])

# 2. 다음 movie의 감독의 영어 이름을 출력하시오.
# movie_DrNm = movie_info['directors']
# movie_DrNm2 = movie_DrNm[0]
# movie_DrNm_En = movie_DrNm2['peopleNmEn']
# print(movie_DrNm_En)

#or

print((((movie['movieInfo'])['directors'])[0])['peopleNmEn'])

# 3. 다음 movie의 배우의 인원을 출력하시오.
# movie_act = movie_info['actors']
# movie_acts = len(movie_act)
# print(movie_acts)

# or

print(len((movie['movieInfo'])['actors']))