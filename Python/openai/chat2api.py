import os
import requests 
from dotenv import load_dotenv


"""
curl https://api.oaifree.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
    #  "model": "gpt-3.5-turbo",
    "model": "gpt-4",
     "messages": [{"role": "user", "content": "who are you?"}],
     "temperature": 0.7
   }'
支持模型：
   text-davinci-002-render-sha 8K
gpt-4 32K
gpt-4-mobile 32K
gpt-4-gizmo 32K
gpt-4-magic-create 32K
gpt-4-plugins 32K
任何其他模型等同 text-davinci-002-render-sha

更新：

team账号只需要传递 ChatGPT-Account-ID 头即可实现切换。
支持使用 gizmo，使用 g-xxx 的 id 作为模型名即可。
支持 whisper，使用 https://api.oaifree.com/v1/audio/transcriptions
我限制了 whisper 上传文件大小为：4M 。
已可对话出图。

"""
load_dotenv()
# print(dict(os.environ)['OPENAI_API_KEY'])

OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
# print(OPENAI_API_KEY)

def get_chat2api_with_whisper():
    url = 'https://api.oaifree.com/v1/audio/transcriptions'
    headers = {
        'Authorization': 'Bearer {}'.format(OPENAI_API_KEY)}
    
    cwd = os.getcwd()
    print(cwd)

    # 定义要上传的文件路径
    file_path = 'output.mp3'  # 替换为你的文件路径

    print(file_path)

    full_path = os.path.join(cwd, file_path)
    print("Full path using cwd:", full_path)

    # 以二进制模式打开文件
    files = {'file': ('audio.mp3', open(full_path, 'rb'), 'audio/mp3'),
             "model": "whisper-1"
             }
    # 发送POST请求
    response = requests.post(url, headers=headers, files=files)
    print(response.json())
    # 关闭文件（避免资源泄漏）
    files['file'][1].close()


def get_chat2api_with_gpt_4():
    url = 'https://api.oaifree.com/v1/chat/completions'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer {}'.format(OPENAI_API_KEY)}
    
    data = {
        # "model": "gpt-3.5-turbo",
        "model": "gpt-4", # "gpt-4", "gpt-3.5-turbo
        "messages": [{"role": "user", "content": "who are you?"}],
        "temperature": 0.7,
    }
    res = requests.post(url, headers=headers, json=data)
    print(res.json())

if __name__ == '__main__':
    # get_chat2api_with_gpt_4()
    get_chat2api_with_whisper()