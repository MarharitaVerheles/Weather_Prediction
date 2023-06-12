# Weather_Prediction
Завдання з рефакторінгу:

Середьоквадратична похибка: 0.0586

![image](https://github.com/MarharitaVerheles/Weather_Prediction/assets/92088991/b93df06e-ff46-4870-816f-58e693499d56)

За допомогою API погоди складаємо датасет (csv file). Після цього навчаємо модель лінійної регрессії на цих даних. 
Координати брались по місту Харків.
В навчанні моделі враховували такі дані:
time - Час в який проводили виміри (дані беруться за кожну годину)
temperature_2m -  Температура повітря на висоті 2 метри над землею
relativehumidity_2m - Відносна вологість на висоті 2 метри над землею
surface_pressure - Атмосферний тиск повітря, приведений до тиску на поверхні. 
cloudcover - Загальна хмарність як частка площі
direct_radiation - Пряме сонячне випромінювання як середнє за попередню годину на горизонтальній площині 
diffuse_radiation - Розсіяна сонячна радіація в середньому за попередню годину
windspeed_10m - Швидкість вітру на висоті 10 метрів над землею
