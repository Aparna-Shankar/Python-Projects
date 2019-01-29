class User:
    def __init__(self, name, engagement):
        self.name = name
        self.engagement_metrics = engagement
        self.score = 0

    def __repr__(self):
        return f'User : {self.name}'


def email_engaged_users(user):
    try:
        user.score =  perform_calculation(user.engagement_metrics)
    except KeyError:
        print('Incorrect values provided for the calculation function')
        # raise      # this will re-raise the exception aka will not suppress it
    else:
        if user.score > 250:
            send_engagement_notification(user) # This else block will execute only if the try block is successful


def perform_calculation(metrics):
    return metrics['clicks'] * 5 + metrics['hits'] * 2


def send_engagement_notification(user):
    print(f'Notification sent to {user}.')


user_one = User('Aparna', {'click': 45, 'hits': 22})
email_engaged_users(user_one)
