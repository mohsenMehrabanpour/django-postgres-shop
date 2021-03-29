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

    if len(post['password']) < 8:
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
    if not re.search(regex, post['email']):
        is_valid = False
        messages.append('your email address is invalid')

    if is_valid:
        return 'ok'
    return messages


def product_text_validator(post):
    """
    the result of this function is a dict of not empty product text fields
    if there was no thing valid it will return False(bool) .
    you should give request.POST to this function

    """
    result = dict()

    if len(post['title']) > 0:
        result['title'] = post['title']
    else:
        return False
    if len(post['price']) > 0:
        result['price'] = int(post['price'])
    else:
        return False
    if len(post['description']) > 0:
        result['description'] = post['description']

    if len(result) > 0:
        return result
    return False


def product_image_validator(img):
    """
    this function check image , if size < 3MB and file type = image it will return True (bool)

    """
    valid = True
    img_size_mb = int(img.size) / 1048576
    file_type = str(img.content_type)[:5]
    if img_size_mb > 3 :
        valid = False
    if file_type != 'image':
        valid = False
    return valid
