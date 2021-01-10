import requests
import sqlite3


def get_jobs(page):
    url = 'https://api.github.com/repos/awesome-jobs/vietnam/issues?page=2&q=is%3Aissue+is%3Aopen'.format(page)
    resp = requests.get(url)
    data = resp.json()
    return data


def main():
    page = 1
    my_id = 1
    while True:
        jobs = get_jobs(page)
        if jobs != []:
            for job in jobs:
                conn = sqlite3.connect("db.sqlite3")
                c = conn.cursor()
                title = job['title']
                detail = job['body']
                c.execute('INSERT INTO awesomejob_awesome_job VALUES (?, ?, ?)', (my_id, title, detail))
                conn.commit()
                conn.close()
                my_id += 1
        else:
            break
        page += 1


if __name__ == "__main__":
    main()
