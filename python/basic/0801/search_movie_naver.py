from pprint import pprint
import requests
from pprint import pprint
from navermovie import NaverMovie

def movies_title():
    '''
    영화 제목 리스틀를 출력하는 함수
    '''
    client_id = '--'
    client_secret = '--'

    n_movie = NaverMovie(client_id, client_secret)
    title_list = n_movie.get_title_list('해리포터')


    return title_list

def movies_released():
    '''
    영화 개봉일 순으로 딕셔너리를 출력하는 함수
    '''
    client_id = '--'
    client_secret = '--'

    n_movie = NaverMovie(client_id, client_secret)
    movies = n_movie.get_movie_released('해리포터')

    return movies


if __name__ == '__main__':
    print(movies_title())
    print(movies_released())