# pyliturgical

![](https://img.shields.io/circleci/project/github/pizen/pyliturgical.svg)
![](https://img.shields.io/codecov/c/github/pizen/pyliturgical.svg)
[![](https://img.shields.io/pypi/v/pyliturgical.svg)](https://pypi.org/project/pyliturgical/)
![](https://img.shields.io/pypi/pyversions/pyliturgical.svg)
![](https://img.shields.io/pypi/format/pyliturgical.svg)
![](https://img.shields.io/github/license/pizen/pyliturgical.svg)

**Library for getting liturgical information, such as color, for a date.**

Example:

```python
>>> from pyliturgical import calendar
>>> from datetime import date
>>> calendar.lookup(date(2018, 12, 25))
('Christmas Day', 'white')
```
