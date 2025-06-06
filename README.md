# 🧠 Reddit Topic Modeling: Kannada Language Debate (June 2025)

## 📍 Project Overview

This project performs **topic modeling** on Reddit comments related to a recent and widely discussed incident in India involving a **female SBI manager** who **refused to speak in Kannada**. The video of the incident went viral and led to a heated public debate about language, identity, and nationalism — especially within the context of **South India’s resistance to Hindi imposition**.

Using Reddit as a platform for analysis provides a window into **authentic, public reactions**. The specific post under analysis attracted **over 600 comments**, making it a rich source for natural language understanding.

This project demonstrates how we can use unsupervised machine learning (specifically **Latent Dirichlet Allocation**) to uncover hidden themes in public discourse.

---

## 🔍 Why Reddit?

Reddit offers:
- **Unfiltered public opinion**: Unlike curated news headlines, Reddit reflects how everyday users argue, react, and feel.
- **Anonymity**: Encourages people to express opinions freely, making it ideal for linguistic, political, and identity-based analysis.
- **Viral reach**: The episode selected had national visibility, ensuring a wide spectrum of viewpoints.

---

## 🧪 Methodology

- Comments were manually scraped and compiled into a single `comments.txt` file.
- Preprocessing included:
  - Lowercasing
  - Tokenization
  - Removal of stopwords and punctuation
- Used `nltk` and `gensim` for text cleaning and topic modeling.
- Modeled using **Latent Dirichlet Allocation (LDA)** with 4 topics.

---

## 🧠 Topics & Interpretations

The model identified **4 distinct themes** in the comments. Here’s a breakdown:

| Topic No. | Top Keywords                                       | Interpretation                         |
|-----------|----------------------------------------------------|----------------------------------------|
| **1**     | language, time, people, come, kannada              | 🟡 **Regional Language Assertion**<br>Comments expressing pride or concern over Kannada not being used or respected. |
| **2**     | language, people, state, know, dont                | 🟠 **State Identity and Public Sentiment**<br>Emotions around regional belonging, language rights, and perceived disrespect. |
| **3**     | language, hindi, speak, english, local             | 🔵 **Language Politics – Hindi vs English**<br>Discussions over which language should be spoken and by whom, touching on power, privilege, and resistance. |
| **4**     | language, english, north, people, india            | 🔴 **North-South Language Divide**<br>Critique of national language politics, northern dominance, and cultural marginalization of the South. |

Each topic reveals a facet of the broader public mood — from linguistic pride to frustration with systemic marginalization.

---

## 📁 Project Structure

Reddit_kannada_debate_topic_modeling/
│
├── comments.txt # Manually collected Reddit comments
├── topic_modeling.py # Python script for topic modeling
├── requirements.txt # Environment dependencies
└── README.md # This file--- TOPICS FOUND ---
Topic 1: 0.013*"language" + 0.007*"time" + 0.006*"people" + 0.006*"come" + 0.005*"kannada"
Topic 2: 0.018*"language" + 0.017*"people" + 0.014*"state" + 0.010*"know" + 0.009*"dont"
Topic 3: 0.039*"language" + 0.022*"hindi" + 0.020*"speak" + 0.016*"english" + 0.015*"local"
Topic 4: 0.022*"language" + 0.018*"english" + 0.010*"north" + 0.009*"people" + 0.008*"india"

yaml
Copy
Edit

---

## 💼 Why This Project Matters

This project is part of my learning journey in:
- **Natural Language Processing (NLP)**
- **Python scripting**
- **Topic modeling using unsupervised learning**
- **Understanding public opinion through computational methods**

It showcases the use of real-world, sensitive social data to derive analytical insight — a skill relevant to roles in:
- **Data Analysis**
- **Digital Humanities**
- **Computational Social Science**
- **Policy Research**
- **Media & Communication Analytics**

---

## 🔧 Dependencies

To run this project, install dependencies with:

```bash
pip install -r requirements.txt