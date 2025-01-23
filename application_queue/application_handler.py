import queue
import threading
import random

class Application:
    def __init__(self):
        self.application_queue = queue.Queue()
        self.stop_cycle = False

    def generate_request(self):
        request = random.randint(1, 100)
        self.application_queue.put(request)
        print(f"Generated request: {request}")

    def process_request(self):
        if not self.application_queue.empty():
            request = self.application_queue.get()
            print(f"Processing request: {request}")
        else:
            print("Queue is empty")
        threading.Event().wait(1)

    def stop_listener(self):
        print("To stop the cycle of requests, type 'stop', 'exit' , 0 stop\n")
        while not self.stop_cycle:
            user_input = input()
            if user_input.lower() in ["stop", "exit", "0"]:
                self.stop_cycle = True
                print("Stopping the application...")

    def run(self):
        threading.Thread(target=self.stop_listener, daemon=True).start()
        while not self.stop_cycle:
            self.generate_request()
            self.process_request()

        print("Application stopped.")

if __name__ == "__main__":
    Application().run()