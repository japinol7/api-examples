from app.app import animes


def test_list_anime_ids_response(app_client_connection_root):
    response = app_client_connection_root
    assert response.status_code == 200


def test_list_anime_ids_count(app_client_connection_root):
    response = app_client_connection_root
    json_resp = response.json()
    animes_count = len(animes)
    assert len(json_resp) == animes_count


def test_list_anime_ids_expected(app_client_connection_root):
    response = app_client_connection_root
    json_resp = response.json()
    expected = [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36,
                39, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]
    assert json_resp == expected


def test_list_animes_count(app_client_root_connection_all):
    response = app_client_root_connection_all
    assert response.status_code == 200

    json_resp = response.json()
    animes_count = len(animes)
    assert len(json_resp) == animes_count


def test_list_animes_count(app_client_root_connection_all):
    response = app_client_root_connection_all
    json_resp = response.json()
    animes_count = len(animes)
    assert len(json_resp) == animes_count


def test_list_animes_first_anime(app_client_root_connection_all):
    response = app_client_root_connection_all
    json_resp = response.json()
    expected = {'id': 12,
                'title': 'Detective Conan',
                'year': 1996,
                'episodes': 0,
                'status': 'CURRENTLY', 'type': 'TV',
                'animeSeason': {'season': 'WINTER', 'year': 1996},
                'picture': 'https://cdn.myanimelist.net/images/anime/7/75199.jpg',
                'sources': ['https://anidb.net/anime/266', 'https://anilist.co/anime/235', 'https://kitsu.io/anime/210', 'https://myanimelist.net/anime/235', 'https://notify.moe/anime/lWnhcKiig']
                }
    assert json_resp[0] == expected


def test_list_animes_first_anime(app_client_root_connection_all):
    response = app_client_root_connection_all
    json_resp = response.json()
    expected = {'id': 63,
                'title': 'Detective Conan Movie 4: Captured In her Eyes',
                'year': 2000, 'episodes': 1,
                'status': 'UNKNOWN', 'type': 'Movie',
                'animeSeason': {'season': 'UNDEFINED', 'year': 2000},
                'picture': 'https://anime-planet.com/images/anime/covers/detective-conan-movie-4-captured-in-her-eyes-1489.jpg',
                'sources': ['https://anime-planet.com/anime/detective-conan-movie-4-captured-in-her-eyes']}
    assert json_resp[-1] == expected
