Если в блоке кода:

```python
class EventStore:
    def __init__(self):
        self._events: List[Event] = []
        self._subscribers: List[Callable[[Event], None]] = []
        self._lock = threading.RLock()
```

`threading.RLock()` заменить на `threading.Lock()`, то при запуске программы образуется дедлок потому что один поток программы будет пытаться захватить lock дважды, а `threading.Lock()` этого не будет позволять.
Технически это будет происходить на уровне метода `append_events()` при попытке чтения из `EventStore`
