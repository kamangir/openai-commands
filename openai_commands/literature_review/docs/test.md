# test run

```bash
@litrev choices=choices1,publish \
	$LITERATURE_REVIEW_OBJECT \
	--count 5 \
	--filename review_463333_screen_csv_20240730130035
```

`choices1.yaml`:

```yaml
description: read this abstract of a scentific paper
choices:
  antimicrobial: if it talks about antimicrobial treatment for cholera.
  susceptibility: if it has information regarding antibiotic-reistance or susceptibility to cholerae strains.
  otherwise: not relevant
```

![image](https://github.com/kamangir/assets/blob/main/openai_commands/literature-review/log.png?raw=true)

🔗 [AMR-v6-choices1.tar.gz](https://kamangir-public.s3.ca-central-1.amazonaws.com/AMR-v6-choices1.tar.gz)

📜 [literature_review.ipynb](../../notebooks/literature_review/literature_review.ipynb)