# Manual
RESTfull API  Сервис терминологии 

1 Список всех справочников : api/schedules/

2 Спиcок справочников, актуальных на указанную дату: api/schedules/?date=yyyy-mm-dd

3 Элементы конкретного справочника текущей версии: api/elements/?schedule=%name

4 Элементы конкретного справочника указанной версии api/elements/?schedule=%name&version=%version

5 Валидация элементов справочника текущей версии: api/validate/?schedule=%name&code=%code&value=%value

6 Валидация элементов справочника указанной версии api/validate/?schedule=%name&version=%version&code=%code&value=%value
