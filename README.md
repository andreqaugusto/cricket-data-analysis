# Cricket Data Analysis

This repository is the solution for a technical test given by a company during the interview process for a Senior Data Engineer position.

## The Challenge

This assessment involves engineering a data ingest process for ball-by-ball data from professional cricket matches. The data include the overall match results and outcomes for every delivery for both teams. The questions below are an opportunity to showcase your data engineering skills as they involve building a data ingest pipeline and running exploratory analysis on that data set.

There are many implementation options and the assessment provides an opportunity for you to determine what assumptions are appropriate and operate within those. Since the purpose of this assessment is to showcase your technical and problem-solving skills, please include clear, efficient, and well-organized code along with explanations on the justification for your approach. Please also include instructions on how to run your code, and structure it in a way that makes it as reproducible as possible.

More information about the assessment and the questions needed to be answered can be found at [ASSESSMENT.md](./challenge/ASSESSMENT.md). The answers for the questions asked in the assessment can be found at the `answers` folder.

## How to Run

First, install all dependencies by running 
```
pip install -r requirements.txt
```
on your Python environment. Keep in mind that this project was built using Python 3.10.

Then, just run
```
python main.py
```

that we will download the data from Cricsheet and create a `cricsheet.db` SQLite database in the `database` folder.