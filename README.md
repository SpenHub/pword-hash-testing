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
|---------|-----|
|Test Case Here|✍️|:heavy_check_mark:|

## Concurrency
|Test Case| 🤖 Automated / ✍️ Manual|Pass?|
|---------|-----|
|Test Case Here|✍️|:heavy_check_mark:|

## Data-Validity
|Test Case| 🤖 Automated / ✍️ Manual|Pass?|
|---------|-----|
|Test Case Here|✍️|:heavy_check_mark:|  

## Timing/ Latency
|Test Case| 🤖 Automated / ✍️ Manual|Pass?|
|---------|-----|
|Test Case Here|✍️|:heavy_check_mark:|

### One-offs
|Test Case| 🤖 Automated / ✍️ Manual|Pass?|
|---------|-----|
|Test Case Here|✍️|:heavy_check_mark:|



# Python Test Info
- I hate showing my bad "side" but if it wasn't evident, this is my first project using Python, please excuse any mistakes that aren't "pythonic" e.g. structure. 
- My test-runner is `pytest` and I've implemented test-cases to the best of abilities. 
    - I felt that for the simplicity of some of these tests, implementing fixtures would've added more complexity. 
- My testing efforst were done with the MacOS binary ( `broken-hashserve_darwin` on `PORT: 8000`)
- Required package not found in stdlib was `pytest`. 
    - I used a virtualenv found in `hasher/` that can be activated with a POSIX shell by running: `source hasher/bin/activate`
    - I attempted to `pip freeze` `pytest` and it's requirements into `requirements.txt`