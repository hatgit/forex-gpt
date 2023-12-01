
# Forex-Rates plugin for Chat-GPT from Forex-GPT.ai 
<img src="https://github.com/hatgit/forex-gpt/assets/5213035/c461f57b-d977-4c95-bc9f-de6abac01501" width="20%" height="auto">

# Install directly from within Chat-GPT:
Forex-Rates is now available to all Chat-GPT premium subscribers, as of June 10th, 2023. Please note that the Plugin works 7-days a week but the trading week is from 5pm EST on Sunday through 5pm EST on Friday, so any requests made on the weekend cannot be in the present tense as markets are closed on the weekends. 

<img src="https://github.com/hatgit/forex-gpt/assets/5213035/517f6fa8-d0c1-45b0-9658-733d04dc014a" width="35%" height="auto">


# Quickstart guide

This is a quick start guide for setting up and running the Forex-Rates OpenAI plugin, which integrates text analysis capabilities with the OANDA API for analyzing currency market data. If you do not already have plugin developer access, please [join the waitlist](https://openai.com/waitlist/plugins).

## Setup for Mac users

You will need the following API keys which can be obtained from their respective providers:

1) Open AI API key for developers:
2) OANDA API for for fxTrade demo account: 

revise the values contained in the `.env` file and set the following variables by repalacing the #comments: 

```HOST=#hosting info (i.e. 0.0.0.0)
PORT=#port info (i.e. 5003)
OANDA_API_KEY=#oanda api key for practice acocounts
OPENAI_API_KEY=#openai api key
OANDA_TOKEN= #repeat same OANDA Api key for yaml file
YOUR_OANDA_USERNAME= #registered email 
ACCOUNT1=#oanada demo account number 1
ACCOUNT2=#oanada demo account number 2 (if any)
ACTIVE_ACCOUNT= #oanada demo account v20 compatible from 1 or 2 
```

1. Navigate to https://chat.openai.com. 
2. In the Model drop down, select "Plugins" (note, if you don't see it there, you don't have access yet).
3. Select "Plugin store"
4. Select "Install unverified plugin"
5. Enter in `https://live.forex-gpt.ai` since this is the URL the server is running on.

The plugin should now be installed and enabled! You can start with a question like "What is the eur/usd sentiment now, based on the past month daily candles using bid prices (don't comment on each candle just overall)" or revise your prompt accordingly. 

**Understanding the maximum message size and token-limit imposted by Chat GPT:**

The following prompts should work, as they scratch the upper threshold of the token limit per message, which is currently 32k tokens, based on the latest engine upgrade to Forex-Rates, switching `gpt-3.5-turbo-0301` to `gpt-4-32k-0314` so that you can query larger historical time-frames. 

**Sample prompts from the last hour of minute data to the last 60 months of month candle stick data:**

Try asking Forex-Rates these prompts:

* "What is the overall sentiment for the EURUSD currency pair using bid prices on ten-minute candles for the past ten hours, excluding volume data?"
* "What is the overall sentiment for the GBPUSD currency pair using bid prices on sixty-minute candles for the past sixty hours, excluding volume data?"
* "What is the overall sentiment for the USDCHF currency pair using bid prices on daily candles for the past sixty days, excluding volume data?"
* "What is the overall sentiment for the USDJPY currency pair using bid prices on weekly candles for the past sixty weeks, excluding volume data?"
* "What is the overall sentiment for the USDCAD currency pair using bid prices on monthly candles for the past sixty months, excluding volume data?"
* "What is the overall sentiment for the EURUSD currency pair using bid prices on daily candles for the past sixty days, excluding volume data, and tell me the starting prices on the first day and last candle price on last day for that period?" 
* "Based on ten-minute candles for the past nine hours using ask prices, what is the sentiment analysis for the EUR/USD currency pair? Please include the starting price, latest price, and describe the current trend leading up to the present."
* "Could you provide an in-depth sentiment analysis for the GBP/USD currency pair using the bid prices of sixty-minute candles over the past sixty hours? Please share the starting price, latest price, and explain the prevailing trend up to the present."
* "I'm interested in understanding the overall sentiment of the USD/JPY currency pair over the past sixty months using the bid prices of monthly candles. Kindly include the starting price, latest price, and elaborate on the current trend leading up to the present."
* "What does the sentiment analysis reveal for the USD/CHF currency pair ask prices based on daily candles over the past thirty days? Please provide the starting price, latest price, and offer insights into the prevailing trend up to the present."
* "Provide a comprehensive sentiment analysis for the AUD/USD currency pair using fifteen-minute candles for the past six hours of bid prices. Include the starting price, latest price, and discuss the current trend leading up to the present."


Here is some further examples: 

<img src="https://github.com/hatgit/forex-gpt/assets/5213035/f907108f-dc9b-4fa5-9521-b6bb2fbfad96" width="60%" height="auto">

 
Another example of interacting with the Chat-GPT in a way that will trigger the Forex-Rates plugin to elicit a response from the OANDA API, by asking:"what is the bid ask spread on the latest 1 minute candle from oanda" where it will default to using the eur/usd pair (alternativley you can ask for a supported currency in your prompt). 

