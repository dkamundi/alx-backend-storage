#!/usr/bin/env python3
"""
Contains the class definition for redis cache
"""
import redis
import uuid
from typing import Union
from functools import wraps


class Cache:
    def __init__(self):
        self.redis = redis.Redis()
        self._redis.flushdb()

    def call_history(method: Callable):
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"

        # Normalize and store input arguments
        input_args = [str(arg) for arg in args]
        self._redis.rpush(input_key, *input_args)

        # Execute the original function to retrieve the output
        result = method(self, *args, **kwargs)

        # Normalize and store the output
        self._redis.rpush(output_key, str(result))
        return result
    return wrapper

    class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def get(self, key: str, fn: Callable = None):
        if self._redis.exists(key):
            data = self._redis.get(key)
            if fn is not None:
                data = fn(data)
            return data
        else:
            return None
    def store(self, data: Union[str, bytes, int, float]) -> str:
        # Generate a random key using uuid
        key = str(uuid.uuid4())
        self.redis.set(key, data)
        return key
    
    def replay(method: Callable):
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"
    
        input_history = cache._redis.lrange(input_key, 0, -1)
        output_history = cache._redis.lrange(output_key, 0, -1)
    
        print(f"{method.__qualname__} was called {len(input_history)} times:")
    
        for input_args, output in zip(input_history, output_history):
            input_args = eval(input_args.decode("utf-8"))  # Convert the input arguments back to a tuple
            print(f"{method.__qualname__}{input_args} -> {output.decode('utf-8')}")

    def get_str(self, key: str):
        return self.get(key, fn=lambda x: x.decode("utf-8"))

    def get_int(self, key: str):
        return self.get(key, fn=lambda x: int(x))

