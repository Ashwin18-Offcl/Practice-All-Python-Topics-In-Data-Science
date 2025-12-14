# Wine Dataset ML Model Comparison
# This Jupyter Notebook evaluates multiple ML models on the Wine dataset and selects the best one based on accuracy

# %% [markdown]
# ## Introduction
# This notebook demonstrates the evaluation of multiple machine learning algorithms on the Wine dataset using Python's scikit-learn library. The goal is to compare model accuracies and select the best performing algorithm.

# %%
# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC

# %% [markdown]
# ## Load and Preprocess Data
# Load the Wine dataset and standardize features for better performance in algorithms like KNN and SVM.

# %%
# Load Wine dataset
wine = load_wine()
X = wine.data
y = wine.target

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# %% [markdown]
# ## Define and Evaluate Models
# We will compare six algorithms: Logistic Regression, KNN, Decision Tree, Random Forest, Gradient Boosting, and SVM using 10-fold cross-validation.

# %%
# Define models to compare
models = []
models.append(('Logistic Regression', LogisticRegression(max_iter=1000)))
models.append(('KNN', KNeighborsClassifier()))
models.append(('Decision Tree', DecisionTreeClassifier()))
models.append(('Random Forest', RandomForestClassifier()))
models.append(('Gradient Boosting', GradientBoostingClassifier()))
models.append(('SVM', SVC()))

# Evaluate each model using cross-validation
results = []
names = []
seed = 42
kfold = StratifiedKFold(n_splits=10, shuffle=True, random_state=seed)

for name, model in models:
    cv_results = cross_val_score(model, X_scaled, y, cv=kfold, scoring='accuracy')
    results.append(cv_results)
    names.append(name)
    print(f"{name}: Mean Accuracy = {cv_results.mean():.4f}, Std = {cv_results.std():.4f}")

# %% [markdown]
# ## Visual Comparison
# We use a boxplot to compare the distribution of accuracy scores across models.

# %%
# Boxplot for algorithm comparison
plt.figure(figsize=(10, 6))
plt.boxplot(results, labels=names, showmeans=True)
plt.title('Algorithm Comparison on Wine Dataset (Accuracy)')
plt.ylabel('Accuracy')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# %% [markdown]
# ## Identify the Best Model
# Select the model with the highest mean accuracy from cross-validation.

# %%
mean_accuracies = [cv.mean() for cv in results]
best_index = np.argmax(mean_accuracies)
print(f"Best Model: {names[best_index]} with Accuracy = {mean_accuracies[best_index]:.4f}")

# %% [markdown]
# ## Conclusion
# Based on cross-validation results, the best performing algorithm on the Wine dataset is identified above. Further improvement can be done by hyperparameter tuning or ensemble methods.
