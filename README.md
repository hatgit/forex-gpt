
<img src="https://github.com/hatgit/forex-gpt/assets/5213035/c461f57b-d977-4c95-bc9f-de6abac01501" width="20%" height="auto">


# Forex-GPT.ai plugin quickstart

This is a quickstart guide for setting up and running the Forex-GPT OpenAI plugin, which integrates text analysis capabilities with the OANDA API for analyzing currency market data. If you do not already have plugin developer access, please [join the waitlist](https://openai.com/waitlist/plugins).

## Setup for Mac users

You will need the following API keys which can be obtained from their respective providers:

1) Open AI API key for developers:
2) OANDA API for for fxTrade demo account: 

rename the file `template.env` to `.env` and set the following variables by repalacing the #comments: 

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


To install the required packages for this plugin, run the following command:

```bash
pip install -r requirements.txt
```

To run the plugin, enter the following command:

```bash
python main.py
```

This should run the local server from within the terminal window that the above main.py comannd was run. Depending on your Python configuration version you may need to run:

```bash
python3 main.py
```


Once the local server is running:

1. Navigate to https://chat.openai.com. 
2. In the Model drop down, select "Plugins" (note, if you don't see it there, you don't have access yet).
3. Select "Plugin store"
4. Select "Develop your own plugin"
5. Enter in `localhost:5003` since this is the URL the server is running on locally, then select "Find manifest file".

The plugin should now be installed and enabled! You can start with a question like "What is the eur/usd sentiment now, based on the past month daily candles (don't comment on each candle just overall)" or revise your prompt accordingly. 

**Understanding the maximum message size and token-limit imposted by Chat GPT:**

The following prompts should work, as they scratch the upper threshold of the token limit per message, which is currently 32k tokens, based on the latest engine upgrade to Forex-GPT, switching `gpt-3.5-turbo-0301` to `gpt-4-32k-0314` so that you can query larger historical time-frames. 

**Sample prompts from the last hour of minute data to the last 60 months of month candle stick data:**

Try asking Forex-GPT these prompts:

* "What is the overall sentiment for the EURUSD currency pair using ten-minute candles for the past ten hours, excluding volume data?"
* "What is the overall sentiment for the GBPUSD currency pair using sixty-minute candles for the past sixty hours, excluding volume data?"
* "What is the overall sentiment for the USDCHF currency pair using daily candles for the past sixty days, excluding volume data?"
* "What is the overall sentiment for the USDJPY currency pair using weekly candles for the past sixty weeks, excluding volume data?"
* "What is the overall sentiment for the USDCAD currency pair using monthly candles for the past sixty months, excluding volume data?"


Here is some further examples: 

<img src="https://github.com/hatgit/forex-gpt/assets/5213035/f907108f-dc9b-4fa5-9521-b6bb2fbfad96" width="60%" height="auto">

 
Another example of interacting with the Chat-GPT in a way that will trigger the Forex-GPT plugin to elicit a response from the OANDA API, by asking:"what is the bid ask spread on the latest 1 minute candle from oanda" where it will default to using the eur/usd pair (alternativley you can ask for a supported currency in your prompt). 

<img src="https://github.com/hatgit/forex-gpt/assets/5213035/7098e22c-b26b-4a3d-8d55-8c7bd16a38d3" width="60%" height="auto">


## Here is a short video demonstrating the Forex-GPT plugin responding in real-time to a query: 

https://github.com/hatgit/forex-gpt/assets/5213035/4e029080-9b86-44fc-a3a1-b347045b1844




## Forex-GPT Plugin Flowchart

![Forex-GPT-plugin-flow-chart drawio](https://github.com/hatgit/forex-gpt/assets/5213035/85c42c3f-54b4-46f4-b107-c595b9d3e1fc)

## Overview of how Forex-GPT works:

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

## Minor Currency Pairs
These pairs do not include the US dollar but include the major currencies like the Euro, the UK Pound, and Yen. Examples include:

- EUR/GBP (Euro / British Pound Sterling)
- EUR/AUD (Euro / Australian Dollar)
- GBP/JPY (British Pound Sterling / Japanese Yen)

## Exotic Currency Pairs
These pairs include a major currency, paired with the currency of a developing economy, such as Brazil, Mexico, or South Africa. Examples include:

- USD/SGD (United States Dollar / Singapore Dollar)
- USD/HKD (United States Dollar / Hong Kong Dollar)
- USD/TRY (United States Dollar / Turkish Lira)

## Cross Currency Pairs
These pairs do not include the US dollar. Examples include:

- EUR/CHF (Euro / Swiss Franc)
- GBP/JPY (British Pound Sterling / Japanese Yen)
- AUD/CAD (Australian Dollar / Canadian Dollar)

## Cryptocurrency Pairs
OANDA also supports some cryptocurrency pairs like:

- BTC/USD (Bitcoin / United States Dollar)
- ETH/USD (Ethereum / United States Dollar)

Please note that the availability of currency pairs may depend on the region and the specific regulations applicable to forex trading in that region. It's always a good idea to check the OANDA API documentation or contact OANDA support for the most accurate and up-to-date information.


## Disclaimer

**Risk Warning: Trading in currency markets involves substantial risk of loss and is not suitable for everyone.** The Forex GPT plugin provided in this repository is intended for informational purposes only and should not be considered as financial or investment advice. Before making any trading decisions, it is important to conduct thorough research, seek professional guidance, and fully understand the risks involved.

**No Warranty:** The Forex GPT plugin is provided "as is" without any warranties or guarantees. The authors and contributors of this repository do not make any representations or warranties, express or implied, regarding the accuracy, reliability, or completeness of the plugin or its suitability for any particular purpose.

**MIT License:** The Forex GPT plugin is released under the [MIT License](https://github.com/hatgit/forex-gpt/blob/main/LICENSE). Please refer to the [LICENSE](https://github.com/hatgit/forex-gpt/blob/main/LICENSE) file for more details.

By using the Forex GPT plugin, you acknowledge and agree to the above disclaimer and understand the associated risks of currency market trading, and the limitations of large language models (LLMs) such as Chat-GPT which may produce inaccurate information about people, places, or facts. The authors and contributors of this repository shall not be held responsible for any losses or damages incurred as a result of using the plugin.

