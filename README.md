# Beyond Analysis Data Engineer Assignment

## This is my very first implementation of an ETL pipeline!

## How to run:

1. pip install pandas
2. Transform into csv using parquet_to_csv.py.
3. According to required results, change main.py to cater to: main_file, choose_filter_date, write_files(res, pth).
4. Once files have been created, use loader.py to create the database files. Adjust db name and path.

### There is a visual description included in Notes/Taxi_pipe_and_loader.ipynb

# Task summarization:

1. Firstly the taxi parquet file is transformed into .csv format. Then the program splits data by chosen date _January_, also storing invalid dates into a different folder, the files will be split accordingly to days of the month.
   I would count this as the first data quality metric- validity.

2. Loader.py injects the given folder that includes all the seperate files into SQLite as one database.

3. Data quality assurance is evaluated by two metrics: Validity and Completeness. Please proceed to the Notes folder, open the Data_Quality.ipynb file. (Github should display Jupyter Notebooks)

4. Due to a lack of time and enough knowledge, I have only modeled a schema which is located in the notes folder as schema.png.

5. My feeling is that due to lack of best-practice knowledge, my code may perhaps be hard to understand or contains spaghetti-code. I am very keen to improve on this! I'd say the visible weak points
   are automation, ease-of-use, run-time. The task also suggested considering a different file format, however I chose to stick with what I was more familiar with. Static files is also an issue, future improvements would involve a smarter way of automating the paths. Given more time, these are exactly the things I would improve. In addition: I would like to study data quality metrics with more
   depth since my implementation only includes two metrics. I have also only provided a schema for a fact-dimension version, having more time and knowledge I would have liked to also transform the dataset.
