def create_message(message_type='warning',*args):
    """
    messages types can be : error, warning, success

    """
    if message_type != 'error' and message_type != 'warning' and message_type != 'success':
        message_type = 'warning'

    messages = {'messsage_type':message_type}
    messages['messages'] = args
    return messages