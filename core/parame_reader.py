import re
import os
import subprocess
from . import log_creater


def read_adb_address():
    adb_info = os.path.join(os.getcwd(), "settings.txt")

    try:
        with open(adb_info, 'r', encoding='utf-8', errors='ignore') as file:
            content = file.read()
            adb_path_match = re.search(r'adb_path = (.+?)$', content, re.MULTILINE)
            adb_port_match = re.search(r'adb_port = (\d+)', content)

        if adb_path_match and adb_port_match:
            adb_path_raw = adb_path_match.group(1)
            adb_path = adb_path_raw.strip('"')
            adb_port = adb_port_match.group(1)
            return adb_path, adb_port
        else:
            log_message = log_creater.write_log("没找到adb路径或端口 \n请检查txt和当前模拟器的adb是否一致")
            print(log_message)
            return None, None
        
    except Exception as e:
        log_message = log_creater.write_log(f"读取adb地址出错: {str(e)}")
        print(log_message)
        return None, None


def run_adb(adb_path, adb_port):
    try:
        subprocess.run([adb_path, "connect", "127.0.0.1:" + adb_port], check=True)
        log_message = log_creater.write_log(f"adb路径: {adb_path} \nadb端口: {adb_port}")
        print(log_message)
    except subprocess.CalledProcessError as e:
        log_message = log_creater.write_log(f"Failed to connect to device: {e}")
        print(log_message)
