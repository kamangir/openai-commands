# 🛠️ VisuaLyze

> How about calling it "VisuaLyze"? This name combines "visualize" and "analyze," reflecting the tool's capability to generate custom data visualizations and analyze user input through AI - OpenAI.

```bash
VisuaLyze run
```

![image](https://github.com/kamangir/openai-commands/assets/1007567/7c0ed5f7-6941-451c-a17e-504c6adab23f)

sample output for [`onlinefoods`](./assets/VisuaLyze/onlinefoods/).

```python
import pandas as pd
import matplotlib.pyplot as plt

def VisuaLyze(df: pd.DataFrame()):
    # Generate a matplotlib visualization of one aspect of the dataset

    # For example, let's say we want to visualize the distribution of ages in the dataset
    plt.figure(figsize=(10,6))
    df['Age'].hist(bins=20, color='skyblue', edgecolor='black')
    plt.title('Distribution of Ages in the Online Food Order Dataset')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.show()
```