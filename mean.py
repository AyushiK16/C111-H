import pandas 
import statistics
import random
import plotly.figure_factory as ff
import plotly.graph_objects as pg



df = pandas.read_csv('data.csv')
data = df['claps'].tolist()

#General Mean
mean = statistics.mean(data)
print('Mean : ', mean)

#Sampling Mean
samplingList = []

for i in range(0,100):
  l = []
  for j in range(0,30):
    l.append(random.choice(data))
  samplingList.append(statistics.mean(l))

samplingMean = statistics.mean(samplingList)
samplingStDev = statistics.stdev(samplingList)
print('Mean of Sample : ', samplingMean)

#Printing the mean in a graph
#figure = ff.create_distplot([samplingList], ['Sample Means'], show_hist=False)
#figure.show()


meanOfList = statistics.mean(samplingList)
devOfList = statistics.stdev(samplingList)
print('Mean of List: ', meanOfList)
print('StDev of List: ', devOfList)

figure = ff.create_distplot([samplingList], ['Maths Score'], show_hist = False )
figure.add_trace(pg.Scatter(x=[meanOfList, meanOfList], y = [0,0.005], name='Mean'))

devStart1 = meanOfList-devOfList
devEnd1 = meanOfList + devOfList

devStart2 = meanOfList- 2*devOfList
devEnd2 = meanOfList + 2*devOfList

devStart3 = meanOfList- 3*devOfList
devEnd3 = meanOfList + 3*devOfList

figure.add_trace(pg.Scatter(x=[devStart1, devStart1], y = [0,0.005], name='StDevStart1'))
figure.add_trace(pg.Scatter(x=[devEnd1, devEnd1], y = [0,0.005], name='devEnd1'))

figure.add_trace(pg.Scatter(x=[devStart2, devStart2], y = [0,0.005], name='devStart2'))
figure.add_trace(pg.Scatter(x=[devEnd2, devEnd2], y = [0,0.005], name='devEnd2'))

figure.add_trace(pg.Scatter(x=[devStart3, devStart3], y = [0,0.005], name='devStart3'))
figure.add_trace(pg.Scatter(x=[devEnd3, devEnd3], y = [0,0.005], name='devEnd3'))

figure.show()