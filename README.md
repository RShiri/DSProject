# Strategic Tone Analysis in Israeli Academic News Articles

**Authors**: Ram Shiri, Amit Gitin, Lior Skudowitz, Nir Yemini  
**Course**: Introduction to Data Science (382.1.2601)  
**Institution**: Ben-Gurion University  
**Semester**: Spring 2025

---

This project analyzes the strategic use of tone in news articles published on the official websites of Israeli academic institutions.  
The data was manually collected from university websites, cleaned, and annotated with tone and thematic tags.

---

## 📊 Objective

Our goal was to explore how Israeli academic institutions use cooperative, competitive, neutral, or mixed framing in their official communications, and whether this framing correlates with institutional factors (e.g., size, prestige, publication volume).

---

## 📁 Project Structure

```
final-project/
├── README.md               # This file
├── proposal.Rmd            # Research proposal document
├── final_report.Rmd        # Final report with code and analysis
├── final_report.pdf        # PDF version of the knitted report
├── code/
│   └── plotting_code.R     # Optional: all ggplot2 charts in standalone file
├── data/
│   └── ALL_articles.csv    # Final dataset
├── figures/
│   ├── pie_chart.png
│   ├── length_density.png
│   ├── tone_by_inst_bar.png
│   └── tone_by_inst_stacked.png
```

---

## 📄 Dataset Description

The main dataset is stored in `data/ALL_articles.csv` and includes the following columns:

| Column                    | Description                                                         |
|---------------------------|---------------------------------------------------------------------|
| **institution**           | Name of the publishing university                                   |
| **date**                  | Date of publication                                                 |
| **title**                 | Article title                                                       |
| **url**                   | Link to the original article                                        |
| **tone**                  | One of: `cooperative`, `competitive`, `neutral`, `mixed`            |
| **mentions_cooperation**  | Whether cooperation was mentioned (TRUE/FALSE)                      |
| **mentions_competition**  | Whether competition was mentioned (TRUE/FALSE)                      |
| **cooperation_type**      | Type of cooperation (e.g., Domestic, International)                 |
| **thematic_tags**         | Semicolon-separated thematic labels                                 |
| **length_words**          | Approximate article length (in words)                               |
| **shanghai_ranked**       | Whether the university appears in the Shanghai ranking (TRUE/FALSE) |

---

## 🎨 Visualizations

The final report includes the following visualizations:

- **Distribution of Article Tones** – Pie chart showing proportions of each tone.
- **Article Length Distribution by Tone** – Density plot (up to 1500 words).
- **Articles by Tone per Institution** – Horizontal bar chart showing counts per tone type.
- **Number of Posts per Institution (All Years)** – Stacked bar chart aggregating all tones.

All plots are created with `ggplot2` and displayed in a unified layout.

---

## ℹ️ Notes

- `mixed` tone refers to articles that include **both cooperative and competitive framing**. These articles were counted in both tone categories in some analyses, and marked distinctly in others.
- `neutral` tone refers to articles that do **not mention cooperation or competition** at all.

---

## 📦 Dependencies

To reproduce the analysis and knit the report, install the following R packages:

```r
install.packages(c("tidyverse", "lubridate", "ggplot2", "forcats", "patchwork"))
```

---
