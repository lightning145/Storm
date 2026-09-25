import sys
import subprocess

a = 0

while (a != 10):
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
    a += 1
