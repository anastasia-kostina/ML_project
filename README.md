# ML_project
Задача: найти клиентов магазина "Лента", рассылка которым рекламного предложения
приведет к совершению покупки (uplift-моделирование). Датасет входит в пакет  sklift. 

Используемые признаки:
gender ('М'/'Ж')
age (float64)
main_format (0/1)
children (float64) 
crazy_purchases_goods_count_6m (float64)
k_var_cheque_group_width_15d (float64)
promo_share_15d (float64)

Модель: Solomodel


Создание образа:
docker build -t mypythonapp .

Запуск контейнера:
docker run -d -p 5000:5000 mypythonapp
