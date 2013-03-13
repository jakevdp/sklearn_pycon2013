from sklearn.decomposition import RandomizedPCA

X_rpca = RandomizedPCA(n_components=2).fit_transform(X)

plot_PCA_2D(X_rpca, iris.target, iris.target_names)
plt.title('Randomized PCA')

plot_PCA_2D(X_pca, iris.target, iris.target_names)
plt.title('PCA')
