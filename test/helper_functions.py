import requests, base64, random, string, json

def build_base_url(host = "http://localhost", port=8000):
    return host + ":" + str(port) + ""

base_url = build_base_url() # => http://localhost:8000/

def random_string_generator(str_size):
    return ''.join(random.choice(string.ascii_letters) for x in range(str_size))

def api_post_password(password: str):
    # headers = {}
    # I hate this but I don't know the pythonic way
    data1 = '{"password":"'
    data2 = '}"}'
    data = data1 + password + data2
    return requests.post(f"{base_url}/hash", data=data)

def api_post_random_password():
    return api_post_password(random_string_generator(20))

def api_get_hash(job_id: int): 
    return requests.get(f"{base_url}/hash/{str(job_id)}")

def api_get_stats():
    return json.loads(requests.get(f"{base_url}/stats").text)

def api_get_stats_requests():
    return api_get_stats()["TotalRequests"]

def api_post_shutdown():
    data = 'shutdown'
    return requests.post(f"{base_url}/hash", data=data)

def decode_base64_hash(base64_hash :str):
    decoded_bytes = base64.b64decode(base64_hash)
    decoded_str = str(decoded_bytes, "utf-8")
    return decoded_str
class ThreadWithReturnValue(Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, Verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None
    def run(self):
        # print(type(self._target))
        if self._target is not None:
            self._return = self._target(*self._args,
                                                **self._kwargs)
    def join(self, *args):
        Thread.join(self, *args)
        return self._return