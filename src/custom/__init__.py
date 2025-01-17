'''
Supported component type entrypoints

- Implement the specific entrypoint associated with your component type
- You can leave the others unimplemented

To support streaming, your implementation should be a generator: https://wiki.python.org/moin/Generators
You may also simply return the final result
'''

import os
from .model import GroqModel

t2t_model = GroqModel(
    os.getenv("GROQ_API_KEY"),
    os.getenv("MODEL")
)

# For speech-to-text models
def start_stt(audio: bytes) -> str:
    raise NotImplementedError

# For text generation models
def start_t2t(system_prompt: str, user_input: str) -> str:
    global t2t_model
    for content_chunk in t2t_model(system_prompt, user_input):
        yield content_chunk

# For text-to-speech generation
def start_ttsg(text: str) -> bytes:
    raise NotImplementedError

# For voice changers
def start_ttsc(audio: bytes) -> bytes:
    raise NotImplementedError