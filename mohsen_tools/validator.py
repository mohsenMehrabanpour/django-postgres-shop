from user.models import User
import re

def signup_validator(post):
    """
    custom validator , give request.post , if validate successfully its return
    ok(as string) else its return a list of errors

    """
    is_valid = True
    messages = []

    user_exist = User.objects.filter(username=post['username']).exists()

    if user_exist:
        is_valid = False
        messages.append('this username already exists')

    if len(post['password']) < 8 :
        is_valid = False
        messages.append('password should be at least 8 character')

    if post['phonenumber'][0:2] != '09' or len(post['phonenumber']) != 11:
        is_valid = False
        messages.append('your phone number is not valid')

    if len(post['address']) < 5:
        is_valid = False
        messages.append('your address is invalid')

    if len(post['firstname']) < 1 or len(post['lastname']) < 1:
        is_valid = False
        messages.append('your name is required')

    regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
    if not re.search(regex,post['email']):
        is_valid = False
        messages.append('your email address is invalid')

    if is_valid:
        return 'ok'
    return messages