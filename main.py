import sys
import subprocess

import time
from datetime import datetime

def my_task():
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 执行脚本任务...")

if __name__ == "__main__":
    INTERVAL = 15   # 间隔 15 秒
    TOTAL_RUNS = 10 # 循环执行 20 次

    for i in range(TOTAL_RUNS):
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
        print("运行结果:\n", stdout)
        #print("Hello, World!")
        if i < TOTAL_RUNS - 1:
            time.sleep(INTERVAL)
