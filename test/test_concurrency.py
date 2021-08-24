import helper_functions as hf
from threading import Thread

def test_multiple_requests():
    # if the resulting arrays of hashes contain NUM_THREADS
    # then all requests were successful
    
    NUM_THREADS = 250
    threads = []
    job_ids = []
    base64_hashes = []

    for i in range(NUM_THREADS):
        t = hf.ThreadWithReturnValue(target=hf.api_post_random_password, args=())
        t.daemon = True
        threads.append(t)

    for i in range(NUM_THREADS):
        threads[i].start()

    for i in range(NUM_THREADS):
        job_ids.append(threads[i].join().text)

    for i in range(NUM_THREADS):
        base64_hashes.append(hf.api_get_hash(job_ids[i]).text)
    
    assert len(job_ids) == NUM_THREADS
    assert len(base64_hashes) == NUM_THREADS
