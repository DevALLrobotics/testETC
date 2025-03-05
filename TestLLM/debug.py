# import torch
# print("CUDA Available:", torch.cuda.is_available())
# print("GPU Count:", torch.cuda.device_count())
# print("GPU Name:", torch.cuda.get_device_name(0) if torch.cuda.is_available() else "No GPU")

# import os
# from dotenv import load_dotenv
# from huggingface_hub import login

# # โหลดค่าใน .env
# load_dotenv()

# # ดึงค่า Token
# hf_token = os.getenv("HF_TOKEN_KEY")
# login(hf_token)

# import transformers
# import torch

# model_id = "meta-llama/Meta-Llama-3-8B"

# pipeline = transformers.pipeline(
#     "text-generation", model=model_id, model_kwargs={"torch_dtype": torch.bfloat16}, device_map="auto"
# )

# pipeline("Hey how are you doing today?")

import torch

# รับข้อความจากผู้ใช้
user_input = "ฉันรู้สึกเครียดมากเลยช่วงนี้"

# สร้าง prompt สำหรับให้โมเดลเข้าใจบทบาท
prompt = f"""คุณคือผู้ช่วยดูแลสุขภาพจิตที่สุภาพและอบอุ่น 
กรุณาตอบข้อความด้านล่างนี้ด้วยคำพูดที่ให้กำลังใจ:

"{user_input}"
"""

# Tokenize ข้อความ
inputs = tokenizer(prompt, return_tensors="pt").to("cuda")

# สั่งให้โมเดล generate ข้อความตอบกลับ
outputs = model.generate(
    **inputs,
    max_new_tokens=200,        # จำนวน Token สูงสุดในการตอบ
    temperature=0.7,           # ควบคุมความหลากหลายของคำตอบ (0-1)
    top_p=0.9,                 # ควบคุมความน่าเป็นไปได้ของคำตอบ
)

# ถอดรหัสข้อความที่โมเดลตอบออกมา
response = tokenizer.decode(outputs[0], skip_special_tokens=True)

print("\n🤖 Bot ตอบกลับว่า:\n")
print(response)
