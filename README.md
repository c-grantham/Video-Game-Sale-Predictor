**Overview**

This ongoing project predicts when a video game will next go on sale and estimates the expected discount percentage based on historical price trends and game metadata.

The pipeline currently includes:

* Collecting historical price data and game metadata via APIs

* Storing data in a Dockerized SQL database

* Cleaning and preprocessing data with Python (pandas, NumPy)

Features to be implemented include:

* Training a machine learning model (XGBoost Regression) to forecast future discounts

* Evaluating performance with metrics such as RMSE and MSE

* Building a user interface in the form of a widget/webpage for users to easily access game price information before purchase
