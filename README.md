# EDGAR
A package containing 4 modules which:
1.Extract 10-k filing reports for all companies in the SP-100 index  
2. Performs FDA on all docs
3. Extracts sentiment words from the Loughran-McDonald Dictionary
4. Counts the number of words falling into each sentiment: Negative, Positive, Uncertainty, Litigious and Constraining for each report.
5.Extracts financial data for each company

The Jupyter notebook file 'run_me.ipynb' performs each of the above steps to give sentiment factors for each company from each report. The financial data is outputted to the file 'daily_stock_prices_df.csv' which contains the price fluctuation and daily return calculations for 1,2,3, 5 and 10 business days over a period of 10 years.

