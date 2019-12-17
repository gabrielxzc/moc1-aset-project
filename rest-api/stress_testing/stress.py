import time
import urllib.parse
import urllib.request
from multiprocessing.pool import ThreadPool


def local_request(url, cookie):
    success = False
    start_time = time.time()
    try:
        req = urllib.request.Request(url=url, method="GET")
        req.add_header("cookie", cookie)

        f = urllib.request.urlopen(req)
        response = f.read().decode('utf-8')
        if "SUCCESS" in response:
            success = True
    except Exception as e:
        print(e)
        raise e

    request_time = time.time() - start_time
    return request_time, success, cookie


def request(url, cookie):
    print("Started execution")
    rt = 0
    max = 0
    min = 1
    epochs = 500
    successes = 0
    for i in range(epochs):
        request_time, success, cookie = local_request(url, cookie)
        if success:
            successes += 1
        rt += request_time
        if request_time > max:
            max = request_time
        if request_time < min:
            min = request_time
    print(rt / epochs, "MAX", max, "MIN", min, "Success ratio", successes / epochs)


def start_async(pool, cookie):
    pool.apply_async(request, kwds={
        "url": url,
        "cookie": cookie
    })


if __name__ == '__main__':
    url = "http://localhost:5000/search?query=abc"
    req = urllib.request.Request(url=url, method="GET")

    f = urllib.request.urlopen(req)
    response = f.read().decode('utf-8')
    _cookie = f.headers.get('Set-Cookie') or ""

    pool = ThreadPool(10)

    for _ in range(10):
        start_async(pool, cookie=_cookie)

    time.sleep(10000)
    pool.close()
    pool.join()

# /download/1
# 2.009877604961395 MAX 2.0430803298950195 MIN 1
# 2.009879641532898 MAX 2.043299913406372 MIN 1
# 2.009895435333252 MAX 2.0403571128845215 MIN 1
# 2.0099112067222595 MAX 2.0524649620056152 MIN 1
# 2.0099060072898864 MAX 2.045529365539551 MIN 1
# 2.009927248477936 MAX 2.035975694656372 MIN 1
# 2.009947279453278 MAX 2.0494697093963623 MIN 1
# 2.0099572105407715 MAX 2.052496910095215 MIN 1
# 2.0099748492240908 MAX 2.0510480403900146 MIN 1
# 2.0099829845428467 MAX 2.053955316543579 MIN 1
