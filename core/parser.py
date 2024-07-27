import time
import forum
import configuration


def job(vocabulary, current_unix, processed_ids):
    for g in vocabulary['threads']:
        thread_create_date = int(g['thread_create_date'])
        time_diff = current_unix - thread_create_date
        thread_id = g['thread_id']
        owner_id = g['creator_user_id']
        owner_domain = g['creator_username']
        exchange = g['thread_title']
        if time_diff < 300 and thread_id not in processed_ids:
            response = {
                'thread_id': thread_id,
                'url': 'https://lolz.live/threads/{thread_id}'.format(thread_id=thread_id),
                'conv_url': 'https://lolz.live/conversations/{conversation_id}'.format(conversation_id=owner_id),
                'username': owner_domain,
                'user_url': 'https://lolz.live/users/{user_id}'.format(user_id=owner_id),
                'created': time_diff,
                'transfer_url': 'https://lolz.live/payment/balance-transfer?user_id={}&hold=1&_noRedirect=1'.format(owner_id),
                'navigation': exchange
            }
            return response