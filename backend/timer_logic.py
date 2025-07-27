import time
import threading
from datetime import datetime

class TimerLogic:
    def __init__(self):
        self.start_time = None
        self.duration_minutes = 0
        self.is_running = False
        self.timer_thread = None

    def start(self, minutes: int):
        self.start_time = datetime.now()
        self.duration_minutes = minutes
        self.is_running = True
        self.timer_thread = threading.Thread(target=self._run_timer)
        self.timer_thread.start()

    def _run_timer(self):
        time.sleep(self.duration_minutes * 60)
        if self.is_running:
            self.is_running = False

    def get_remaining_time(self) -> dict:
        if not self.is_running or not self.start_time:
            return {"minutes": 0, "seconds": 0}
        
        elapsed = (datetime.now() - self.start_time).total_seconds()
        total_seconds = self.duration_minutes * 60
        remaining_seconds = max(0, int(total_seconds - elapsed))
        
        if remaining_seconds == 0:
            self.is_running = False
        
        return {
            "minutes": remaining_seconds // 60,
            "seconds": remaining_seconds % 60
        }
    
    def stop(self):
        self.is_running = False
    