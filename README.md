# Retail Data Analysis and Visualization Pipeline

This repository showcases an end-to-end solution for analyzing retail data. Leveraging a Kaggle CSV dataset, the project provides a comprehensive workflow from data ingestion to visualization.

## Table of Contents

- [Overview](#overview)
- [Technologies Used](#technologies-used)
- [Setup](#setup)
- [Usage](#usage)
- [License](#license)

## Overview

The project is designed to:
1. Ingest raw retail data into Google Cloud.
2. Perform data quality checks using Soda.
3. Build data models with DBT.
4. Visualize insights through Sigma dashboards.
5. Manage the entire data pipeline with Airflow and the Astro CLI.
6. Ensure a robust infrastructure with Cosmos.

## Technologies Used

- **Google Cloud**: Cloud data platform for data ingestion.
- **Soda**: Data quality checks and monitoring.
- **DBT**: Data transformation and modeling.
- **Sigma**: Data visualization and dashboard creation.
- **Airflow & Astro CLI**: Data pipeline orchestration.
- **Cosmos**: Infrastructure management.

## Setup

This project is based on the tutorial by Marc Lamberti. If you wish to replicate or understand the detailed steps, please refer to [this guide](https://robust-dinosaur-2ef.notion.site/PUBLIC-Retail-Project-af398809b643495e851042fa293ffe5b).

## Usage

The project starts by ingesting raw retail data into Google Cloud. After ensuring data quality with Soda, the data undergoes transformation and modeling with DBT. Insights derived from the data are then visualized using Sigma dashboards. The entire process, from ingestion to visualization, is orchestrated using Airflow and the Astro CLI, ensuring a seamless and automated data pipeline.

## License

This project is licensed under the [MIT License](LICENSE.md).
