
<img src="https://github.com/hatgit/forex-gpt/assets/5213035/c461f57b-d977-4c95-bc9f-de6abac01501" width="20%" height="auto">


# Forex-GPT.ai plugin quickstart

This is a quickstart guide for setting up and running the Forex-GPT OpenAI plugin, which integrates text analysis capabilities with the OANDA API for analyzing currency market data. If you do not already have plugin developer access, please [join the waitlist](https://openai.com/waitlist/plugins).

## Setup for Mac users

You will need the following API keys which can be obtained from their respective providers:

1) Open AI API key for developers:
2) OANDA API for for fxTrade demo account: 

Each API key should be set as a local variable using the command: 

```bash
export OPENAI_API_KEY="your_api_key_here"
```

```bash
export OANDA_API_KEY="your_api_key_here"
```

Stored API key values can be modified using `nano ~/.zshrc`


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

The plugin should now be installed and enabled! You can start with a question like "What is the eur/usd sentiment now, based on the past month daily candles (don't comment on each candle just overall)" or revise your prompt accordingly. Here is an example: 

<img src="https://github.com/hatgit/forex-gpt/assets/5213035/f907108f-dc9b-4fa5-9521-b6bb2fbfad96" width="60%" height="auto">

 
Another example of interacting with the Chat-GPT in a way that will trigger the Forex-GPT plugin to elicit a response from the OANDA API, by asking:"what is the bid ask spread on the latest 1 minute candle from oanda" where it will default to using the eur/usd pair (alternativley you can ask for a supported currency in your prompt). 

<img src="https://github.com/hatgit/forex-gpt/assets/5213035/7098e22c-b26b-4a3d-8d55-8c7bd16a38d3" width="60%" height="auto">




## Forex-GPT Plugin Flowchart

![Forex-GPT-plugin-flow-chart drawio](https://github.com/hatgit/forex-gpt/assets/5213035/85c42c3f-54b4-46f4-b107-c595b9d3e1fc)


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


