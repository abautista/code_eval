#!/usr/bin/env python

import sys


groups = {}
users = {}


def get_suggestions(user, friends):
    friends_number = len(friends)
    suggestions = []

    for group_name, members in groups.items():
        friends_in_group = 0
        for friend in friends:
            if friend in members:
                friends_in_group += 1
        if not user in members and float(friends_in_group) >= float(friends_number) / 2:
            suggestions.append(group_name)
    suggestions.sort()
    return suggestions


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as users_info:
        for user_info in users_info:
            user_name, user_friends, user_groups = user_info.replace("\n", "").split(':')
            user_friends = user_friends.split(",")
            user_groups = user_groups.split(",")

            users[user_name] = user_friends
            for group_name in user_groups:
                groups.setdefault(group_name, []).append(user_name)

    suggestions = {}
    users_with_suggestions = []
    for user, friends in users.items():
        user_suggestions = get_suggestions(user, friends)
        if user_suggestions:
            users_with_suggestions.append(user)
            suggestions[user] = user_suggestions

    users_with_suggestions.sort()
    for user in users_with_suggestions:
        print "%s:%s" % (user, ','.join(suggestions[user]))
