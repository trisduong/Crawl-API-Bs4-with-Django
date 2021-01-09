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
    token = '6c4f3844137d6964fd40583b8cc20e12ebad94ef'
    page = 1
    conn = sqlite3.connect("db.sqlite3")
    c = conn.cursor()
    c.execute('CREATE TABLE jobs (title CHAR, detail CHAR)')
    while True:
        jobs = get_jobs(page, token)
        if jobs != '':
            for job in jobs:
                print(job)
                title = job['title']
                detail = job['body']
            c.execute('INSERT INTO jobs VALUES (?, ?)', (title, detail))
        else:
            break
        page += 1
    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()
