import time
import threading
from datetime import datetime, timedelta
from typing import Optional, Callable

class TimerLogic:
    def __init__(self):
        self.start_timer = None
        self.minutes: int = 0
        self.is_running: bool = False
        self.timer_thread = None
        self.callback = None

    def timer_start(self, minutes: int, callback=None):
        self.start_timer = datetime.now()
        self.minutes = minutes
        self.is_running = True
        self.callback = callback
        #starts the timer in a different thread
        self.timer_thread = threading.Thread(target=self._run_timer)
        self.timer_thread.start()
        return {"status": "started", "duration": minutes}

    def _run_timer(self):
        #The internal timer runner
        time.sleep(self.minutes * 60)
        if self.is_running:
            self.is_running = False
            if self.callback:
                self.callback()

    def get_remaining_time(self) -> dict: 
        # The remaining timer 
        if not self.is_running or not hasattr(self, 'start_timer'):
            return {"minutes": 0, "seconds": 0}
        elapsed = (datetime.now() - self.start_timer).total_seconds()
        total_seconds = self.minutes * 60
        remaining_seconds = max(0, int(total_seconds - elapsed))
        minutes = remaining_seconds // 60
        seconds = remaining_seconds % 60
        return {"minutes": minutes, "seconds": seconds}
    
    def stop_timer(self):
        #stops the timer
        self.is_running = False
        return {"status": "stopped"}
    