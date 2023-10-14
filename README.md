# Модель прогнозирования стоимости жилья для агентства недвижимости

Агентство недвижимости столкнулось с проблемой — риелторы тратят слишком много времени на сортировку объявлений и поиск выгодных предложений. Поэтому скорость их реакции и качество анализа не дотягивают до уровня конкурентов. Это сказывается на финансовых показателях агентства.

**Наша цель** — разработать модель машинного обучения, которая поможет обрабатывать объявления и увеличит число сделок и прибыль агентства.

## Данные
Описание данных следующее:

- `status` — статус продажи;
- `private pool` и `PrivatePool` — наличие собственного бассейна;
- `ropertyType` — тип объекта недвижимости;
- `street` — адрес объекта;
- `baths` — количество ванных комнат;
- `homeFacts` — сведения о строительстве объекта (содержит несколько типов сведений, влияющих на оценку объекта);
- `fireplace` — наличие камина;
- `city` — город;
- `schools` — сведения о школах в районе;
- `sqft` — площадь в футах;
- `zipcode` — почтовый индекс;
- `beds` — количество спален;
- `state` — штат;
- `stories` — количество этажей;
- `mls-id` и `MlsId` — идентификатор MLS (Multiple Listing Service, система мультилистинга);
- `target` — цена объекта недвижимости (целевой признак, который необходимо спрогнозировать).