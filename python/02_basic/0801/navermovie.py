import requests
from pprint import pprint


class NaverMovie:
    def __init__(self, client_id, client_secret) -> None:
        self.client_id = client_id
        self.client_secret = client_secret

    def get_search_data(self, query: str):
        '''
        원하는 검색 결과의 데이터를 그대로 반환하는 메서드
        '''
        base_url = f'https://openapi.naver.com/v1/search/movie.json?query={query}'
        head = {
        'X-Naver-Client-Id': f'{self.client_id}',
        'X-Naver-Client-Secret': f'{self.client_secret}'
        }
        data = requests.get(base_url, headers = head).json()
        return data

    def get_title_list(self, query: str):
        '''
        검색 결과의 영화 제목 리스트를 반환하는 메서드
        '''
        result = self.get_search_data(query)
        data = result.get('items')
        title_list = []
        for movie in data:
            title_list.append(movie['title'])

        return title_list

    def get_movie_released(self, query: str):
        result = self.get_search_data(query)
        data = result.get('items')
        title_released = []
        for movie in data:
            title_released.append([movie['title'], movie['pubDate']])
        title_released.sort(key=lambda x:x[1])
        
        return dict(title_released)