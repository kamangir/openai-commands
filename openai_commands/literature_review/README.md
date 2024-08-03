
# 🛠️ literature review

literature review using [OpenAI API](../completion/).

```bash
 > literature_review help
literature_review \
	[dryrun,~download,~upload] \
	[.|<object-name>] \
	[--count <-1>] \
	[--filename <filename.csv>] \
	[--choices <choices.yaml>]
 . run literature review on <object-name>.
```

## example run

```bash
literature_review - AMR-v1 \
	--count 5 \
	--filename review_463333_screen_csv_20240730130035.csv \
	--choices choices1.yaml
```

`choices1.yaml`:

```yaml
antimicrobial: if it talks about antimicrobial treatment for cholera.
susceptibility: if it has information regarding antibiotic-reistance or susceptibility to cholerae strains.
otherwise: not relevant 
```


![image](https://github.com/kamangir/assets/blob/main/openai_commands/literature-review/log.png?raw=true)

🔗 [AMR-v1.tar.gz](https://kamangir-public.s3.ca-central-1.amazonaws.com/AMR-v1.tar.gz)

📜 [literature_review.ipynb](../../notebooks/literature_review/literature_review.ipynb)

---

notes: [1](https://arash-kamangir.medium.com/%EF%B8%8F-open-ai-experiments-146-6d3390da78c3), [2](https://arash-kamangir.medium.com/%EF%B8%8F-open-ai-experiments-145-dc241e47d9e1)