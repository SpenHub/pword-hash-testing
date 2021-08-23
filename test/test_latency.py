from time import perf_counter_ns
import helper_functions as hf

# Setting thresholds
# job_id time shouldn't exceed half second
# hash time shouldn't exceed 5 sec + 10%
DESIRED_JOB_TIME = 500000000   # 0.5 seconds
DESIRED_HASH_TIME = 5500000000 # 5.5 seconds

def test_job_id_return_time():
    start = perf_counter_ns()
    hf.api_post_password(hf.random_string_generator(10))
    end = perf_counter_ns()
    time = end - start

    assert (time) < DESIRED_JOB_TIME

def test_hash_return_time():
    start = perf_counter_ns()
    hf.api_get_hash(
            hf.api_post_password(
                hf.random_string_generator(10)).text).text
    end = perf_counter_ns()
    time = end - start

    assert (time) < DESIRED_HASH_TIME