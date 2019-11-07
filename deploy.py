#! /usr/bin/env python3

import os
import shutil
import time

DIST_PATH = "./dist"
SANDBOX_PATH = "./.sandbox_repo"
BRANCH_NAME = "deploy"

def cmd(_c: str):
    os.system(_c)

print("1. 正在执行 npm run build")
cmd("npm run build >/dev/null 2>&1")

if not os.path.exists(DIST_PATH):
    print("无法找到 dist 产物目录")
    exit(0)

if os.path.exists(SANDBOX_PATH):
    shutil.rmtree(SANDBOX_PATH)

os.mkdir(SANDBOX_PATH)
shutil.copytree(DIST_PATH, SANDBOX_PATH + "/dist")

black_list = [".gitignore"]

# 配置文件
print(f"2. 复制所需文件")
for file in os.listdir(os.curdir):
    if os.path.isdir(file) or file in black_list:
        continue
    if os.path.isfile(file):
        os.system(f"cp {file} '{SANDBOX_PATH}'")

# git
os.chdir(SANDBOX_PATH)
print(f"3. 开始执行 Git 发布到 {BRANCH_NAME} 分支")
cmd("git init >/dev/null 2>&1")
cmd(f"git checkout --orphan {BRANCH_NAME} >/dev/null 2>&1")
cmd("git add .")
time_mst = time.strftime("%d/%m/%Y %H:%M:%S")
cmd(f'git commit -am "update in {time_mst}" >/dev/null 2>&1')
cmd("git remote add origin git@github.com:Desgard/DissCode-FE.git >/dev/null 2>&1")
cmd(f"git push origin {BRANCH_NAME} --force  >/dev/null 2>&1")
