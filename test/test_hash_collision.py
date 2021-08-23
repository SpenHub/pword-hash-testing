import helper_functions as hf
import threading

def test_password_collision_basic(same_pass:str = "test"):
    base64_hash = hf.api_get_hash(
                        hf.api_post_password(same_pass).text).text
    base64_hash2 = hf.api_get_hash(
                        hf.api_post_password(same_pass).text).text
    # If this is a password hashing app, we should be salting our hashes
    # to prevent rainbow-table type attacks. (two people of same pass have same hash)
    assert base64_hash != base64_hash2

# def test_password_collision_rand():
#     NUM_REQUESTS = 10
#     base64_hashes = []
#     for i in range(NUM_REQUESTS):
#         base64_hashes.append(hf.api_get_hash(
#                         hf.api_post_password(hf.random_string_generator(i)).text).text)
#     # WIP
