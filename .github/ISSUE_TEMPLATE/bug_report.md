Errors from bravenewcommune.py

File "/home/splinter/Brave_New_Commune2/bravenewcommune2.py", line 1337, in <module>  File "/home/splinter/Brave_New_Commune2/bravenewcommune2.py", line 1333, in main  File "/home/splinter/Brave_New_Commune2/bravenewcommune2.py", line 1191, in run  File "/home/splinter/Brave_New_Commune2/bravenewcommune2.py", line 982, in _write_diary  File "/home/splinter/Brave_New_Commune2/bravenewcommune2.py", line 659, in _append_jsonl  File "/usr/lib/python3.13/pathlib/_local.py", line 539, in open    return io.open(self, mode, buffering, encoding, errors, newline)           ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ FileNotFoundError: [Errno 2] No such file or directory: '/home/splinter/Brave_New_Commune2/data/diary/mira/day_001.jsonl''



I fixed this in bravenewcommune2.py

