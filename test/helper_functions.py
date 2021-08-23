import requests, base64, random, string

def build_base_url(host = "http://localhost", port=8000):
    return host + ":" + str(port) + ""

base_url = build_base_url() # => http://localhost:8000/

def api_post_password(password: str):
    # headers = {}
    data = '{"password":"{password}}"}'
    return requests.post(f"{base_url}/hash", data=data)

def api_get_hash(job_id: int): 
    return requests.get(f"{base_url}/hash/{str(job_id)}")

def api_get_stats():
    return requests.get(f"{base_url}/stats")

def api_post_shutdown():
    data = 'shutdown'
    return requests.post(f"{base_url}/hash", data=data)

def decode_base64_hash(base64_hash :str):
    decoded_bytes = base64.b64decode(base64_hash)
    decoded_str = str(decoded_bytes, "utf-8")
    return decoded_str

def random_string_generator(str_size):
    return ''.join(random.choice(string.ascii_letters) for x in range(str_size))
