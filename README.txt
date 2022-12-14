Проект "Телеграм-бот на фэнтезийную тематику"

Участники проекта:
- Бунин Илья (тимлид)
- Попов Роман
- Хоменко Андрей

Цель проекта: Создать многофункционального телеграм-бота, который будет выводить информацию
пользователям на интересующие их темы. А именно:
		- выводить на экран список интересующих фильмов;
		- выводить на экран список интересующих игр (компьютерных и настольных);
		- отправлять файлы с информацией о случайном персонаже/множестве персонажей;
		- показывать информацию о боте.

Реализация и функционал проекта:
	Весь функционал бота реализован через кнопки.
	Кнопка "Во что поиграть???" отправляет боту аналогичное сообщение,
		на что он отвечает выводом списка игр с ссылками на ресурс,
		где их можно приобрести и обложки игр.
	Кнопка "создание персонажа" отправляет боту аналогичное сообщение,
		на что он отвечает сообщением с тремя кнопками, нажатие на которые запускает
		генерациию и отправку пользователю выбранных файлов.
	Кнопка "что посмотреть?" отправляет боту аналогичное сообщение,
		на что он отвечает сообщением, в котором будут содержаться кнопки,
		которые имеют то же название, что и фильмы, ссылки на которые они содержат.
		Нажатив на эти кнопки, пользователь получает предложение перейти на страницу
		фильма в Кинопоиске или Википедии. В конце списка кнопок находится кнопка
		"Выберу сам!", который предлагает пользователю перейти по ссылке на Кинопоиск,
		где пользователь смодет выбрать фильм для просмотра самостоятельно.
	Кнопка "информация о боте" отправляет боту аналогичное сообщение,
		на что он отвечает текстовым сообщением с информацией о боте на английском
		(как самом популярном в мире) языке.

Запуск проекта на своем компьютере:

	- Скопировать на свой компьютер файлы из данного репозитория
		(если вы нашли данный тесктовый документ вне GitHub, то ссылку на репозиторий
		можете скопировать ниже:
			"https://github.com/Elijahbunn/DZ_02.12.22")

	- Установить на свой компьютер библиотеки для работы с телеграм-ботами - telebot.
		Ссылка на подробную инструкцию по устновке данной библиотеки ниже:
			https://habr.com/ru/post/580408/
		Еще две библиотеки, которые используются в проекте (creat_bot, logging) не потребуют
		отдельной установки.

	- Открыть папку со скаченным репозиторием в своей среде разработки;
	- Прописать в терминале комманду "python ./bot.py" и нажать "Enter";
	- Теперь бот работает. Перейдите в Telegram, найдите там нашего бота @our_fantasy_bot.
	- Наслаждайтесь функционалом :)

Примечания тимлида:
	- Не реализовали venv-пространство в данном проекте, т.к. у каждого из участников
		проекта возникали с этим проблемы "от мала до велика", на решение которых
		ни у кого из нас не хватило времени. Постараемся реализовать в следующем проекте.
	- Разбивки на модули кода с функциями для работы с кнопками также не были реализованы,
		т.к. в библиотеке telebot все функции реализованы через декораторы, а их синтаксис
		я (тимлид) изучил только сейчас, то разбить приложение на модули я не успел.
