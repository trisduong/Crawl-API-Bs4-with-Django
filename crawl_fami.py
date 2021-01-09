def main():
    import requests
    from bs4 import BeautifulSoup
    import sqlite3
    url_home = 'https://www.familug.org/search?max-results=10'
    r = requests.get(url_home)
    tree = BeautifulSoup(markup=r.text, features="lxml")
    node_home = tree.find_all(name='h3', attrs={'class': 'post-title entry-title', 'itemprop': 'name'})
    conn = sqlite3.connect("db.sqlite3")
    c = conn.cursor()
    my_id = 1
    for node in node_home:
        node = str(node)
        link = node[node.find('http'): node.find('html') + 4]
        title = node[node.find('html') + 6: node.find('</a>')]
        c.execute('INSERT INTO awesomejob_fami_post VALUES (?, ?, ?)', (my_id, title, link))
        my_id += 1
    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()
