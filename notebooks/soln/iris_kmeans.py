kmeans = KMeans(n_clusters=3, random_state=rng).fit(X)

plot_2D(X_pca, kmeans.labels_, ["c0", "c1", "c2"])
plt.title('K-Means labels')

plot_2D(X_pca, iris.target, iris.target_names)
plt.title('True labels')
