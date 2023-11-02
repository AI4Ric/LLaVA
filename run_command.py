import os

os.system("""curl -X POST http://localhost:40000/worker_generate_stream \
-H 'Content-Type: application/json' \
-d '{"model":"llava-v1.5-13b","prompt":"A chat between a curious human and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the human\\'s questions. USER: hello, how are you today? ASSISTANT:","temperature":0.2,"top_p":0.7,"max_new_tokens":512,"stop":"</s>","images":[]}' \
--output response.txt""")
