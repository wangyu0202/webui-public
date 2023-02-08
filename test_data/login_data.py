login_data_is_pass = [
    {"title": "正常登录", "phone": "1333333", "pwd": "aaa"}
]

login_data_is_null = [
    {"title": "密码为空", "phone": "1333333", "pwd": "", "expected": "请输入密码"},
    {"title": "手机号为空", "phone": "", "pwd": "aaa", "expected": "请输入手机号"}
]

login_data_is_error = [
    {"title": "账号未注册", "phone": "13333331", "pwd": "123", "expected": "此账号没有经过授权，请联系管理员!"},
    {"title": "密码错误", "phone": "1333333", "pwd": "aaa1", "expected": "帐号或密码错误!"}
]
