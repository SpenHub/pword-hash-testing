import helper_functions as hf
import hashlib as hl
import base64
from threading import Thread

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

def test_sha512():
    # Compute SHA512, base64 encode, and compare
    # with "hash/<job_id>" response
    h = hl.new("sha512")
    h.update(b"password")
    sha512_hash = h.hexdigest()

    base64_encoded_hash = base64.b64encode(sha512_hash.encode("ascii")) 
    print(base64_encoded_hash)

    api_base64_encoded_hash = hf.api_get_hash(
            hf.api_post_password("password").text).text

    assert api_base64_encoded_hash in str(base64_encoded_hash)

def test_stats_num_jobs():
    # if the resulting arrays of hashes contain NUM_THREADS
    # then all requests were successful
    init_stats_num_jobs = int(hf.api_get_stats_requests())

    NUM_THREADS = 123
    threads = []
    job_ids = []
    base64_hashes = []

    for i in range(NUM_THREADS):
        t = ThreadWithReturnValue(target=hf.api_post_random_password, args=())
        t.daemon = True
        threads.append(t)

    for i in range(NUM_THREADS):
        threads[i].start()

    for i in range(NUM_THREADS):
        job_ids.append(threads[i].join().text)

    for i in range(NUM_THREADS):
        base64_hashes.append(hf.api_get_hash(job_ids[i]).text)

    final_stats_num_jobs = int(hf.api_get_stats_requests())

    assert init_stats_num_jobs + NUM_THREADS == final_stats_num_jobs


    
test_stats_num_jobs()