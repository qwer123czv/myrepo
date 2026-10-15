# 과제 
def get_movie_audience(date, title):
    """
    주어진 날짜와 영화 제목의 관객 수를 알려준다.

    받는 것: date(날짜 문자열) - 8자리 날짜. 예: "20260824"
              title(문자열) - 영화 제목. 예: "오디세이"
    돌려주는 것: (문자열) 관객 수. 예: 12,345명
    """
    params = {"key": API_KEY, "targetDt": date}
    response = requests.get(BASE_URL, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()
    movies = data["boxOfficeResult"]["dailyBoxOfficeList"]

    for movie in movies:
        if movie["movieNm"] == title:
            return int(movie["audiCnt"])

    return f"'{title}' 은(는) {date} 순위에 없습니다."