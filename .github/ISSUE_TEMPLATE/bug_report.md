Errors from bravenewcommune.py

File "/home/splinter/Brave_New_Commune2/bravenewcommune2.py", line 1337, in <module>  File "/home/splinter/Brave_New_Commune2/bravenewcommune2.py", line 1333, in main  File "/home/splinter/Brave_New_Commune2/bravenewcommune2.py", line 1191, in run  File "/home/splinter/Brave_New_Commune2/bravenewcommune2.py", line 982, in _write_diary  File "/home/splinter/Brave_New_Commune2/bravenewcommune2.py", line 659, in _append_jsonl  File "/usr/lib/python3.13/pathlib/_local.py", line 539, in open    return io.open(self, mode, buffering, encoding, errors, newline)           ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ FileNotFoundError: [Errno 2] No such file or directory: '/home/splinter/Brave_New_Commune2/data/diary/mira/day_001.jsonl''



I fixed this in bravenewcommune2.py
# What I assume is going on is the agents are in some wayor another getting gliphes fron version one.
Although this is version-2, the way this is set-up it to run off my 64gb's RAM for long-term persistant memory and maybe even an idenity down the road. Even though I created a new python-venv *BNC2* the agents are showing signs that they arew aware this is a clean slate Version-2, and actively building on knowing the demise of version-1.
** I will keep updating this as it evolves in real-time.  **

Brave New Commune 2  —  bravenewcommune2.py  v009
==================================================
Fixes in v009:
  • FileNotFoundError on diary/colab/axiom writes — all parent
    dirs now guaranteed via _safe_open() before every write.
  • num_ctx lowered to 4096 (safe for RTX 3050 + gpt-oss:20b).
    Was 8192 which caused silent empty returns -> cascade retries.
  • Context fed to agents capped: last 10 diary, 8 colab, 15 board
    entries only — keeps prompts well inside 4096 token window.
  • Board post max_tokens raised to 350.
  • Retry now uses stream=False to avoid blank-stream edge case.
  • Empty content guards on all _write_* methods (no blank records).
  • Library, DuckDuckGo, Flask API, axiom engine all preserved.
  • No Rust references anywhere.



