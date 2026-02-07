import pytest
import requests


class TestAPI:
    auth_token = ("Bearer FsUSOrUEjC0p8vaY66q85KtfKW6-"
                  "X0OrgoUhjWJ1jN5KjFScsjY1YiiDnT-L0TeB")

    id_project = None

    base_url = 'https://ru.yougile.com'
    project_name = "AutoGenProject"

    def _check_status_code(self, response, expected_codes):
        assert response.status_code in expected_codes, (
            f"Ожидались коды {expected_codes}, получен {response.status_code}"
        )

    @pytest.mark.order(1)
    def test_post(self):
        data = {
            "title": str(self.project_name),
            "users": {}
        }

        # POST запрос на создание проекта
        r = requests.post(
            self.base_url + '/api-v2/projects',
            headers={"Authorization": self.auth_token},
            data=data
        )

        self._check_status_code(r, [200, 201])

        self.__class__.id_project = r.json()["id"]

    @pytest.mark.order(2)
    def test_post_negative(self):
        # POST запрос без токена авторизации
        r = requests.post(
            self.base_url + '/api-v2/projects',
            headers={"Authorization": ""},
            data={"title": "InvalidProject"}
        )
        self._check_status_code(r, [401])

    @pytest.mark.order(3)
    def test_put(self):
        assert self.__class__.id_project is not None, "ID проекта не получен!"

        data = {"title": self.project_name + "_edited"}

        # PUT запрос на изменение проекта
        r = requests.put(
            self.base_url + '/api-v2/projects/' + self.__class__.id_project,
            headers={"Authorization": self.auth_token},
            data=data
        )

        self._check_status_code(r, [200, 201])

    @pytest.mark.order(4)
    def test_put_negative(self):
        # PUT запрос с несуществующим ID
        r = requests.put(
            self.base_url + '/api-v2/projects/invalid_project_id',
            headers={"Authorization": self.auth_token},
            data={"title": "InvalidProject"}
        )
        self._check_status_code(r, [404])

    @pytest.mark.order(5)
    def test_get(self):
        assert self.__class__.id_project is not None, "ID проекта не получен!"

        # GET запрос на получение информации о проекте
        r = requests.get(
            self.base_url + '/api-v2/projects/' + self.__class__.id_project,
            headers={"Authorization": self.auth_token},
        )

        self._check_status_code(r, [200, 201])

    @pytest.mark.order(6)
    def test_get_negative(self):
        # GET запрос с некорректным форматом ID
        r = requests.get(
            self.base_url + '/api-v2/projects/123-invalid-id-456',
            headers={"Authorization": self.auth_token},
        )
        self._check_status_code(r, [404])


if __name__ == '__main__':
    pytest.main()
