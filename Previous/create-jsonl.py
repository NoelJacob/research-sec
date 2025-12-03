# %%
import json

import pandas as pd

# %%
df = pd.read_csv("./edgartools-data.csv")

# %%
part1 = '{"request":{"contents":[{"role":"user","parts":[{"text":'
part2 = '}]}],"generationConfig":{"responseMimeType":"application/json","responseSchema":{"type":"OBJECT","properties":{"chain_of_thought":{"type":"STRING"},"estimated_mw":{"type":"INTEGER"},"score":{"type":"NUMBER","minimum":0,"maximum":10},"confidence":{"type":"INTEGER","minimum":0,"maximum":100}},"required":["chain_of_thought","estimated_mw","score","confidence"]}}}}'

# %%
with open("./system_prompt_2.md", "r", encoding="utf-8") as f:
    system_prompt = f.read()

# %%
batch_size = 100
with open("./text.jsonl", "a", encoding="utf-8") as f:
    batch = []
    for path in df["path"]:
        with open(path, "r", encoding="utf-8") as file_f:
            file_content = file_f.read()
        prompt = (
            part1 + json.dumps(system_prompt + "INPUT FILE**\n" + file_content) + part2
        )
        batch.append(prompt)
        if len(batch) >= batch_size:
            f.write("\n".join(batch) + "\n")
            f.flush()
            batch = []
    if batch:
        f.write("\n".join(batch) + "\n")
        f.flush()

# %%
