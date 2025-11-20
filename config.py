import os

BASE_DIR = os.Path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.Path.join(BASE_DIR,"output")
os.makedirs(OUTPUT_DIR,exist_os=True)

NLM_FRAMES = 30
INPUT_SIZE = (224,224)