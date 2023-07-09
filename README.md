# fake-currency-detection
this project will provide banknote authentication, the model will predict is banknote is real or fake note 

## Install

This project requires **Python, jupyter notebook installed** and the following Python libraries installed:

- [NumPy](http://www.numpy.org/)
- [Pandas](http://pandas.pydata.org/)
- [seaborn](https://seaborn.pydata.org/)
- [matplotlib](http://matplotlib.org/)
- [scikit-learn](http://scikit-learn.org/stable/)
- [imblearn](https://imbalanced-learn.org/stable/)
- [Flask](https://flask.palletsprojects.com/)

## Usage

first, you can clone this git repository

```
git clone https://github.com/HillalXD/fake-currency-detection.git
```

then navigate your command to this directory

```
cd fake-currency-detection
```

after that run `app.py` to open flask webapp
```
python app.py
```

then on webapp browser url add `/apidocs`like this:
```
http://127.0.0.1:8000/apidocs
```


## Code 
- Template code is provided in the `classifier.ipynb` notebook file.
- `banknote.csv` is provide data source for training model
- `knearest.pkl` is classifier pickle file
- `app.py` is flask webapp file


