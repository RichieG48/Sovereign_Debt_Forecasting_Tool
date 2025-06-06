# Sovereign_Debt_Forecasting_Tool

The goal is to make a tool to forecast sovereign debt, and make forecasting scenarios with different rate cuts / spending and earnings from the States.

Backend : forecasting ML model, trained on historical data from several countries. As features it will have the time series but also the rate cuts, the forecasted rate cuts (that will be entered by the user, for instance : flat, 5 cuts, raise etc...). The State deficit (there will also be the possibility to choose a target 
deficit to see how it affects the debt scenario).

Frontend : Dash page with a dropdown to select the country, then select the parameters of your scenario (possibility to put several scenarios at once to compare them). Then a dcc graph to plot everything.
