
# 🛠️ literature review (`@litrev`)

literature review using [OpenAI API](../completion/).

```bash
 > @litrev help
@litrev \
	[choices=<choices>,dryrun,~download,publish,suffix=<suffix>,~upload] \
	[AMR-v6|<object-name>] \
	[--count <-1>] \
	[--filename <filename>] \
	[--overwrite 1] \
	[--verbose 1]
 . <object-name>/<filename>.csv -literature-review-@-<choices.yaml>-> <object-name>-<suffix>/<filename>-<choices>.csv.
```

## example run

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

## for study type

`choices-study-type.yaml`

```yaml
description: select from these studies theose that assess the clinical efficacy of cholera treatments and/or examine the antibiotic resistance in Vibrio cholerae strains in clinical samples
choices:
  clinical trials: if it talks about clinical trials.
  prospective observational studies: if it talks about prospective observational studies with comparators like Standard care, placebo, or other antibiotics.
  cross sectional: if it talk about cross-sectional studies.
  surveillance studies: if it talks about surveillance.
```

## for screening results

`choices-screening-result.yaml`

```yaml
description: select from these studies theose that assess the clinical efficacy of cholera treatments and/or examine the antibiotic resistance in Vibrio cholerae strains in clinical samples
choices:
  antibiotic treatment: if it talks about the intervention with any of these antibiotic treatments, tetracycline* or doxycycline* or azithromycin or erythromycin or clarithromycin, roxithromycin or ciprofloxacin or nalidixic acid or chloramphenicol or furazolidone or norfloxacin or cotrimoxazole or trimethoprim or sulfamethoxazole or sulphamethoxazole, assessing clinical efficacy (benefits) of different antimicrobial treatments.
  outcome: if it mentioned any of the following outcomes, mortality, duration of illness (diarrhea), total stool volume, total days of hospitalization, total amount of intravenous fluid needed, fecal excretion of the bacteria.
  susceptibility: if it talks about antibiotic susceptibility in bacterial culture, or less commonly genomic data, antibiotic* or antimicrob* or (antimicrobial resistance) or susceptible or susceptibility, antibiotic susceptibility testing and prevalence of antibiotic-resistant or resistance pattern in clinical samples.
  no full-text review: if it talks about non-human studies, environmental samples, water sources, traditional medicines, natural, leaf, leaves, peptides, or extracts.
```

---

notes: [1](https://arash-kamangir.medium.com/%EF%B8%8F-open-ai-experiments-146-6d3390da78c3), [2](https://arash-kamangir.medium.com/%EF%B8%8F-open-ai-experiments-145-dc241e47d9e1)