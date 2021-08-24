# JumpCloud QA Assignment:
## Assumptions:
- Endpoints supported:
	- POST: `/hash`
	- GET: `/hash`
	- GET: `/stats`
- SHA512 hashing algorithm is used.
- A job_id should be returned immedietly.
- Password-hashing can take up to 5 seconds to complete.
- Any in-progress hash-requests should complete even if shutdown signal is sent.
- Stats endpoint is accurate with # of requests, and average time per request.

# Test Plan

I wasn't quite sure how in-depth to make these tests so I tried to test all the "AC" from the prompt, and any additonal tests I thought required. My testing efforts sometimes are very brief with basic descriptions, to those with explicit steps and validation critera. Please excuse if the test-plan is either too explicit or too implicit.

## Collisions
|Test Case| 🤖 Automated / ✍️ Manual|Pass?|
|---------|--------------------------|-----|
|Send same password twice, verify different hash|🤖|:heavy_multiplication_x:|
|Send 1000s of unique passwords, verify no same hash|✍️|:heavy_check_mark:|

## Concurrency
- It appears that the active password-hashing job is killed when the shutdown-request is initiated, however this could be due to my lack of experience using threading in Python. 
|Test Case| 🤖 Automated / ✍️ Manual|Pass?|
|---------|--------------------------|-----|
|250 simultaneous requests should all resolve to valid pass|🤖|:heavy_check_mark:|
|Shutdown while password-hash is actively running|🤖|:heavy_multiplication_x:|

## Data-Validity
- Note that manual failures here could be a result of differing encoding into the sha512 algorithm.
- Any attempts made to compare the base64 decoded hash, to a known sha512 hash of `<password>` were always different with `broken-hashserve_darwin`'s hash resulting in non-ASCII characters. 

|Test Case| 🤖 Automated / ✍️ Manual|Pass?|
|---------|--------------------------|-----|
|Verify SHA512|✍️|:heavy_multiplication_x:|
|Verify SHA512 + Base64 Encode|🤖|:heavy_multiplication_x:|
|Verify stat's Number of Requests is accurate|🤖|:heavy_check_mark:|

## Timing/ Latency
- I noticed that the time to receive a job_id was consistently ~ 5 seconds, and the time to receive a hash, given a job_id was near instant. Regardless, given the prompt that's a failure. 
- I used 5.5 seconds as that's 5 seconds + 10% (potentially possible given differences in machines running the program)

|Test Case| 🤖 Automated / ✍️ Manual|Pass?|
|---------|--------------------------|-----|
|Time to receive job_id for current hash < 5 seconds|✍️|:heavy_multiplication_x:|
|Time to receive job_id for current hash < 5 seconds|🤖|:heavy_multiplication_x:|
|End-to-end time to receive a hash < 5.5 seconds |✍️|:heavy_check_mark:|
|End-to-end time to receive a hash < 5.5 seconds |🤖|:heavy_check_mark:|


# Python Test Info
- I hate showing my bad "side" but if it wasn't evident, this is my first project using Python, please excuse any mistakes that aren't "pythonic" e.g. structure. 
- My test-runner is `pytest` and I've implemented test-cases to the best of abilities. 
    - I felt that for the simplicity of some of these tests, implementing fixtures would've added more complexity. 
- My testing efforst were done with the MacOS binary ( `broken-hashserve_darwin` on `PORT: 8000`)
- Required package not found in stdlib was `pytest`. 
    - I used a virtualenv found in `hasher/` that can be activated with a POSIX shell by running: `source hasher/bin/activate`
    - I attempted to `pip freeze` `pytest` and it's requirements into `requirements.txt`
