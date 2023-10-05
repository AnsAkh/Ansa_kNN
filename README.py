# Ansa_kNN
kNN
from sklearn.neighbors import KNeighborsClassifier

# Оқу деректер жинағын жасаңыз
# Бізде жемістердің салмағы мен түсі туралы мәліметтер бар деп елестетіп көрейік
# Салмақ граммен өлшенеді, түс сандармен кодталады (мысалы, қызыл үшін 0 және Жасыл үшін 1)
X_train = [[300, 0], [200, 0], [150, 1], [500, 1]]
y_train = ['алма', 'алма', 'алмұрт','алмұрт']

# Жақын көршілердің әдіс классификаторының данасын жасаңыз
knn = KNeighborsClassifier(n_neighbors=3)

# Модельді оқыту деректер жиынтығында оқыту
kn.fit(X_train, y_train)

# Енді бізде оқытылған модель бар және оны жаңа жемістерді жіктеу үшін пайдалана аламыз

# Белгісіз класы мен сипаттамалары бар жаңа жеміс жасаңыз
new_fruit = [[250, 0]] # жемістің салмағы 250 грамм және қызыл (0)

# Жаңа жеміс класын болжау
predicted_class = knn.predict(new_fruit)

print ("жаңа жемістің болжамды класы:", predicted_class[0])
