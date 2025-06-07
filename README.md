**Reddit Topic Modeling: Kannada Language Debate (June 2025)**

This project performs topic modeling on Reddit comments related to a recent and widely discussed incident in Bangalore, India involving a female SBI manager who refused to speak in Kannada. The video of the incident went viral and led to a heated public debate about language, identity, and nationalism, especially within the context of South India’s resistance to Hindi imposition.

Using Reddit as a platform for analysis provides a window into non-mainstream social-media public reactions with this specific post attracting over 600 comments, making it a rich source for natural language understanding.

This project demonstrates how we can use unsupervised machine learning (specifically Latent Dirichlet Allocation) to uncover the connections shared between various hidden themes in public discourse.

#Why Reddit?

**Reddit offers:**

Public opinion: Unlike curated news headlines and instagram or Facebook, Reddit offers a degree of anonymity which helps reflect how everyday users argue, react, and feel.

Anonymity: The said anonymity encourages people to express opinions freely, making it ideal for linguistic, political, and identity-based analysis.

Viral reach: The episode selected had national visibility, ensuring a wide spectrum of viewpoints.

**Methodology**

Comments were scraped and compiled into a single comments.txt file.

Preprocessing included:

Lowercasing

Tokenization

Removal of stopwords and punctuation

Used nltk and gensim for text cleaning and topic modeling.

Modeled using Latent Dirichlet Allocation (LDA) with 4 topics.

**Topics and Interpretations**

The model identified 4 distinct themes in the comments. Here is a breakdown:

Topic 1
Top keywords: language, time, people, come, kannada

Interpretation: Regional Language Assertion

Comments here reflect frustration that outsiders (**people**) **come** to Karnataka but don’t respect **Kannada**, possibly directing towards stronger regional linguistic pride.

Topic 2
Top keywords: language, people, state, know, dont
Interpretation: State Identity and Public Sentiment


Emotions around regional (**State**) belonging, **know**ing language rights, and perceived disrespect (**dont**). Unlike Topic 1 which is about asserting Kannada in general, Topic 2 reflects discussions around civic responsibilty (people), ignorance, and feelings of exclusion (**dont**)

Topic 3
Top keywords: language, hindi, speak, english, local

Interpretation: Language Politics – Hindi vs English

Discussions over which language should be spoken (**Hindi and English**) and by whom, touching upon linguistic politics — language choice as identity and resistance. This topic touches on power, privilege, and resistance by highlighting the pressure of choosing between dominant languages like Hindi and English, while defending the legitimacy of **local** languages. The term local itself has traditionally had great discursive significance in distinguishing between local and national. 

Topic 4
Top keywords: language, english, north, people, india

Interpretation: North-South Language Divide

Critique of national language politics, highlighting the divisive nature of Northern Southern linguistic dentities, and questions on cultural marginalization of the South.

Each topic reveals a facet of the broader public mood — from linguistic pride to frustration with systemic marginalization.

Topic 1 and 2 are both grounded in regional sentiment, language use in everyday life, and local identity.  Topic 3 and 4 shift from local sentiment to macro-political frameworks, involving national power, Hindi dominance, English privilege, and North-South tensions.

**Project Structure**

Reddit_kannada_debate_topic_modeling/
│
├── comments.txt - Manually collected Reddit comments
├── topic_modeling.py - Python script for topic modeling
├── requirements.txt - Environment dependencies
└── README.md - This file

**Topics Found**

Topic 1: 0.013*"language" + 0.007*"time" + 0.006*"people" + 0.006*"come" + 0.005*"kannada"
Topic 2: 0.018*"language" + 0.017*"people" + 0.014*"state" + 0.010*"know" + 0.009*"dont"
Topic 3: 0.039*"language" + 0.022*"hindi" + 0.020*"speak" + 0.016*"english" + 0.015*"local"
Topic 4: 0.022*"language" + 0.018*"english" + 0.010*"north" + 0.009*"people" + 0.008*"india"

**Why This Project Matters**

This project is part of my learning journey in:

Natural Language Processing (NLP)

Python scripting

Topic modeling using unsupervised learning

Understanding public opinion through computational methods

It showcases the use of real-world, sensitive social data to derive analytical insight — a skill relevant to roles in:

Data Analysis

Digital Humanities

Computational Social Science

Policy Research

Media and Communication Analytics

Dependencies

**To run this project, install dependencies with:**

pip install -r requirements.txt

