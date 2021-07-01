import pickle
import os


def test():
    path = 'mydata.pickle'
    with open(path, "wb") as saved_data:
        pickle.dump([1, 2, 3, "data"], saved_data)

    with open(path, 'rb') as restored_data:
        lst = pickle.load(restored_data)
        assert lst == [1, 2, 3, "data"]
    os.remove(path)


def test_dict():
    entry = {}
    entry['title'] = "Dive into history, 2009 edition"
    entry['article_link'] = 'http://diveintomark.org/archives/2009/03/27/dive-into-history-2009-edition'
    entry['comments_link'] = None
    entry['internal_id'] = b'\xDE\xD5\xB4\xF8'
    entry['tags'] = ('diveintopython', 'docbook', 'html')
    entry['published'] = True
    import time
    entry['published_date'] = time.strptime('Fri Mar 27 22:20:42 2009')
    import pickle
    with open('entry.pickle', 'wb') as f:
        pickle.dump(entry, f)


def test_read():
    with open('entry.pickle', 'rb') as f:
        entry = pickle.load(f)
        print(entry)
