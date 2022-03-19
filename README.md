# :globe_with_meridians: Geography Quiz Chatbot

## Synopsis

*Geography Quiz Chatbot* is a chatbot where users can play :cityscape: _Guess the capital_ (given a country the user must select the correct capital from a range of choices) or :world_map: _Guess the country_ (given the outlines of a country the user must select the correct country from a range of choices). The questions will be delivered and checked by [Python](https://www.python.org/) Lambdas. The following short screen recording shows an interaction with the chatbot via [WhatsApp](https://en.wikipedia.org/wiki/WhatsApp).

[![Link to YouTube](screenshot.png)](https://www.youtube.com/watch?v=ZT8t0I6cvHI)

## Tech Stack

The chatbot is built on a variety of serverless cloud technologies, namely:

- [Twilio Autopilot](https://www.twilio.com/autopilot)
- [Twilio Messaging](https://www.twilio.com/messaging)
- [AWS Lambda](https://aws.amazon.com/lambda/)
- [Serverless Framework](https://www.serverless.com/)
- [Python](https://www.python.org/)

## Structure

The project is laid out like this:

```
├── autopilot
├── data
├── README.md
├── screenshot.png
└── serverless
```

`autopilot` contains the [Twilio Autopilot](https://www.twilio.com/autopilot) definitions. The main file is `schema.json` located under `autopilot/geography-quiz-chatbot/model`.

`data` holds the source files and images (the outlines of the countries) which are used in the geography questions. It also contains a Python script (`build-and-upload-images-v2.py`) to build the images.

`serverless` contains the Python Lambdas which ask and evaluate the questions.

## Usage & Development

...

## Deployment & Hosting

...