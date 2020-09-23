# Gift Exchange maker 🎅 🎃 🎁 

Python script to generate a CSV list for a gift exchange.

## To run the script

The script takes a CSV of names as an argument of participants in the exchange to match with others.

Simply run `python run_gift_exchange_script.py -f PATH_TO_CSV_OF_NAMES`

### Troubleshooting

**Please use Python 3** as Python 2 has been sunsetted!

If you need to update your version of Python, I recommend [pyenv](https://github.com/pyenv/pyenv)

If not, you should be able to run [Homebrew](https://brew.sh/) if you have it! Simply run `brew install python`. This should default to python 3.

If you still have trouble after you've installed python 3, you may need to specifically call python 3 when you run your command, like so:

`python3 run_gift_exchange_script.py -f PATH_TO_CSV_OF_NAMES`

## Sample CSV generated:

```
sender,match_name,match_email
Jane Doe,MJF,MJF@example.com
John Doe,Jane Doe,janedoe@example.com
Johnny Appleseed,John Doe,johndoe@example.com
MJF,Boaty McBoatface,boaty@example.com
Boaty McBoatface,Johnny Appleseed,johnnyappleseed@example.com
```

The file will be named `gift-exchange-matches-TODAYS_DATE.csv` and will appear at the root of the folder where the script has been run from.

Running the script multiple times will simply overwrite the existing file.
