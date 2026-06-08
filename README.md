````markdown
# Trust & Safety Abuse Detection Pipeline

An LLM-ready content moderation pipeline that processes user-generated content, classifies abuse categories, generates moderation signals, and visualizes moderation insights through an interactive dashboard.

## Overview

This project simulates a Trust & Safety workflow used by modern online platforms to identify harmful content, prioritize moderation efforts, and monitor abuse trends at scale.

The system ingests user-generated comments, performs text normalization, classifies content into abuse categories, generates moderation signals, and presents actionable insights through a Streamlit dashboard.

The architecture is designed to support GPT-powered moderation workflows through a pluggable classification layer. A lightweight local classifier is included for development and testing, while production deployments can be configured to use OpenAI models through environment-based API integration.

## Features

- LLM-ready content moderation architecture
- Multi-label abuse classification
- Trust & Safety signal generation
- Risk prioritization and moderation workflows
- Structured output validation using Pydantic
- Moderation analytics and reporting dashboard
- Abuse trend monitoring
- High-risk content review interface
- Configurable OpenAI API integration

## Tech Stack

- Python
- OpenAI GPT-4 (LLM-ready integration)
- Pandas
- Pydantic
- Streamlit
- Git & GitHub

## Dataset

This project uses the Jigsaw Toxic Comment Classification Dataset containing over 150,000 user-generated comments labeled across multiple toxicity categories.

Abuse categories include:

- Toxic
- Severe Toxic
- Obscene
- Threat
- Insult
- Identity Hate

## Architecture

```text
Dataset
   ↓
ingest.py
   ↓
normalize.py
   ↓
classify.py
      ├── Local Classification Mode
      └── OpenAI GPT Classification Mode
   ↓
aggregate.py
   ↓
Streamlit Dashboard
````

## Project Structure

```text
Trust-safety-abuse-detection/
│
├── dashboard/
│   └── streamlit_app.py
│
├── src/
│   ├── ingest.py
│   ├── normalize.py
│   ├── classify.py
│   ├── aggregate.py
│   └── schemas.py
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── outputs/
│
├── requirements.txt
├── README.md
└── .gitignore
```

## LLM Integration

The classification layer is designed to support GPT-powered moderation workflows using environment-based API configuration.

To enable OpenAI classification:

1. Create a `.env` file
2. Add your OpenAI API key
3. Configure the classification provider
4. Run the pipeline normally

Example:

```env
OPENAI_API_KEY=your_api_key_here
```

This architecture allows the moderation workflow to operate in both local-development and LLM-powered deployment modes without changes to downstream processing, aggregation, or dashboard components.

## Dashboard Capabilities

The dashboard provides:

* Total comment volume
* High-risk content monitoring
* Risk priority distribution
* Abuse category distribution
* Sample moderation results
* High-risk content review

## Running the Project

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Execute Pipeline

```bash
python src/ingest.py
python src/normalize.py
python src/classify.py
python src/aggregate.py
```

### Launch Dashboard

```bash
streamlit run dashboard/streamlit_app.py
```

## Sample Outputs

* Classified moderation results
* Risk-priority summaries
* Abuse category distributions
* Moderation analytics dashboard

## Future Enhancements

* GPT-powered moderation reasoning
* Human-in-the-loop review queue
* Active learning workflows
* Real-time moderation APIs
* Automated escalation policies
* Multi-model moderation orchestration

## Resume Highlights

* Processed 150K+ user-generated comments through an automated moderation pipeline.
* Generated abuse classification and risk-prioritization signals for Trust & Safety workflows.
* Designed an LLM-ready moderation architecture supporting future GPT-powered classification.
* Built an interactive dashboard for abuse trend monitoring and high-risk content review.

```
```
