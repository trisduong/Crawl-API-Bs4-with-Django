import requests
import sqlite3


def get_jobs(page, token):
    url = 'https://api.github.com/repos/awesome-jobs/vietnam/issues?page={}&q=is%3Aissue+is%3Aopen?access_token={}'.format(page, token)
    with open('token.txt') as f:
        token = f.read()
    resp = requests.get(url)
    data = resp.json()
    return data


def main():
    id = 1
    page = 1
    conn = sqlite3.connect("db.sqlite3")
    c = conn.cursor()
    while True:
        jobs = get_jobs(page, token)
        if jobs != '':
            for job in jobs:
                title = job['title']
                detail = job['body']
                c.execute('INSERT INTO jobs VALUES (?, ?, ?)', (id, title, detail))
                id += 1
        else:
            break
        page += 1
    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()
