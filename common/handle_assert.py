from common.handle_log import logs


def assert_result(actual, expected, case_title):
    try:
        assert actual == expected
    except AssertionError as e:
        logs.exception(e)
        raise e