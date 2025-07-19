import json
import argparse


def load_user_data(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def analyze_user(data):
    score = 0
    reasons = []

    if data.get('default_image'):
        score += 1
        reasons.append('default profile image')

    followers = data.get('followers', 0)
    following = data.get('following', 0)
    if followers < 50:
        score += 1
        reasons.append('few followers')
    if following > followers * 10:
        score += 1
        reasons.append('following too many accounts')

    posts = data.get('posts', 0)
    if posts < 5:
        score += 1
        reasons.append('very few posts')

    last_post_days_ago = data.get('last_post_days_ago', 0)
    if last_post_days_ago > 365:
        score += 1
        reasons.append('inactive for over a year')

    return score, reasons


def main():
    parser = argparse.ArgumentParser(description='Detect potential fake accounts on X')
    parser.add_argument('data', help='Path to JSON file with user data')
    args = parser.parse_args()

    data = load_user_data(args.data)
    score, reasons = analyze_user(data)

    print(f"Fake score: {score}")
    for reason in reasons:
        print('-', reason)
    if score >= 3:
        print('>> Account is likely fake.')
    else:
        print('>> Account seems legitimate.')


if __name__ == '__main__':
    main()

