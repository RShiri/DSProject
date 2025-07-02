# Strategic Tone Analysis in Israeli Academic News Articles

**Authors**: Ram Shiri, Amit Gitin, Lior Skudowitz, Nir Yemini  
**Course**: Introduction to Data Science (382.1.2601)  
**Institution**: Ben-Gurion University  
**Semester**: Spring 2025  
_Last updated: July 2025_

---

This project analyzes the strategic use of tone in news articles published on the official websites of Israeli academic institutions.  
The data was manually scraped from university news sections, cleaned, and annotated manually by the research team with tone and thematic tags.

---

## 🔍 Research Question

**How do Israeli universities communicate competition and cooperation, and how does that play out on their websites?**

---

## 📚 Contribution

This project builds on Nir Yemini’s work on coopetition in Israeli academia, expanding the focus from policy-level analysis to institutional **media discourse** as reflected in official university news articles.

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
│   └── plotting_code.R     # Optional: ggplot2 charts (externalized)
├── scrape/
│   └── scrape_code.R       # Optional: scraping logic (if available)
├── data/
│   └── ALL_articles.csv    # Final dataset
```

📄 See full [Final Report (PDF)](./final_report.pdf)

---

## 📄 Dataset Description

The main dataset is stored in `data/ALL_articles.csv` and includes the following columns:

| Column                    | Description                                                                 |
|---------------------------|-----------------------------------------------------------------------------|
| **institution**           | Name of the publishing university                                           |
| **date**                  | Date of publication                                                         |
| **title**                 | Article title                                                               |
| **url**                   | Link to the original article                                                |
| **tone**                  | One of: `cooperative`, `competitive`, `neutral`, `mixed`. <br> `mixed` = both coop & comp; `neutral` = neither. |
| **mentions_cooperation**  | Whether cooperation was mentioned (TRUE/FALSE)                              |
| **mentions_competition**  | Whether competition was mentioned (TRUE/FALSE)                              |
| **cooperation_type**      | Type of cooperation (e.g., Domestic, International)                         |
| **thematic_tags**         | Semicolon-separated thematic labels                                         |
| **length_words**          | Approximate article length (in words)                                       |

---

##  Visualizations

The final report includes the following visualizations:

- **Distribution of Article Tones** – Pie chart showing proportions of each tone.
- **Article Length Distribution by Tone** – Density plot (up to 1500 words).
- **Articles by Tone per Institution** – Bar chart showing counts per tone type.
- **Number of Posts per Institution (All Years)** – Stacked bar chart aggregating all tones.

All plots are created with `ggplot2` and displayed using `patchwork`.

---

##  Dependencies

To reproduce the analysis and knit the report, install the following R packages:

```r
install.packages(c("tidyverse", "lubridate", "ggplot2", "forcats", "patchwork"))
```
