from enum import Enum
from dataclasses import dataclass


class JobState(Enum):
    RUNNING = 'RUNNING'
    STOPPED = 'STOPPED'
    DONE = 'DONE'


@dataclass
class Job:
    jid: int
    pid: int
    pgid: int
    state: JobState
    cmdline: str


_job_list = []
