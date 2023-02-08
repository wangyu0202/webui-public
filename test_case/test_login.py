import pytest
from test_data import login_data
from common.handle_log import logs


class TestLogin:

    @pytest.mark.parametrize("case", login_data.login_data_is_pass)
    def test_login_pass(self, login_fixture, case):
        login_page, index_page = login_fixture
        login_page.login(case["phone"], case["pwd"])
        res = index_page.is_login()
        try:
            assert res
        except AssertionError as e:
            logs.error("用例--{}--执行失败".format(case["title"]))
            logs.exception(e)
            raise e
        else:
            logs.info("用例--{}--执行通过".format(case["title"]))
            index_page.login_quit()

    @pytest.mark.parametrize("case", login_data.login_data_is_null)
    def test_login_data_null(self, login_fixture, case):
        login_page, index_page = login_fixture
        login_page.login(case["phone"], case["pwd"])
        res = login_page.get_page_error_info()

        try:
            assert res == case["expected"]
        except AssertionError as e:
            logs.error("用例--{}--执行失败".format(case["title"]))
            logs.exception(e)
            raise e
        else:
            logs.info("用例--{}--执行通过".format(case["title"]))

    @pytest.mark.parametrize("case", login_data.login_data_is_error)
    def test_login_toast_error(self, login_fixture, case):
        login_page, index_page = login_fixture
        login_page.login(case["phone"], case["pwd"])
        res = login_page.get_toast_error_info()
        try:
            assert res == case["expected"]
        except AssertionError as e:
            logs.error("用例--{}--执行失败".format(case["title"]))
            logs.exception(e)
            raise e
        else:
            logs.info("用例--{}--执行通过".format(case["title"]))
