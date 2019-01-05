# pyliturgical

Library for getting liturgical information, such as color, for a date.

```python
>>> from pyliturgical import calendar
>>> from datetime import date
>>> calendar.lookup(date(2018, 12, 25))
('Christmas Day', 'white')
```
