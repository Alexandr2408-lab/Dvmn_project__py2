import smtplib
server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
server.login(shyrick98kuzin@yandex.com, 24Sanya08)
server.sendmail(shyrick98kuzin@yandex.ru, elenacuzina@yandex.ru, message)

letter = """\
From: shyrick98kuzin@yandex.ru
To: elenacuzina@yandex.ru
Subject: Приглашение!
Content-Type: text/plain; charset="UTF-8";

Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!\n\n%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя.\n\nКак будет проходить ваше обучение на %website%?\n\n→ Попрактикуешься на реальных кейсах.\nЗадачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей.\nЗадачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.\nВсе проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 
\nРегистрируйся → %website%  \nНа курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл."""

website = "https://dvmn.org/profession-ref-program/kerzhakof/74Zsr/"
friend_name = "Elena"
sender_name = "Alexandr"
letter = letter.replace("%friend_name%",friend_name)
letter = letter.replace("%my_name%",sender_name)
letter = letter.replace("%website%",website)
letter = letter.encode("UTF-8")
server.quit()

print(letter)