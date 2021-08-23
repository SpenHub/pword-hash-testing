import threading
import helper_functions as hf

def write_to_file(unused_param: str):
    filename = hf.random_string_generator(2)
    content = hf.random_string_generator(10)
    print(f"Filename: {filename}\nContent: {content}")
    f = open(f"{filename}.txt", "a")
    f.write(content)
    f.close()
    
NUM_THREADS = 2
threads = []

for i in range(NUM_THREADS):
    t = threading.Thread(target=write_to_file, args=("beep",))
    t.daemon = True
    threads.append(t)

for i in range(NUM_THREADS):
    threads[i].start()

for i in range(NUM_THREADS):
    threads[i].join()

print("done")