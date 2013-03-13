clf = DecisionTreeRegressor()
clf.fit(data.data, data.target)

predicted = clf.predict(data.data)

plt.scatter(data.target, predicted)
plt.plot([0, 50], [0, 50], '--k')
plt.axis('tight')
plt.xlabel('True price ($1000s)')
plt.ylabel('Predicted price ($1000s)')
