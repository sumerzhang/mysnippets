from openai import OpenAI
key = ''
base_url = 'https://api.oaifree.com/v1'
client = OpenAI(api_key=key, base_url=base_url)

response = client.audio.speech.create(
  model='tts-1',
  voice='shimmer',
  input='那个天才的想法这就实现了？你特这么是个天才!',
)

response.stream_to_file('./output.mp3')

