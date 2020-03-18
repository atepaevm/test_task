# Получение финансовых данных

## Описание
Простой пример паттерна ETL. Рассмотрим модули подробнее.
* Extracter. Получает raw-html-страницу и сохраняет в директорию data/. Возвращает текст.
* Transformer. Переводит текст в pandas.DataFrame, проводит парсинг чисел, дат и текста. Использует регулярные выражения.
* Loader. Имитирует загрузку в СУБД.
Все модули можно запустить как main-код. В этом случае Extracter сохраняет данные в файл, Transformer берёт самый последний файл из data/, а поведение Loader остаётся неизменным.
##Артефакты
Запуск Tasker'а приводит к следующим артефактам:
* В директории data/ скачивается html-страничка
* В директории export/ появляются два xlsx-файла с данными

## Использование
Для корректного использования рекомендую установить пакеты из requirements.txt

## Особенности
* Код оформлен по PEP8
* Испольован логгер (см. директорию logs/). Каждую полночь файл переименовывается с добавлением метки времени.
* Использованы DataFrame из pandas для удобного подсчёта статистики

## Смотри также

Отсылаю к моей статье на Хабре: https://habr.com/ru/post/483356/

# Спасибо за внимание!