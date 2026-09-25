import sys
import subprocess

import time
from datetime import datetime

def dddh():
    # 启动子进程
    process = subprocess.Popen(
        [sys.executable, "dddh.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=1  # 行缓冲区
    )

    # 向子脚本写入第一行输入（回应第一个 input）
    process.stdin.write("17787155514\n")
    process.stdin.flush()

    # 获取子脚本全部输出并等待结束
    stdout, stderr = process.communicate()
    print("dddh 运行结果:\n", stdout)
    #print("Hello, World!")

def wxcy():
    # 启动子进程
    process = subprocess.Popen(
        [sys.executable, "wxcy.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=1  # 行缓冲区
    )

    process.stdin.write("2\n")
    process.stdin.flush()

    process.stdin.write("17787155514\n")
    process.stdin.flush()

    # 获取子脚本全部输出并等待结束
    stdout, stderr = process.communicate()
    print("wxcy运行结果:\n", stdout)
    #print("Hello, World!")

def my_task():
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 执行脚本任务...")
    dddh()
    wxcy()

if __name__ == "__main__":
    INTERVAL = 15   # 间隔 15 秒
    TOTAL_RUNS = 10 # 循环执行 10 次

    for i in range(TOTAL_RUNS):
        my_task()
        if i < TOTAL_RUNS - 1:
            time.sleep(INTERVAL)
