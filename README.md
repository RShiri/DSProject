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

Our goal was to explore how Israeli academic institutions use cooperative, competitive, neutral, or mixed (now labeled *Coopetitive*) framing in their official communications, and whether this framing correlates with institutional factors (e.g., size, prestige, publication volume, global ranking).

---

## 📁 Project Structure

```

final-project/
├── README.md              # Project overview and team info
├── proposal.Rmd           # Research proposal document
├── final_report.Rmd       # Full report with code and analysis
├── final_report.pdf       # Knitted PDF version of the report
├── code/
│   └── plotting_code.R    # Optional: reusable ggplot2 charts
├── scrape/
│   └── scrape_code.R      # Scraping logic 
├── data/
│   ├── ALL_articles_final_corrected.csv   # Main dataset 
│   

```
 See full [Final Report (PDF)](./Final_report.pdf)

---

## 📄 Dataset Descriptions

### `ALL_articles.csv`

| Column                    | Description                                                                 |
|---------------------------|-----------------------------------------------------------------------------|
| **institution**           | Name of the publishing university                                           |
| **date**                  | Date of publication                                                         |
| **title**                 | Article title                                                               |
| **url**                   | Link to the original article                                                |
| **tone**                  | One of: `Cooperative`, `Competitive`, `Neutral`, `Coopetitive`. <br> `Coopetitive` = both coop & comp; `Neutral` = neither. |
| **mentions_cooperation**  | Whether cooperation was mentioned (TRUE/FALSE)                              |
| **mentions_competition**  | Whether competition was mentioned (TRUE/FALSE)                              |
| **cooperation_type**      | Type of cooperation (e.g., Domestic, International)                         |
| **thematic_tags**         | Semicolon-separated thematic labels                                         |
| **length_words**          | Approximate article length (in words)                                       |

### `shanghai.csv`

| Column            | Description                                                     |
|-------------------|-----------------------------------------------------------------|
| **University/Year** | University name (row name)                                     |
| **2003–2024**     | Shanghai rank per year. May include exact rank or a range.      |

---

## 📈 Visualizations

The final report includes the following visualizations:

- **Distribution of Article Tones** – Pie chart showing tone proportions.
- **Article Length Distribution by Tone** – Density plot (up to 1500 words).
- **Articles by Tone per Institution** – Bar chart showing counts per tone type.
- **Shanghai Ranking Over Time** – Line chart showing Shanghai global rankings (2003–2024).

All plots are created with `ggplot2` and arranged using `patchwork`.

---

## 📦 Dependencies

To reproduce the analysis and knit the report, install the following R packages:

```r
install.packages(c("tidyverse", "lubridate", "ggplot2", "forcats", "patchwork"))


