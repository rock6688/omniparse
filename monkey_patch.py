# monkey_patch.py

import requests

# 备份原始的 requests.get 方法
original_get = requests.get

# 定义一个新的 get 函数
def patched_get(url, *args, **kwargs):
    # 检查并替换 URL
    if url.startswith("https://huggingface.co/"):
        url = url.replace("https://huggingface.co/", "https://mirror.huggingface.co/")
    # 调用原始的 get 方法
    return original_get(url, *args, **kwargs)

# 替换 requests.get 为 patched_get
requests.get = patched_get

# 如果还需要处理其他方法，比如 requests.post
original_post = requests.post

def patched_post(url, *args, **kwargs):
    if url.startswith("https://huggingface.co/"):
        url = url.replace("https://huggingface.co/", "https://mirror.huggingface.co/")
    return original_post(url, *args, **kwargs)

requests.post = patched_post

"""
在项目启动时应用猴子补丁
在项目的入口文件（通常是 main.py 或类似文件）中，导入并应用猴子补丁模块。确保这个导入在其他代码运行之前进行。

例如，在 main.py 中：

# 导入并应用猴子补丁
import monkey_patch

# 你项目的其他代码
import requests

def main():
    # 测试请求
    response = requests.get('https://huggingface.co/vikp/surya_det3/resolve/main/config.json')
    print(response.url)  # 应该输出 'https://mirror.huggingface.co/vikp/surya_det3/resolve/main/config.json'
    print(response.json())

if __name__ == "__main__":
    main()

"""