<img src="https://github.com/hatgit/forex-gpt/assets/5213035/7098e22c-b26b-4a3d-8d55-8c7bd16a38d3" width="60%" height="auto">


## Here is a short video demonstrating the Forex-Rates plugin responding in real-time to a query: 

https://github.com/hatgit/forex-gpt/assets/5213035/4e029080-9b86-44fc-a3a1-b347045b1844




## Forex-Rates Plugin Flowchart

![Forex-GPT-plugin-flow-chart drawio](https://github.com/hatgit/forex-gpt/assets/5213035/85c42c3f-54b4-46f4-b107-c595b9d3e1fc)

## Overview of how Forex-Rates plugin works:

1. Imports necessary libraries and modules.

2. Configures Flask app and CORS settings.

3. Defines the following routes:

   - **"/generate" (POST)**
     - Takes a 'prompt' and 'temperature' from the request's JSON.
     - Generates text using OpenAI's Completion API with the specified 'prompt' and 'temperature'.
     - Returns the generated text as a JSON response.

   - **"/complete" (POST)**
     - Takes 'text' from the request's JSON.
     - Uses OpenAI's Completion API to complete the provided 'text'.
     - Returns the completed text as a JSON response.

   - **"/search" (POST)**
     - Takes a 'query' from the request's JSON.
     - Uses OpenAI's Completion API to generate a response to the query.
     - Returns the generated text as a JSON response.

   - **"/playground" (POST)**
     - Takes 'code' from the request's JSON.
     - Uses OpenAI's Completion API to generate a response to the code.
     - Returns the generated text as a JSON response.

   - **"/logo.png" (GET)**
     - Serves a logo image from the current directory.

   - **"/openapi.yaml" (GET)**
     - Serves an OpenAPI specification file from the current directory.

   - **"/.well-known/ai-plugin.json" (GET)**
     - Serves an AI plugin manifest file from the .well-known directory.

   - **"/prices" (GET/POST)**
     - Depending on the method, takes parameters from the request's JSON or arguments.
     - Checks if all required parameters are provided.
     - If not, returns a prompt message as a JSON response.
     - If yes, retrieves the price data from Oanda using the parameters.
     - Returns the price data as a JSON response.

   - **"/api/analyze" (POST)**
     - Takes parameters from the request's JSON.
     - If 'from_time' is not provided, calculates it as 2 days before the current time.
     - Analyzes the market using the parameters.
     - Returns the market sentiment as a JSON response.

4. Defines the OpenAIPlugin class:
   - Initializes the Oanda and OpenAI clients.
   - Defines methods to analyze the market and get Oanda candles.

5. Prints Oanda and OpenAI API keys.

6. Lists all available OpenAI engines and prints their IDs.

7. Runs the Flask app on host '0.0.0.0' and port '5003'.

8. Requires the user to point the Chat-GPT developer plugin interface to the localhost URL (i.e., `http://localhost:5003`).

9. The plugin is loaded into Chat-GPT and can be enabled.

10. User asks Chat-GPT for analysis or sentiment on a supported currency pair (i.e., EUR/USD) for a specific duration (i.e., 1 week) and time-series (daily interval), and the plugin triggers and formats the request to the broker API to retrieve prices and perform calculations as per the Main.py file (see flow chart below).

<img width="1587" alt="Main-dot-py-Application-flow-chart" src="https://github.com/hatgit/forex-gpt/assets/5213035/e009fe63-0e37-45e9-8e0b-b5e69d4fd574">


## Getting help

**Server status**
- Railway.app status https://https://status.railway.app/

**Open AI API resources:**

If you run into issues or have questions building a plugin, please join our [Developer community forum](https://community.openai.com/c/chat-plugins/20).
* https://chat.openai.com/?model=gpt-4-plugins
* https://platform.openai.com/docs/plugins/introduction
* https://chat.openai.com/

**OANDA API developer resources**: 

* https://github.com/hootnot/oandapyV20-examples
* https://github.com/oanda/v20-python-samples
* https://pypi.org/project/v20/
* https://developer.oanda.com/
* https://developer.oanda.com/rest-live-v20/introduction/
* https://developer.oanda.com/rest-live-v20/pricing-ep/#CurrentPrices
* https://developer.oanda.com/rest-live-v20/account-df/

## Major Currency Pairs
These are the most traded currency pairs in the world, representing the world's largest economies. They include:

- EUR/USD (Euro / United States Dollar)
- USD/JPY (United States Dollar / Japanese Yen)
- GBP/USD (British Pound Sterling / United States Dollar)
- USD/CHF (United States Dollar / Swiss Franc)
- AUD/USD (Australian Dollar / United States Dollar)
- USD/CAD (United States Dollar / Canadian Dollar)
- NZD/USD (New Zealand Dollar / United States Dollar)
- USD/MXN (United States Dollar / Mexican Peso)
- USD/HUF (United States Dollar / Hungarian Forint)
- USD/TRY (United States Dollar / Turkish Lira)
- USD/CNH (United States Dollar / Chinese Yuan)
- USD/PLN (United States Dollar / Polish Zloty)
- USD/DKK (United States Dollar / Danish Krone)
- USD/NOK (United States Dollar / Norwegian Krone)
- USD/SEK (United States Dollar / Swedish Krona)
- USD/HKD (United States Dollar / Hong Kong Dollar)
- USD/SGD (United States Dollar / Singapore Dollar)
- USD/CZK (United States Dollar / Czech Koruna)
- USD/ZAR (United States Dollar / South African Rand)
- USD/THB (United States Dollar / Thai Baht)


## Cross Currency Pairs
These pairs do not include the US dollar but include the major currencies like the Euro, the UK Pound, and Yen. Examples include:
- EUR/GBP (Euro / British Pound Sterling)
- EUR/AUD (Euro / Australian Dollar)
- GBP/JPY (British Pound Sterling / Japanese Yen)
- EUR/JPY (Euro / Japanese Yen)
- GBP/CHF (British Pound Sterling / Swiss Franc)
- GBP/CAD (British Pound Sterling / Canadian Dollar)
- EUR/CHF (Euro / Swiss Franc)
- AUD/JPY (Australian Dollar / Japanese Yen)
- CHF/JPY (Swiss Franc / Japanese Yen)
- EUR/CAD (Euro / Canadian Dollar)
- EUR/ZAR (Euro / South African Rand)
- EUR/NOK (Euro / Norwegian Krone)
- NZD/JPY (New Zealand Dollar / Japanese Yen)
- NZD/CAD (New Zealand Dollar / Canadian Dollar)
- NZD/CHF (New Zealand Dollar / Swiss Franc)
- AUD/CAD (Australian Dollar / Canadian Dollar)
- GBP/AUD (British Pound Sterling / Australian Dollar)
- GBP/NZD (British Pound Sterling / New Zealand Dollar)
- AUD/SGD (Australian Dollar / Singapore Dollar)
- AUD/CHF (Australian Dollar / Swiss Franc)
- AUD/HKD (Australian Dollar / Hong Kong Dollar)
- NZD/SGD (New Zealand Dollar / Singapore Dollar)
- NZD/HKD (New Zealand Dollar / Hong Kong Dollar)
- SGD/JPY (Singapore Dollar / Japanese Yen)
- HKD/JPY (Hong Kong Dollar / Japanese Yen)
- CHF/HKD (Swiss Franc / Hong Kong Dollar)
- TRY/JPY (Turkish Lira / Japanese Yen)
- CHF/ZAR (Swiss Franc / South African Rand)
- GBP/ZAR (British Pound Sterling / South African Rand)
- EUR/HKD (Euro / Hong Kong Dollar)
- GBP/HKD (British Pound Sterling / Hong Kong Dollar)
- EUR/CZK (Euro / Czech Koruna)
- CAD/JPY (Canadian Dollar / Japanese Yen)


## Cryptocurrency Pairs
OANDA also supports some cryptocurrency pairs like:

- BTC/USD (Bitcoin / United States Dollar)
- ETH/USD (Ethereum / United States Dollar)

Please note that the availability of currency pairs may depend on the region and the specific regulations applicable to forex trading in that region. It's always a good idea to check the OANDA API documentation or contact OANDA support for the most accurate and up-to-date information.

## Currency Conversion
The Forex-Rates plugin for Chat-GPT 4 can also make currency conversion calculations, such as by asking it to convert an arbitrary amount of one currency into another using the latest rates. For instance, asking "What is $163,765 in euros?" will return a result like seen in the screenshot below: 

<img width="568" alt="Screen Shot 2023-11-05 at 5 31 51 PM" src="https://github.com/hatgit/forex-gpt/assets/5213035/f18302e6-8baa-4b2c-a32a-3e31ea37a8b3">



## Disclaimer

**Risk Warning: Trading in currency markets involves substantial risk of loss and is not suitable for everyone.** The Forex Rates plugin provided in this repository is intended for informational purposes only and should not be considered as financial or investment advice. Before making any trading decisions, it is important to conduct thorough research, seek professional guidance, and fully understand the risks involved.

**No Warranty:** The Forex Rates plugin is provided "as is" without any warranties or guarantees. The authors and contributors of this repository do not make any representations or warranties, express or implied, regarding the accuracy, reliability, or completeness of the plugin or its suitability for any particular purpose.

**MIT License:** The Forex GPT plugin is released under the [MIT License](https://github.com/hatgit/forex-gpt/blob/main/LICENSE). Please refer to the [LICENSE](https://github.com/hatgit/forex-gpt/blob/main/LICENSE) file for more details.

By using the Forex-Rates plugin, you acknowledge and agree to the above disclaimer and understand the associated risks of currency market trading, and the limitations of large language models (LLMs) such as Chat-GPT which may produce inaccurate information about people, places, or facts. The authors and contributors of this repository shall not be held responsible for any losses or damages incurred as a result of using the plugin.

