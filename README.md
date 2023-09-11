# Asesor de Carreras Universitarias

Este código es un programa que utiliza técnicas de procesamiento de lenguaje natural (NLP) y aprendizaje automático para recomendar carreras universitarias basadas en las respuestas proporcionadas por un usuario a una serie de preguntas. El programa es parte de un sistema de asesoramiento vocacional que intenta sugerir carreras en función de las afinidades e intereses del usuario. A continuación, se describen los pasos del programa:

## Pasos del Programa

1. **Importación de bibliotecas:** El código comienza importando varias bibliotecas de Python, como `pandas` para el manejo de datos, `TfidfVectorizer` para la vectorización de texto, `RandomForestClassifier` para el modelo de clasificación, `LabelEncoder` para codificar etiquetas, `train_test_split` para dividir los datos en conjuntos de entrenamiento y prueba, y `cosine_similarity` para calcular la similitud coseno entre vectores.

2. **Definición de preguntas y respuestas:** Se definen una serie de preguntas relacionadas con los intereses y afinidades de un usuario. Las respuestas del usuario se almacenarán en la lista `respuestas_usuario`.

3. **Listas de carreras y características de carrera:** Se proporciona una lista ficticia de carreras universitarias (`carreras_tec_tijuana`) y características asociadas a cada carrera (`caracteristicas_carrera`). Estas características describen los aspectos principales de cada carrera.

4. **Creación de un DataFrame:** Se crea un DataFrame de pandas llamado `data` para almacenar las preguntas y las carreras relacionadas.

5. **División de datos:** Los datos se dividen en conjuntos de entrenamiento (`X_train`, `y_train`) y prueba (`X_test`, `y_test`) utilizando la función `train_test_split`. Esto se hace para entrenar y evaluar el modelo.

6. **Vectorización de texto:** Se utiliza TF-IDF (Term Frequency-Inverse Document Frequency) para convertir las preguntas de texto en representaciones numéricas que el modelo de aprendizaje automático pueda entender. Las representaciones TF-IDF se almacenan en `X_train_tfidf` y `X_test_tfidf`.

7. **Entrenamiento del modelo:** Se crea un modelo de clasificación Random Forest y se entrena con los datos de entrenamiento (`X_train_tfidf`, `y_train`).

8. **Interacción con el usuario:** El programa le pide al usuario que responda a las preguntas definidas anteriormente. Las respuestas del usuario se almacenan en la lista `respuestas_usuario`.

9. **Vectorización de las respuestas del usuario:** Las respuestas del usuario se vectorizan utilizando el mismo vectorizador TF-IDF que se usó para las preguntas.

10. **Cálculo de similitud:** El programa calcula la similitud coseno entre las respuestas del usuario vectorizadas y las características de cada carrera. Esto ayuda a determinar qué tan cercana es la afinidad del usuario con cada carrera.

11. **Recomendación de carreras:** Las carreras se ordenan en función de su similitud con las respuestas del usuario, y se muestran en orden descendente, comenzando con las carreras más similares.


