﻿label story:
    stop music fadeout 1.0
    window hide dissolve
    pause 2.0
    
    show screen end1 with fade
    pause 5.0
    hide screen end1
    pause 2.0
    screen end1:
       text "19 декабря" yalign 0.5 xalign 0.5
    scene bg grocery 
    with dissolve_scene_full
    play music clubs
    "Хм, медленный день."
    "Медленные дни в круглосуточном магазине – отстой."
    "Особенно в качестве менеджера."
    "Я могу просто сидеть и заниматься бумажной работой."
    "Может быть, есть какие-нибудь распоряжения."
    "Но у меня есть целая неделя, чтобы исполнить их."
    "Если бы я сделал их сейчас, то потом мне было бы скучно."
    "Проблемы первого мира, скажу я вам."
    mc "Отстой."
    #show Sayori
    show sayori work happ cm oe at t11
    s om "Да ладно тебе, могло быть и хуже."
    s "До конца дня всего пара часов."
    mc "Легко сказать, стоять и ничего не делать – одно из твоих любимых занятий."
    s neut "Неправда."
    mc "Я работаю с тобой, могу подтвердить это."
    s happ "Может, если бы ты работал побольше, то не заметил, что я не работаю."
    mc "Я менеджер, моя работа – следить за тем, чтобы ты выполняла свою работу."
    mc "Что ты зачастую не делаешь."
    s pout md "Хмф."
    s om "Злюка."
    mc "Продолжишь дуться, и я поставлю тебя на ночную смену."
    s nerv ce om "Беру свои слова назад."
    mc "Я так и думал."
    show sayori neut oe
    mc "Так чем ты занята сегодня вечером?"
    s "Ничем особенным, просто вернусь домой и займусь вечерней рутиной."
    s happ "Ужин, дела с котом и просмотр телевизора."
    mc "Не понял про тему с котом."
    s angr "Коты тоже умеют гулять!"
    mc "Это странно!"
    s "Ты странный!"
    mc "Может и так, но это не делает выгул кота не странным."
    s anno "Мистер Миттенс не считает это странным."
    mc "У Мистера Миттенса нет права голоса."
    s happ "В любом случае, что насчёт тебя?"
    s "Есть весёлые планы на вечер?"
    mc "Не, просто тихая ночь с семьёй."
    s "То, что она тихая, не значит, что она не может быть весёлой."
    mc "Я сказал тихая, но к слову, у меня шестилетний ребёнок."
    mc "Такое редко бывает тихим."
    s ce "Она прелестная."
    mc "Она такая, просто поменьше, когда я устаю."
    s oe "Я уверена, что не всё так плохо."
    mc "Я бы не сказал, что это плохо."
    mc "Иногда непросто не отставать."
    s "Оно того стоило."
    mc "Да, ты права."
    s nerv "......Ты же на самом деле не собирался переводить меня в ночную смену, не так ли?"
    mc "Естественно, нет."
    mc "Особенно после последнего раза."
    "Её напугал енот, она заперла двери и всю ночь пряталась в моём кабинете."
    "Да, больше никогда." #have Sayori look away embarassed in the background
    #fade out, fade in
    scene bg grocery 
    with fadehold
    "Хорошо, почти на месте."
    "Просто осталось дождаться, пока чел на ночной смене придёт сюда."
    "Который является болью в заднице, потому что он всегда появляется минута в минуту."
    "Клянусь, он, должно быть, специально ждёт снаружи."
    "Один из тех парней, который «Мне не платят за то, чтобы я приходил раньше»."
    #show Sayori again, winter outfit
    show sayori winterwork happ cm oe at t11
    mc "... Я вижу, тебе тоже не терпится уйти."
    s ce "Агась!"
    mc "Тебе везёт, что твой босс достаточно добродушен, чтобы не ругать тебя за то, что ты собралась свалить пораньше."
    s oe "Я вполне уверена, что он меня не уволит."
    mc "Ага."
    mc "Кстати, не слишком ли холодно, чтобы выгуливать кота?"
    s ce "Нет, у него есть одежда и ботинки!"
    mc "Хм-м-м, ну ладно тогда."
    show sayori oe at t22
    #show chad mc
    show chadmc turned casual happ cm oe at t21
    
    c "Эй, начальник!"
    c "Как дела?"
    mc "Добрый вечер, Чед, все хорошо."
    mc "Я вижу, у тебя снова нет униформы."
    c "Говорю тебе, без неё будет легче ловить магазинных воров."
    mc "Ты буквально большую часть времени стоишь за кассой."
    c curi mb "Может быть, я клиент, который заблудился."
    show chadmc ma
    mc "..."
    mc "Подожди, ты пришёл сюда только в этом?"
    c happ om oe "Да, я живу, наверное, в 15 минутах ходьбы отсюда."
    c "Кроме того, подвергая себя воздействию природы, ты укрепляешь свой иммунитет."
    mc "Я вполне уверен, что оно не так работает."
    c "Это не то, что говорится в Интернете."
    mc "...Короче, неважно."
    mc "Ладно, мы расходимся, спокойной ночи."
    s "Пока, Чед!"
    c "Ещё увидимся!"
    "...Тебе так повезло, что ты единственный, кто хочет работать ночью."
    #fade out
    stop music fadeout 1.0
    
    scene bg sayo_house_night_snow
    show snow
    play music snowyjazz
    with fadehold
    show sayori winterwork happ cm oe at t11
    s "Спасибо, что провёл меня до дома."
    mc "Без проблем, мне всё равно по пути."
    mc "Ты уже переехала на верхний этаж?"
    s neut "Нет, всё ещё в подвале."
    s happ "Но как только люди наверху съедут, я, скорее всего, заберу квартиру."
    mc "Это хорошо, подвальные квартиры – отстой."
    s neut "Ты говоришь это мне."
    s "Тебе везёт, у тебя есть дом."
    mc "Ну, это и хорошо и плохо."
    mc "Больше комнат – больше счетов."
    s happ "Да, логично, в любом случае, увидимся завтра?"
    mc "Нет, завтра я уезжаю, так что будешь только ты."
    s "Ладно, тогда увидимся через день."
    mc "Конечно, пока, Сайори."
    s ce "Пока!"
    show sayori at thide
    hide sayori
    "А теперь добраться домой одному, здесь чертовски холодно."
    #fade out
    
    scene bg house_snow_night with fadehold
    show snow
    
    "Тепло, слава богу."
    "...Пахнет вкусненько."
    "Не терпится выяснить, что так пахнет."
    stop music fadeout 1.0
    play music sayo_gaze
    
    scene bg kitchen with fade
    show monika forward_casual happ cm oe at t11
    mc "Чем так вкусно пахнет?"
    m "Ох! Привет, дорогой."
    show monika ce at h11:
       ease .3 zoom 3.8 yoffset 1900 
    #hug/kiss
    window hide dissolve
    pause 2.0
    show monika at h11:
       ease .5 zoom 1.0 yoffset 0
    m oe "Я не слышала, как ты зашёл."
    mc "Да, я скрытный."
    mc "Так, что же готовится?"
    m "Терияки из лосося."
    mc "Чудесно!"
    mc "Где малышка?"
    m "Наверху в своей комнате."
    m "Вообще-то, ужин почти готов, не мог бы ты сходить за ней?"
    mc "Конечно."
    
    scene bg altbedroomnight with fade
    show miyuki casual e7 at t11
    
    mc "Мию? Ужин почти готов."
    mm m2 "О, привет, папа!"
    mm e4 "Сейчас закончу рисовать, и спущусь."
    show miyuki m10
    mc "А что ты рисуешь?"
    mm e7 m3 "Чиби кролика."
    show miyuki m10
    mc "Звучит очаровательно."
    mm e4 m2 "Он реально миленький!"
    mm e7 m4 "Но он ещё не доделан, так что не смотри."
    show miyuki m10
    mc "Хорошо, хорошо, только спустись, как закончишь."
    mm e4 m2 "Обязательно!"
    
    scene bg kitchen with fade
    
    show monika forward_casual happ cm oe at t11
    mc "Она скоро спустится."
    m "Отлично."
    m "Ну, как поработал?"
    mc "Скучно, рад, что закончилось."
    m rhip laug mb "Оу, ну, по крайней мере, завтра у тебя выходной."
    show monika ma
    mc "Да, это уже что-то."
    m happ om "Как Сайори?"
    mc "Сайори-Сайори, ты и сама знаешь, как она."
    mc "Боже, я клянусь, у этой девушки в голове парк развлечений, куда она сбегает."
    mc "Я имею в виду, никогда не видел, чтобы кто-то выглядел таким весёлым, ничего не делая."
    m rdown neut "Может быть, но она всегда такая."
    mc "Я знаю, но временами это сбивает меня с толку."
    mc "И в такие дни, как этот, я немного ревную."
    m happ ce "А-ха-ха, ну что ж, теперь ты дома, не нужно сердиться."
    mc "Да, ты права."
    m neut oe "Ты уверен, что она придёт?"
    mc "Да, она просто рисовала кролика, или что-то такое."
    m happ "Мило."
    m "Ну, ужин готов, может, мне стоит позвать её."
    show monika at t21
    show miyuki casual e7 at t22
    mm "Всё в порядке, мама, я здесь."
    mc "Закончила свой рисунок, Мию?"
    mm "Да, но мне не нравится, как он выглядит, поэтому я его выкинула."
    mm e4 "Я опять попробую завтра."
    mm e7 "А что на ужин?"
    m "Лосось с обжаренными овощами."
    mm e4 "М-м-м, люблю лосося."
    show miyuki e7
    m ce "Он очень полезен для твоего здоровья, так что рада слышать."
    show monika oe
    mc "Да, ты бы могла быть как твоя тётя Сайори, и любить сладости."
    mm back m4 "Ну, я люблю сладости, но от большого количества мой животик болит."
    show miyuki cm
    mc "Урок, который тётя до сих пор не усвоила."
    mm e4 "Тётя Сайори глупышка."
    mc "И вправду."
    show miyuki neutral
    m rhip "М-м-м, милая, разве ты не хотела кое о чём спросить папу?"
    mm e7 m4 "Я?"
    show miyuki m9
    m rdown "Кхм, мы говорили об этом ранее."
    mm m2 e6 "...А, да!!"
    show monika rdown
    mm om e7 back "Папа, мы можем устроить Рождественскую вечеринку в этом году?"
    mc "Вечеринку?"
    mm e4 "Да! С декорациями, едой и всяким разным!"
    mc "Ах-х-х...."
    mm e7 m4 b2 "Пожалуйста-а-а!?"
    show miyuki m9
    mc "Я не очень уверен."
    mm b1 m3 "Я могу помочь с декорациями и всяким разным!"
    mm b2 m4 "Ну же, папа, пожалуйста?"
    show miyuki m9
    mc "Эм-м-м... что думает мама?"
    m lpoint rhip "Оно должно быть будет весёлым, мы могли бы пригласить Сайори, Юри и Нацуки, может быть, даже мою маму."
    show monika ldown
    mc "Хм-м-м, ну может быть."
    m ce "Что ж, я полностью за, но я сказала ей, что мы оба должны согласиться."
    show monika oe
    mc "Вот что я тебе скажу, Мию, папа сегодня немного устал, но я подумаю об этом и дам тебе знать завтра, хорошо?"
    mm m4 neutral "Звучит как нет..."
    show miyuki m9 neutral
    mc "Миюки..."
    mm m8 b3 "Хорошо..."
    mc "Отлично."
    show miyuki m9 b1 
    mc "Как в школе?"
    mm m4 "Всё здорово."
    mm om "На самом деле, мы мало что сделали сегодня, не считая нескольких игр, потому что это был последний день перед каникулами."
    mc "Что ж, звучит весело."
    mm e4 "Потому что и вправду было весело!" #лишняя запятушка
    mm e7 "Я ничего не выиграла, но мне всё равно было весело."
    m ce "В этом и смысл, милая."
    show monika oe
    mm "Да, я знаю."
    mm "Ладно, я закончила есть, могу я пойти поиграть?"
    m neut "Ты не желаешь десерта?"
    mm b2 "Я объелась, может, позже."
    m happ "Ладно, ты можешь пойти поиграть."
    show miyuki at thide
    hide miyuki
    show monika at t11
    mc "У тебя есть десерт?" #fadeout miyuki during this line
    m rhip "Нет, я просто собиралась угостить её мороженым или ещё чем-нибудь."
    m rdown "Но тебе тоже можно."
    mc "Здорово, спасибо, мам."
    m ce "Всегда пожалуйста." #gleeful
    mc "Ага."
    m oe "Прошло столько лет, а тебя всё ещё легко дразнить."
    mc "Ты продолжаешь меня шантажировать, ха-ха-ха."
    m rhip "Что могу сказать? Это весело."
    m rdown neut "Кстати, о веселье, что ты думаешь о том, чтобы устроить вечеринку?"
    mc "Я думаю, у нас осталось мало времени, и мы понятия не имеем, сможем ли мы успеть."
    m rhip "Но-о-о?..."
    mc "Но я не против этой идеи."
    m happ ce rdown lpoint "Так давай же займёмся этим!"
    show monika ldown
    mc "Мы можем, но я думаю, на всякий случай, было бы лучше посмотреть, кто сделает это первым." #либо обе запятые, либо без запятых вообще
    show monika oe
    mc "Я не хочу, чтобы она расстроилась, если никто не сможет."
    m "Что ж, наверное, ты прав."
    mc "Дорогая, это не похоже на вечеринку, это семейная посиделка с декорациями."
    m neut "На этом и остановимся."
    m happ "Ну, кого мы можем позвать?"
    mc "Всех, кого ты упомянула ранее, кроме твоей матери."
    m anno e1a "Что? Почему?"
    mc "Потому что твоя мать не приходит ни на одну вечеринку, которую я устраиваю."

    m "{i}Мы{/i} устраиваем, и это всё ещё не ответ на мой вопрос."
    mc "Потому что твоя мать – зануда!"
    mc "Она не любит меня!"
    m "Дело не в тебе, а в нашей дочке, которую она очень сильно любит."
    m "К тому же, тебе не придётся пить, потому что на вечеринке не будет алкоголя."
    mc "Ты правильно сказала, без алкоголя, а это значит, что твоя мама не придёт."
    m angr oe "Эй!"
    mc "Я прав."
    mc "Эта женщина – алкоголичка."
    m "Неправда."
    mc "Если будет вечеринка, то она должна быть такой, где я не буду спорить с кем-то настолько самовлюблённым."
    mc "Если это произойдёт, твоей матери придётся уйти."
    mc "Я не пытаюсь быть уродом, я пытаюсь предотвратить конфликт до того, как он произойдёт." #это фемили френдли мод, так что без единого мата блятб пожалуйста
    m anno "...допустим."
    m neut "Тогда только Сайори, Юри и Нацуки?"
    mc "Звучит здорово."
    mc "Чтобы доказать, что я не плохой парень, я могу сводить Миюки к бабушке пораньше ненадолго."
    m happ ce "Благодарю."
    m oe "Она это оценит."
    mc "Я сказал, что могу, но посмотрим, когда наступит день."
    mc "И всё же, что нам нужно для вечеринки?"
    m neut "Ну, это же Рождественская вечеринка, это будет просто, но надо бы сделать список."
    mc "...И сколько это всё будет стоить?"
    m happ "У нас достаточно денег, не думай об этом."
    mc "Легко сказать, ты не работаешь в круглосуточном магазине."
    m anno rhip "Нет, не работаю, и я говорю тебе, что это не тот разговор, который я хочу вести."
    m ce "Да, я зарабатываю больше, чем ты, но для меня это не имеет значения."
    m neut oe rdown "Главное для меня – благополучие нашей семьи."
    mc "По крайней мере, в этом мы можем согласиться."
    m happ "Точно, а остальное бессмысленно."
    "Легко сказать, тяжело не чувствовать."
    "Но не время для этого."
    mc "Хорошо, тогда давай составим список."
    mc "Давай сначала пройдём в зал, я хочу поваляться на диване."
    m "Отлично, тогда я схожу за ручкой и листком на верх."
    #fade out
    stop music fadeout 1.0
    
    scene bg living_room_night with fadehold
    
    play music chillvibes
    "Неделя, чтобы собрать это всё."
    "Должно быть, это будет весело."
    "Сначала нужно узнать, смогут ли прийти люди."
    "Я уверен, что Сайори точно придёт, но насчёт Юри и Нацуки не знаю, так что надо бы узнать."
    "Не мешало бы пригласить ещё пару человек, чтобы это стоило того."
    #show moni
    show monika forward_casual happ cm oe at t11
    m "Хорошо, давай представим, что нам нужно."
    mc "Ты знаешь, кого ещё мы можем пригласить?"
    m neut md "М-м-м?"
    show monika md
    mc "Я просто задумался, кого ещё мы можем пригласить."
    mc "Если мы собираемся потратиться на это, было бы хорошо собрать побольше людей."
    m om "Хорошо подмечено."
    m happ "Я думаю, я бы могла пригласить свою подругу по кофе."
    mc "Котоноха?"
    m "Кто же ещё?"
    mc "Не знаю, у тебя должно быть, много друзей."
    m neut "Фальшивых друзей, ты имеешь в виду."
    m happ "Я сократила их до нескольких настоящих."
    mc "А."
    mc "Что ж, не помешает спросить её."
    mc "Я могу позвать брата, у него всё равно нет занятий получше."
    m anno "Он всё ещё безработный?"
    mc "Ага."
    m "Разве ты не можешь устроить его в магазин?"
    mc "Нет времени, а даже если бы и было, я люблю своего брата, но не настолько, чтобы видеть его столь часто."
    m ce "Это плохо."
    show monika oe
    mc "Это братские отношения, тебе не понять."
    mc "В любом случае это только 2 дополнительных человека, кого ещё можно?"
    m neut "У меня никого, насколько я понимаю."
    mc "У меня тоже, но, если у всех получится, этого должно быть достаточно."
    mc "Теперь вернёмся к нашему списку."
    m "Да, во-первых, нам нужна ёлка."
    mc "Отлично, не должно возникнуть проблем с этим."
    m anno "Говорит тот, кто ещё ничего не купил."
    mc "Я был занят!"
    show monika neut
    mc "Не беспокойся, я возьму ёлку в ближайшее время."
    m happ "Отлично."
    m neut "Нужны ещё украшения на ёлку, и ещё хотя бы в гостиной."
    mc "Было бы здорово, не думаю, что остальную часть дома нужно украшать."
    mc "Думаю, нам ещё нужна еда."
    m happ "Конечно, нам нужна гора закусок и напитков для вечеринки."
    mc "Я могу купить большинство в торговом центре, но тебе придётся расписать."
    m ce "Могу заняться этим прямо сейчас."
    mc "Прекрасно."
    show monika neut oe
    #phone ringtone
    mc "М-м-м?"
    mc "Чёрт подери, почему он звонит?"
    show chadmc turned casual happ cm oe at t31 zorder 2
    show grocerysplit behind chadmc zorder 2
    show monika behind grocerysplit
    mc "Привет?"
    c "Привет, начальник!"
    mc "Ты же понимаешь, что время ночи не самое подходящее?"
    c "Да, я знаю и сильно извиняюсь, но у меня очень важный вопрос."
    mc "Х-х-х, что такое?"
    c "Ладно, типа, я проверял просроченные продукты, и нашёл кое-что."
    c neut "Мой вопрос такой, могу ли я забрать это домой?"
    mc "Что? Нет, естественно нет."
    c "Но оно просрочено, мы бы всё равно выбросили бы."
    mc "Нет."
    c "Это пустая трата времени, это даже не похоже на плохое."
    mc "Меня не волнует, это против правил компании, так что нет."
    mc "Если ты уйдешь с чем-нибудь из этого, ты уволен."
    c "Хорошо, хорошо, не нужно перегибать палку."
    c happ "Я просто выброшу это, как обычно."
    mc "Я проверю камеры, чтобы удостовериться в этом."
    mc "Я вешаю трубку."
    c "До встречи, начальник."
    show chadmc at thide
    hide chadmc
    show grocerysplit at thide
    hide grocerysplit
    
    mc "Этот парень так меня раздражает."
    m happ "По крайней мере, вовремя. Пока ты говорил, я составила список."
    mc "Ни один звонок от него никогда не бывает вовремя."
    
    scene bg entrance_night with fade
    #show Miyu pjs
    show miyuki pajama m9 at t11
    mc "В любом случае, я думаю, я возьму Мию, чтобы поспрашивать каждого."
    show miyuki e4 cm
    miyu "Да-а-а-а."
    show miyuki e7
    m "Мы не можем просто позвонить им?"
    show miyuki b3 m9
    #show annoyed
    mc "Не, я думаю, она хочет спросить у них лично, плюс я могу выполнить несколько поручений по пути."
    #show gleeful
    show miyuki e7 b1 cm
    mc "Я могу сначала зайти к Нацуки, потом к Юри, и наконец, спросить Сайори на работе."
    mc "Ты можешь позвонить своим друзьям, а я напишу брату завтра."
    m "Звучит как хороший план."
    mm e4 "{size=12}Да, это так.{/size}" #small writing
    mc "Пойду посмотрю, не спит ли она ещё, скажу ей, что я разбужу её довольно рано."
    mm m4 e7 "О-оу."
    
    scene bg living_room_night with fade
    show monika forward_casual happ cm oe at t11
    mc "Если она ещё не спит, я уложу её спать, и потом мы можем посмотреть фильм, или заняться ещё чем-нибудь."
    m "Хорошо, любимый."
    
    scene bg entrance_night with fade
    
    "Хм... клянусь, что только что слышал шаги надо мной."
    "Она подслушивала?"
    
    scene bg hallway with fade
    
    "Из её комнаты ничего не слышно."
    "Но я знаю, как справиться с этим."
    
    scene bg altbedroomdark with fade
    
    show miyuki pajama e5 m10 at t11
    "..."
    mc "Миюки, ты уже уснула?"
    mm "..."
    mm om "{size=12}Да-а-а...{/size}" #small writing
    mc "А ты знаешь, что спящие люди не могут ответить на этот вопрос?"
    mm b2 "{size=12}...Наверно?{/size}" #small writing
    mc "Я знаю, что ты не спишь, дорогая."
    #show Miyuki
    mm om e7 "Окей, я не сплю, но я пыталась!"
    mm e4 b1 "Я очень жду завтрашнего дня!"
    mc "Ох, ты слышала про него."
    mm b2 e7 "Возможно, я подслушала с лестницы."
    mc "Да, мне показалось, что я слышал шаги, мисс скрытность."
    mm m4 "Прости."
    show miyuki m9
    mc "За что?"
    mm m4 "За шпионство."
    show miyuki m9
    mc "Хм, тебе не стоило подслушивать, но на этот раз я не злюсь."
    show miyuki b1 
    mc "В любом случае, я поднялся, чтобы сказать тебе об этом."
    mm m4 "Правда?"
    show miyuki m9
    mc "Ага, а ещё тебе нужно встать рано и быть бодрой."
    mm b1 om e4 "Окей!"
    show miyuki e7
    mc "Ты будешь приглашать гостей, как думаешь, ты справишься с этим?"
    show miyuki pose
    mm "Ты можешь положиться на меня, пап." #finger point
    show miyuki pajama neutral
    mc "Я знаю, а теперь вернись в кроватку."
    mm neutral b2 "Могу я немного почитать перед сном?"
    mm "Я ещё не хочу спать."
    mc "Хорошо, только немного, окей?"
    mc "Завтра тяжёлый день для нас."
    mm b1 e4 "Окей, папа, я клянусь."
    mc "Это моя девочка, спокойной ночи, Мию."
    mm e7 "Спокойной, папа, я люблю тебя!"
    mc "Я тоже тебя люблю, милая."
    #fadeout
    scene bg living_room_night with fade
    show monika forward_casual happ cm oe at t11
    m "Она всё ещё не спала?"
    mc "Ну, спала, но вообще-то не спала."
    mc "Она немного почитает, если ты хочешь пожелать ей спокойной ночи.."
    m ce "Конечно хочу, скоро вернусь." #fadeout monika after
    show monika at thide
    hide monika
    "Удивительно, как сильно Мию похожа на свою маму."
    "Наверное, это хорошо."
    "Слишком много моих генов, и ты вырастешь менеджером круглосуточного магазина."
    "На сегодня достаточно самобичевания."
    "Вздремну, пока Моника не вернётся."
    stop music fadeout 1.0
    return