from sklearn.externals import joblib

def classify_utterance(utt):
    # load the vectorizer
    loaded_vectorizer = joblib.load('tfidf.pkl')

    # load the model
    loaded_model = joblib.load('ML_model.pkl')

    # make a prediction
    print(loaded_model.predict(loaded_vectorizer.transform([utt])))

classify_utterance("How to do")
classify_utterance("What is this")







# from bokeh.io import output_file, show
# from bokeh.models import ColumnDataSource
# from bokeh.palettes import GnBu3, OrRd3
# from bokeh.plotting import figure
#
# output_file("bar_stacked_split.html")
#
# fruits = ['Apples', 'Pears', 'Nectarines', 'Plums', 'Grapes', 'Strawberries']
# years = ["2015", "2016", "2017"]
#
# exports = {'fruits' : fruits,
#            '2015'   : [2, 1, 4, 3, 2, 4],
#            '2016'   : [5, 3, 4, 2, 4, 6],
#            '2017'   : [3, 2, 4, 4, 5, 3]}
# imports = {'fruits' : fruits,
#            '2015'   : [-1, 0, -1, -3, -2, -1],
#            '2016'   : [-2, -1, -3, -1, -2, -2],
#            '2017'   : [-1, -2, -1, 0, -2, -2]}
#
# p = figure(y_range=fruits, plot_height=350, x_range=(-16, 16), title="Fruit import/export, by year",
#            toolbar_location=None)
#
# p.hbar_stack(years, y='fruits', height=0.9, color=GnBu3, source=ColumnDataSource(exports),
#              legend_label=["%s exports" % x for x in years])
#
# p.hbar_stack(years, y='fruits', height=0.9, color=OrRd3, source=ColumnDataSource(imports),
#              legend_label=["%s imports" % x for x in years])
#
# p.y_range.range_padding = 0.1
# p.ygrid.grid_line_color = None
# p.legend.location = "top_left"
# p.axis.minor_tick_line_color = None
# p.outline_line_color = None
#
# show(p)