import threading

def my_function():
    # Create a new model instance and save it
    instance = MyModel.objects.create(...)

    # The signal handler will be executed in the same thread
    print(threading.get_ident())

# Start a new thread to call my_function
thread = threading.Thread(target=my_function)
thread.start()