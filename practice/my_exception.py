def sign_up():
    '''회원가입 함수'''
    
try:
    sign_up()
except BadUserName:
    print("이름으로 사용할 수 없는 입력입니다")
except PasswordNotMatched:
    print("입력한....")
    