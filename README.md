# TechStockAnalysis

## Status: 

IN - PROGRESS

## Aim: 

To create a custom index which tracks major tech stocks such as Microsoft, Amazon, Google, Facebook, etc by building an automated data pipeline using yfinance package and hosting on AWS platform.

## Current Progress:

1) Creating py executable file which reads stock table from RDS having info about stocks and a) creates individual stock tables b) Updates the base table's stock name field

## High Level Architecture

![Stock Analysis Solution Architecture](StockAnalysisFlowchartv1.drawio.png "Stock Analysis Solution Architecture")

## Task List

- [x] stockDataExtract.py takes argument as stock symbol and produces csv.
This will be used as base for making lambda function, interacting with SNS Topic, RDS and API Gateway as shown above.

- [x] updateStockTable (as a lambda) deployed over RDS invoked via API, which inserts stock symbol and weight upon invocation

## Resources Used:

1. yfinance package: https://pypi.org/project/yfinance/ 

2. Diagram made from draw.io : https://app.diagrams.net/

3. Cloud environment on AWS: https://aws.amazon.com/
