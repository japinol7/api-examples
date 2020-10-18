from app.app import animes, ANIME_NOT_FOUND_MSG_ERROR


ANIMES_MAX_ID_BEFORE_TESTS = 63


def test_list_anime_ids_response(app_client_get_root):
    response = app_client_get_root
    assert response.status_code == 200


def test_list_anime_ids_count(app_client_get_root):
    response = app_client_get_root
    json_resp = response.json()
    animes_count = len(animes)
    assert len(json_resp) == animes_count


def test_list_anime_ids_expected(app_client_get_root):
    response = app_client_get_root
    json_resp = response.json()
    expected = [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36,
                39, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]
    assert json_resp == expected


def test_list_animes_response(app_client_get_all):
    response = app_client_get_all
    assert response.status_code == 200


def test_list_animes_count(app_client_get_all):
    response = app_client_get_all
    json_resp = response.json()
    animes_count = len(animes)
    assert len(json_resp) == animes_count


def test_list_animes_first_anime(app_client_get_all):
    response = app_client_get_all
    json_resp = response.json()
    expected = {'id': 12,
                'title': 'Detective Conan',
                'year': 1996,
                'episodes': 0,
                'status': 'CURRENTLY',
                'type': 'TV',
                'animeSeason': {'season': 'WINTER', 'year': 1996},
                'picture': 'https://cdn.myanimelist.net/images/anime/7/75199.jpg',
                'sources': ['https://anidb.net/anime/266', 'https://anilist.co/anime/235', 'https://kitsu.io/anime/210', 'https://myanimelist.net/anime/235', 'https://notify.moe/anime/lWnhcKiig']
                }
    assert json_resp[0] == expected


def test_list_animes_last_anime(app_client_get_all, app_client_get_last_expected):
    response = app_client_get_all
    json_resp = response.json()
    assert json_resp[-1] == app_client_get_last_expected


def test_create_anime_count(animes_count_before_tests, app_client_post):
    response = app_client_post
    assert response.status_code == 201
    assert len(animes) == animes_count_before_tests + 1


def test_get_anime(app_client_get, app_client_get_last_expected):
    response = app_client_get(ANIMES_MAX_ID_BEFORE_TESTS)
    assert response.status_code == 200
    assert response.json() == app_client_get_last_expected


def test_get_anime_not_found(app_client_get):
    response = app_client_get(111111)
    assert response.status_code == 404
    assert response.json() == {'error': ANIME_NOT_FOUND_MSG_ERROR}


def test_create_anime_expected(app_client_post, client_test):
    response = app_client_post
    expected = {
            'id': ANIMES_MAX_ID_BEFORE_TESTS + 1,
            'title': 'Fake Detective Conan',
            'year': 1995,
            'episodes': 12,
            'status': 'CURRENTLY',
            'type': 'TV',
            'animeSeason': {'season': 'fake_season', 'year': 1995},
            'picture': 'fake_picture',
            'sources': ['fake_source_01', 'fake_source_02']
            }
    assert response.json() == expected

    response = client_test.get(f'/{ANIMES_MAX_ID_BEFORE_TESTS + 1}/')
    assert response.json() == expected


def test_create_anime_expected_second(app_client_post_second, client_test):
    response = app_client_post_second
    expected = {
            'id': ANIMES_MAX_ID_BEFORE_TESTS + 2,
            'title': 'Fake 2 Detective Conan',
            'year': 1999,
            'episodes': 24,
            'status': 'CURRENTLY',
            'type': 'TV',
            'animeSeason': {'season': 'fake_season', 'year': 1999},
            'picture': 'fake_2_picture',
            'sources': ['fake_2_source_01', 'fake_2_source_02']
            }
    assert response.json() == expected

    response = client_test.get(f'/{ANIMES_MAX_ID_BEFORE_TESTS + 2}/')
    assert response.json() == expected
