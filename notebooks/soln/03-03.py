#03-03.py
X, y = preprocess(data, shuffle=False, n_samples=1000, normalization=None)

from sklearn.manifold import Isomap
iso = Isomap(n_neighbors=15, n_components=3)
X_proj = iso.fit_transform(X)

three_component_plot(X_proj[:, 0], X_proj[:, 1], X_proj[:, 2], y, labels, trim_outliers=True)
