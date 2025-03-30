import time
import codecs
from multiprocessing import Queue, Process
import os


def process_a(input_q, to_b_q):
    while True:
        msg, sent_time = input_q.get()
        if msg == "exit":
            to_b_q.put(("exit", sent_time))
            break
        msg = msg.lower()
        time.sleep(5)
        to_b_q.put((msg, sent_time))


def process_b(from_a_q, to_main_q):
    while True:
        msg, sent_time = from_a_q.get()
        if msg == "exit":
            break
        encoded = codecs.encode(msg, "rot_13")
        to_main_q.put(encoded)
        duration = time.time() - sent_time
        with open(os.getcwd() + "/artifacts/artifacts_queu.txt", "a", encoding="utf-8") as file:
            file.write(f"Decoded message: {msg}\n")
            file.write(f"Encoded message: {encoded}\n")
            file.write(f"Time processed: {duration:.4f}s\n\n")
        print(encoded)


if __name__ == "__main__":
    q_to_a = Queue()
    q_to_b = Queue()
    q_to_main = Queue()

    a = Process(target=process_a, args=(q_to_a, q_to_b))
    b = Process(target=process_b, args=(q_to_b, q_to_main))

    a.start()
    b.start()

    print("Enter a message")
    while True:
        message = input()
        sent_time = time.time()
        q_to_a.put((message, sent_time))
        if message == "exit":
            break

    a.join()
    b.join()
