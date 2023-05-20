﻿label story2:
    scene black
    with fadehold
    window hide dissolve
    pause 2.0
    
    show screen end2 with fade
    pause 5.0
    hide screen end2
    pause 2.0
    screen end2:
        text "20 декабря" yalign 0.5 xalign 0.5
    scene black
    with fadehold
    
    "..."
    mm "{size=12}Пап.{/size}" #small writing"
    "..."
    mm "{size=16}Пап?{/size}"
    "..."
    mm "Папа, просыпайся!!"
    mc "Хм-м...что?"
    scene bg living_room_day
    show miyuki casual at t11
    with fadehold
    play music chillvibes
    #open eyes, very close Miyu
    mc "Привет, Мию."
    mm "Привет, пап."
    mm e4 "Уже утро!"
    mc "Действительно."
    mm "Хе-хе-хе, глупый папа, ты заснул на диване."
    mc "...Так и есть, не так ли?"
    mm "Угу!"
    mm e7 "Но пришло время проснуться, с утра пораньше, как ты и сказал."
    mc "И то верно."
    "Кстати, который час?"
    "{i}8 утра.{/i}"
    "О, неплохо, не так рано."
    "Интересно, проснулась ли Моника."
    mc "Твоя мама ещё спит, Мию?"
    mm m4 "М-м-м, не знаю."

    mm m6 "Я проснулась и спустилась сюда, увидела, что ты спишь и разбудила тебя."
    show miyuki cm
    mc "Что ж, раз уж она ещё не спустилась, значит, скорее всего, спит."
    mc "Ну, как тебе идея приготовить ей завтрак в качестве сюрприза?"
    mm om "Давай! Маме это понравится!"
    mc "Тогда давай отправимся на кухню и посмотрим, что мы можем приготовить."
    
    scene bg kitchen with wipeleft
    show miyuki casual at t11
    mc "Хм-м-м, есть идеи?"
    mm e4 m2 "Блинчики!"
    show miyuki cm
    mc "Это потому, что они понравится ей, или ты хочешь их приготовить для себя?"
    mm e7 "И то, и другое."
    mc "Что мама, что дочь, ладно, блины так блины."
    mm e4 m2 "Ура!"
    show miyuki cm
    mc "Хорошо, тогда достань смесь из нижнего шкафчика, а я возьму яйца и молоко."
    mm e7 "Хорошо, пап."
    "Магазин сейчас открыт, может, мне стоило позвонить Сайори."
    "Ладно, яйца и молоко есть."
    mm "Вот и смесь, папа."
    mm "Можно я смешаю всё вместе?"
    mc "Конечно, милая, только я сначала добавлю молоко и яйца."
    "{w}.{w=0.1}{w}.{w=0.1}{w}.{w=0.1}" #separate dots
    mc "Вот, начинай."
    mc "Постарайся всё хорошо смешать."
    mm "Я знаю, тётя Нацуки говорит, что ты должен выбивать из этого всё дерьмо, когда взбиваешь что-то."
    mc "...Ну, тётя Нацуки не должна была говорить тебе выбивать дерьмо из всего подряд, но технически, она права."
    mc "Просто перемешивай, а когда перемешаешь, то приступим к готовке."
    mc "Пока ты будешь этим заниматься, папа быстро позвонит тёте Сайори."
    mm m4 "Ты же не собираешься рассказывать ей о вечеринке, правда?!"
    mm m2 e6 "Я хочу это сделать!!"
    show miyuki cm
    mc "Не волнуйся, ты можешь поговорить с ней об этом позже, мне просто нужно обсудить с ней кое-что."
    mm m4 e7 "Оу."
    mm om "Тогда хорошо."
    mc "А теперь, мисс, приступай."
    mm "Уже!"
    
    #*ringing*
    play audio dial
    window hide dissolve
    pause 7.0
    
    
    show sayori work neut cm oe at t31 zorder 2
    show sayosplit behind sayori
    s "Алло?"
    mc "Утречко, Сайори."
    s happ "О, привет, [player], что делаешь?"
    mc "Готовлю блины с Мию."
    s ce "Оу-у, как мило, передай ей трубку!"
    mc "Не могу, она занята смешиванием."
    s anno oe "Тогда включи громкую связь."
    mc "На это нет времени, это по поводу работы."
    s neut "Ох, что не так?"
    mc "На самом деле ничего особенного, просто сделай мне одолжение и посмотри записи с камер наблюдения прошлой ночью."
    mc "Мне нужно знать, взял ли Чед с собой домой просроченные вещи."
    s curi "Зачем ему это делать?"
    mc "Потому что это Чед."
    mc "В любом случае, если посмотришь, напиши мне, брал или нет, я был бы очень признателен."
    s happ "Конечно, я дам тебе знать."
    mc "Отлично, спасибо, Сайори."
    s "Нет проблем!"
    mc "В любом случае, я поговорю с тобой позже, мне нужно приготовить завтрак."
    s ce "Хорошо, пока!"
    show sayori at thide
    hide sayori
    show sayosplit at thide
    hide sayosplit
    mc "Ты закончила?"
    mm "Думаю, да."
    mc "Дай посмотрю...Да, ты отлично справилась."
    mc "Я начну жарить блины."
    mm "Я пойду накрою на стол." #fade out miyuki after
    show miyuki at thide
    hide miyuki
    mc "Звучит хорошо, готовка не займёт много времени."
    mm "Хорошо, потому что я очень голодна!"
    mc "Что ж, тебе придётся немного подождать, потому что сначала мы приготовим порцию для мамы."
    mm "Мы должны принести их ей в постель!"
     
    mc "Хорошая идея, завтрак в постели – это всегда приятно."
    mm "Надеюсь, она ещё не проснулась."
    mc "Не думаю, что это проблема, это займёт несколько минут."
    mm "Разве блины так быстро готовятся?"
    mc "Для одного человека – да, просто обычно я готовлю их дольше для нас троих."
    mm "Хм."
    #show Miyu
    show miyuki casual at t11
    mm "Эй, я могу налить ей стакан сока в дополнение к ним?"
    mc "Конечно, милая, ей это понравится." #fade out Miyu
    show miyuki at thide
    hide miyuki
    "Обычно она пьёт кофе, но это слишком мило, она может просто выпить его после."
    mc "Не могла бы ты сходить в гостиную за подносом?"
    mc "Мы принесём её завтрак на нём."
    mm "Пойду достану его."
    mc "Спасибо, Мию."
    "Хорошо, блины есть, сок есть, осталось дождаться дочь."
    "Они, наверное, смогут поболтать, пока я готовлю завтрак для Миюки и меня."
    "Хм, на улице довольно солнечно."
    "Надеюсь, там не слишком холодно."
    mm "Вот и он!"
    mc "Хорошая работа, теперь мы просто положим завтрак на поднос и принесём его ей наверх."
    mm "Могу я понести его?"
    mc "Как насчёт того, чтобы я понёс его вверх по лестнице, а потом оттуда понесёшь ты?"
    mm "Договорились."
    mc "Ладно, тогда пойдём разбудим маму."
    #fade out
    stop music fadeout 1.0
    
    scene bg bedroom with fade
    show miyuki casual at t22
    show monika pjs dist om ce at t21
    play music clubs
    mc "Тук-тук."
    mm "Обслуживание номеров!"
    m curi cm e4a "М-м-м?"
    m om "Обслуживание номеров?"
    mm e4 "Так точно, мама, мы приготовили тебе завтрак!"
    m neut ce mb "О? Вы сделали его сейчас?"
    show monika ma
    mm "Ага, блинчики!"
    mm e7 "И я помогала."
    #monika open eyes
    m happ oe om "Вау!"
    m "Выглядит потрясающе, милая."
    mm "Я замесила тесто и налила сок."
    m ce "Посмотрите на моего маленького поварёнка, ты собираешься составить конкуренцию тёте Нацуки."
    mm e4 "Возмо-о-о-ожно."
    m oe "Что ж, большое тебе спасибо, Мию, я уверена, что это будет вкусно."
    #moni kiss
    show monika ce at h11:
        ease .3 zoom 3.8 yoffset 1900 
    #hug/kiss
    window hide dissolve
    pause 2.0
    show monika at h21:
        ease .5 zoom 1.0 yoffset 0
    show miyuki e7
    m "И тебе тоже спасибо."
    mc "Награда стоила усилий."
    m ce n3 "О, прекрати это."
    mc "Я разве соврал?"
    mc "Да ни за что."
    m n4 b1b "Хва-а-атит!"
    mc "Ни за что!"
    #moni kiss again
    show monika ce at h11:
        ease .3 zoom 3.8 yoffset 1900 
    #hug/kiss
    window hide dissolve
    pause 2.0
    
    show monika at h21:
        ease .5 zoom 1.0 yoffset 0
    #end kiss
    show miyuki e3 m4 b3 behind monika
    mm "Фу-у-у, мерзость!"
    mm e7 m4 "Гадость."
    show miyuki m9
    m happ b1a n1 oe om "Это просто привязанность, дорогая, в этом нет ничего плохого."
    mm m4 "Это отвратительно!"
    show miyuki m9
    mc "Ха-ха-ха, ну, раз ты так говоришь, Мию, то ладно."
    show miyuki m9 b1 e7
    mc "Хочешь поболтать с мамой, пока я пойду готовить наш завтрак?"
    mm om "Окей."
    mc "Это не займёт много времени, я позову вас, когда будет готово."
    m "Можешь приготовить чашку кофе?"
    mc "Конечно."
    m "Спасибо, любимый."
    mc "Всегда пожалуйста."
    #fade out
    
    scene bg kitchen with fade
    show miyuki casual at t22
    show monika pjs happ cm oe at t21
    
    mc "Что ж, это было хорошо, что думаешь?"
    mm e7 om "Они были действительно вкусными."
    mm e7 "Спасибо, пап."
    mc "Не за что, и спасибо тебе за твою помощь."
    mm back e4 "Хе-хе-хе, было весело!"
    m "Скоро нам придётся готовить папе завтрак в постель, Мию."
    mm neutral e7 om "Да!"
    mc "Разве я ещё не говорил, что твой поцелуй был достаточной наградой?"
    m "Не начинай, мистер."
    mc "Что я могу сказать, я люблю дразнить."
    m "Будто я этого не знала, а-ха-ха."
    "Хм, похоже, сейчас около половины десятого."
    mc "Ладно, Мию, собирай свои вещи, мы отправимся через несколько минут."
    mm "Хорошо, папа."
    show miyuki at thide
    hide miyuki
    show monika at t11
    m "И куда вы двое направитесь в первую очередь?"
    mc "Придерживаясь моего вчерашнего плана, сначала мы навестим Нацуки."
    m "Я могла бы довести вас к ней, мне всё равно по пути на работу."
    mc "Конечно, это сэкономит немного времени."
    mc "Мию?"
    mm "Да?" #offscreen
    mc "Твоя мама отвезёт нас к тёте Нацуки."
    mm "Хорошо!"
    m "Ты тоже можешь надеть свои вещи, я только схожу за ноутбуком, и мы можем отправляться."
    mc "Отлично."
    #fade out
    stop music fadeout 1.0
    
    scene bg altstreetday_snow with fadehold
    
    show monika forward_winter neut cm oe at t21 zorder 2
    show miyuki winter at t22
    play music snowyjazz
    m "Вы не против пойти отсюда пешком?"
    mc "Да, без проблем."
    m happ "Хорошо, тогда увидимся после работы."
    mm "Пока, мама!"
    mm e4 "Люблю тебя!"
    show miyuki e7
    m "И тебя люблю, милая."
    show monika ce at h11:
        ease .3 zoom 3.8 yoffset 1900 
    #hug/kiss
    window hide dissolve
    pause 2.0
    show monika at h11:
        ease .5 zoom 1.0 yoffset 0
    #moni kiss
    m "Хорошего дня, дорогой, люблю тебя."
    mc "Я тоже тебя люблю, хорошего дня на работе."
    m ce "Конечно, постараюсь, ага."
    #fade out Monika
    show monika at thide
    hide monika
    show miyuki at t11
    mc "Хорошо, мисс, давай отправимся к тёте Нацуки."
    mm "Держу пари, она будет рада нас видеть."
    mc "Тебя? Определённо. Меня? Э-э-э, посмотрим."
    "Мне очень нравится доставать её."
    "Никто не может раздражать её так, как я."
    "Честно говоря, это забавно."
    mm "Торопись, пап."
    mc "Что за спешка? У нас целый день впереди, Мию."
    mm e4 "Да, но я правда хочу пригласить её прийти на вечеринку!"
    show miyuki e7
    mc "И ты пригласишь, только потерпи ещё немного."
    mm back b2 m4 "Но-"
    show miyuki m9
    mc "Эй, никаких «но». Мы всего в нескольких кварталах отсюда, и она никуда не собирается."
    mc "Просто наслаждайся прогулкой."
    mm neutral b3 m8 e4 "Хмф."
    mm m4 "Ладно."
    show miyuki m8
    mc "Хорошо."
    mc "А взамен я буду ходить быстрее, хорошо?"
    mm b2 om e7 "...Окей, папа."
    mc "Рад, что ты в деле, пошли."
    #fade out
    
    scene bg bakeryopening with fadehold
    show miyuki winter at t11
    
    "Здесь всегда пахнет корицей."
    "Я знаю, что это пекарня, но чёрт."
    "Это всегда заставляет меня купить пару булочек с корицей."
    mm "Эй, папа, можно нам чего-нибудь перекусить, раз уж мы здесь?"
    mc "Например?"
    mm m4 "М-м-м-м..."
    mm m8 b3 "..."
    mc "Есть из чего выбирать, правда?"
    mm b1 om "Угу! Сложно выбрать."
    mc "Ну, мы всё равно ещё будем здесь недолго, выбери что-нибудь, и я куплю это для тебя."
    mm "Хорошо, папа, я постараюсь выбрать что-нибудь побыстрее."
    show miyuki at t22
    show natsuki turned casual happ cm oe at t21
    n "Эй, вы двое!"
    mm e4 "Тётя Нацуки!"
    n ce "Как поживает моя маленькая Мию?"
    mm e7 "Замечательно!"
    show miyuki e7
    n oe "А как у тебя дела, [player]?"
    mc "Неплохо, что насчёт тебя?"
    n neut "Чертовски занята, но в остальном я в порядке."
    mc "Да, такое время."
    n "И не говори, я люблю свой бизнес, но, чёрт возьми, это утомительно."
    n "Тебе повезло, что ты работаешь только в круглосуточном магазине."
    mc "Я совсем не считаю себя счастливчиком, но я понимаю, о чём ты говоришь."
    n happ "Хорошо."
    n "Итак, что привело вас двоих сюда?"
    mc "О, я пришёл, чтобы сделать заказ на дюжину печенек, каждое из которых с разным вкусом."
    n anno rhip "...Правда?"
    mc "Конечно, одно с шоколадной крошкой, одно медовое овсяное с изюмом, одно с орехами и белым шоколадом макадамии, одно с арахисовым маслом, одно сахарное печенье, одно-"
    n ce "Мию, он сейчас серьёзно?"
    mm "Я не знаю, наверное, нет."
    n oe "Я тоже об этом думаю."
    n lhip "Просто говорю, если ты закончишь этот список и все ещё хочешь их, я выставлю двойную цену."
    mc "Это просто плохое обслуживание клиентов."
    mc "Я требую встречи с менеджером."
    show natsuki at thide
    hide natsuki
    pause(1.5)
    show natsuki turned casual sedu cm ce at t21
    #have natsuki slide offscreen, then back on
    n sedu ce "Пекарь, менеджер, владелец, прямо перед тобой."
    n happ b1d oe "У вас есть жалоба? Вы можете обсудить её с младшим руководителем."
    mm m4 "Со мной?"
    show miyuki m9
    n ce rhip "Верно."
    mm om e4 "Потрясающе!"
    mc "Учитывая, что мы здесь редко бываем, руководитель, возможно, неподходящая для неё работа."
    n oe rdown b1a "Конечно, она следит за тобой и держит в узде."
    n ce "Хорошая работа, Мию."
    mm "Спасибо!"
    show miyuki e7
    mc "Настраивает собственную дочь против меня, как жестоко."
    n oe "Мы, девочки, должны держаться вместе."
    mm "Да, папа."
    mc "Я бы так быстро не спрыгивал с корабля, в конце концов, из-за тебя мы сегодня здесь."
    mm e6 "...О да!"
    mm e7 "Тётя Нацуки, ты сможешь прийти на нашу вечеринку?"
    mm back "Пожалуйста?"
    n neut "Вечеринка?"
    mc "Да, перед Рождеством, она очень хотела, чтобы мы её устроили, и вот мы здесь."
    n "Здорово."
    show miyuki neutral m9 
    n pout "Но я не знаю, получится ли у меня, Мию."
    n sad "Рождество – самое загруженное время года для меня, и, возможно, я не смогу уйти отсюда до позднего вечера."
    mm b2 m4 "О-о-о."
    show miyuki m9 b1
    n happ "Но эй! Если я смогу, я позвоню твоему папе и дам ему знать, хорошо?"
    mm b2 om "Хорошо..."
    n ce "Как насчет бесплатной булочки с корицей, чтобы поменять этот хмурый взгляд?"
    mm "...Было бы славно."
    show miyuki b1
    mc "Можно мне тоже одну бесплатно?"
    n neut oe "А ты разве маленькая милая девочка?"
    mc "Я мог бы притвориться одной из них, если это означает бесплатную еду."
    n anno "Сделаешь это, и я запрещу тебе заходить в магазин."
    mc "Намёк ясен."
    mm e4 "А-ха-ха, ты боишься тёти Нацуки, папа."
    n happ "Да, и не позволяй ему забыть об этом."
    show miyuki e7
    mc "Я не боюсь, просто избегаю ужасной ситуации, когда я никогда не попробую твою выпечку снова."
    n "Это самое большое наказание, которое я могу тебе вынести."
    mc "Как говорится, я хочу булочку с корицей, и я заплачу за это."
    n ce "Нет, они обе за счёт заведения, я просто прикалывалась над тобой."
    mc "Ну, тогда ладно..."
    mc "Спасибо, Нацуки."
    mm e4 "Да, спасибо!"
    show miyuki e7
    n oe "Обоим – не за что."
    n rhip "Не стесняйтесь, возьмите булочки, а я должна вернуться к работе, эти заказы сами собой не выполнятся."
    mc "Отлично, мы поговорим с тобой позже."
    mm "Пока, тётя Нацуки!"
    n rdown ce "Пока, Мию."
    n oe "Да встречи, [player]."
    mc "До встречи."
    #fade out
    
    
    scene bg altstreetday_snow with fadehold
    
    show miyuki winter at t11
    
    mc "Итак, чем мы займёмся теперь?"
    mc "Хочешь спросить тётю Юри, или сначала пообедаем?"
    mm back e4 b2 om "Д-давай сначала пообедаем, пап." #nervous
    show miyuki cm
    mc "Хорошо, Мию."
    mc "Мы можем пойти в то кафе рядом, которое тебе нравится."
    mm neutral e6 om b1 "Правда?!"
    mc "Правда."
    mm e4 m2 "Ура!"
    mm om e7 "Я надеюсь, что милая леди там."
    mc "Думаю, мы увидим её, когда приедем."
    #fade out
    stop music fadeout 1.0
    
    scene bg cafe with fadehold
    show miyuki winter at t11
    play music firelofi
    mm m4 b2 e5 "Бр-р-р-р, на улице холодно."
    show miyuki m7
    mc "И то верно, но ты скоро согреешься."
    show kiyomi turned casual happ cm oe at t21
    show miyuki e7 b1 m9 at t22
    ky "Привет, ребята, с возвращением!" #Kiyomi
    mc "Привет снова."
    mm om "Привет, Кийоми!"
    ky ce "Как ты, Миюки?"
    show kiyomi oe
    mm e4 "Хе-хе, великолепно."
    show miyuki e7
    ky "Ну, рада слышать."
    ky "Сегодня только вы двое?"
    mc "Да, только мы."
    mm "Мама на работе."
    ky neut "О, я поняла."
    ky happ "Что ж, передай ей от меня привет, когда увидишь её."
    mm "Хорошо."
    ky "Так что вам принести выпить?"
    mm e4 "Яблочный сок, пожалуйста!"
    show miyuki e7
    mc "Я буду кофе."
    ky "Конечно, скоро вернусь."
    #fadeout kiyomi
    show kiyomi at thide
    hide kiyomi
    show miyuki at t11
    mm "Она здесь сегодня, папа."
    mc "Да, повезло нам, правда?"
    mm "Да, она очень хорошая."
    mc "И очень дружелюбная."
    "Хотя у неё странное чувство стиля."
    "Она, должно быть, сумасшедшая, чтобы носить что-то подобное зимой."
    show miyuki at t22
    show kiyomi turned casual happ cm oe at t21
    ky "Кофе для тебя и яблочный сок для тебя."
    mm "Спасибо!"
    ky ce "Не за что."
    ky oe "Уже знаете, что будете есть?"
    mm e4 "Угу!"
    show miyuki e7
    ky "Хорошо, милая, заказывай."
    mm "Можно мне куриные крылышки?"
    ky ce "Конечно, можно."
    ky oe "С картошкой фри?"
    mm "Да, пожалуйста."
    ky "Отлично, а для вас?"
    mc "Я возьму чизбургер с беконом, и картошкой фри."
    ky "Отлично, это не займёт много времени."
    mc "Спасибо."
    show kiyomi at thide
    hide kiyomi
    #fade out kiyomi again
    show miyuki at t11
    mm b2 m4 "А где мы возьмём ёлку?"
    show miyuki m9
    mc "М-м-м-м..."
    mm e4 m4 "Нам нужна ёлка, папа!"
    mm e7 "Мы должны были найти её неделю назад!"
    show miyuki m9 
    mc "Я знаю, я знаю."
    mc "Я постараюсь найти её завтра после работы, хорошо?"
    mm m4 "Обещаешь?"
    show miyuki m9
    mc "Обещаю."
    mc "Обещаю, что постараюсь, но не обещаю, что найду."
    mc "Но я сделаю всё, что в моих силах."
    mm om "Уж постарайся."
    mc "О, ещё бы, иначе я должен буду отвечать перед тобой и твоей мамой."
    mm b1 e4 "Вот именно!"
    "Она вырастет такой же, как мама, я знаю."
    "Я боюсь этого."
    mm "Эй, а Кийоми может прийти на вечеринку?"
    mc "Что? Нет, мы не приглашаем официантку."
    mm b2 m4 "О-о-о, почему нет?"
    show miyuki m9
    mc "Потому что это будет странно, Мию."
    mm m4 "Нет, это не так, мы ей нравимся."
    show miyuki m9
    mc "Да, как клиенты, она не является ни частью семьи, ни другом."
    mm m4 "О-о-о-о."
    show miyuki m9
    mc "Извини, но «нет» – это окончательный ответ."
    mm m8 b1 "Хмф."
    mc "Дуйся сколько хочешь, это ничего не изменит."
    mm m8 b3 "Хмф."
    mc "Хмф."
    mm e4 b3 m8 "Хмф!"
    mc "Хмф!!!"
    mm m4 "Прекрати!"
    show miyuki e7 m9
    mc "После вас, мисс."
    mm m4 "Злюка!"
    show miyuki m9
    mc "Эта злюка платит за обед, так что он не может быть таким злым."
    mm e4 m4 "...Может."
    show miyuki m9
    mc "Знаешь, ты напоминаешь мне тётю Сайори, когда дуешься."
    mm b1 e7 om "Думаешь, она сможет прийти на вечеринку?"
    mc "Сможет, я знаю это."
    mm m4 "Правда?"
    show miyuki m9
    mc "Да, я просто дам ей выходной, чтобы у неё не было оправданий."
    mc "И к тому же, ты правда думаешь, что она упустит возможность провести время с тобой?"
    mm m4 "...Нет."
    show miyuki m9
    mc "Именно. Тётя Сайори всегда хочет провести больше времени с Мию."
    mm e4 om "Э-хе-хе, я всегда хочу больше времени с тётей Сайори!"
    show miyuki e7 at t22
    show kiyomi turned casual happ cm oe at t21
    ky "Хорошо! Вот ваш заказ."
    ky "Бургер для папы и куриные крылышки для мисс Миюки."
    mc "Спасибо."
    mm "Спасибо, Кийоми!"
    ky ce "Пожалуйста, просто скажите, если вам нужно что-то ещё."
    show kiyomi oe
    mc "Конечно."
    show kiyomi at thide
    hide kiyomi
    #fade out Kiyomi
    show miyuki at t11
    mc "Отличненько, давай поторопимся и поедим, нам ещё нужно сделать пару остановок, а потом мы вернёмся домой к ужину."
    "Сегодня так много поручений."
    mm "Хорошо, папа."
    #fade out
    stop music fadeout 1.0
    
    scene bg library with fadehold
    show miyuki winter b2 m9 at t11
    play music yuri_theme
    "Всегда забавляет, когда я думаю о Юри, работающей в книжном магазине."
    "Похоже, она рождена для этой работы."
    mc "..."
    mc "Мию, ты выглядишь немного нервной."
    mm m4 "Я в порядке."
    show miyuki m9
    mc "Ладно."
    "Юри сегодня не работает?"
    "Она не за прилавком."
    "Может быть, я должен был хотя бы проверить, прежде чем появляться здесь."
    show miyuki at t22
    show yuri turned casual happ cm oe at t21
    y "О, привет, [player], привет, Миюки."
    y "Что привело вас сюда сегодня?"
    mc "Привет, Юри, как дела?"
    y ce "Довольно хорошо, спасибо."
    y neut oe "Самое загруженное время года, приятно видеть так много людей, увлекающихся литературой."
    y happ "Или хотя бы тех, кто дарит подарки в виде книг."
    y neut rup "Поэтому вы здесь?"
    show yuri rdown
    mc "М-м-м? На самом деле нет."
    "Хотя это напомнило мне о том, что нужно купить подарок для Моники и Сайори."
    "Подарки будут на днях, честное слово."
    mc "Мы здесь, потому что Миюки хочет кое-что тебе сказать."
    y happ "Ну, я была бы рада ответить на вопрос от тебя, Миюки."
    mm m9 "..."
    mc "Ну же, Миюки."
    mc "Что ты хочешь спросить у тёти Юри?"
    mm back b2 m4 "{size=12}...Тыхотелабыприйтикнамнавечеринку...{/size}"#small writing
    show miyuki m9
    y neut "Скажи это чуть погромче, я тебя не услышала."
    mm m4 "...Т-ты хотела бы прийти к нам на вечеринку?"
    show miyuki m9
    y "Вечеринка?"
    mc "Да, вечеринка в канун Рождества."
    mc "Мы решили послать тебе приглашение по её просьбе, поэтому я приводил её ко всем, чтобы спросить."
    y happ "Оу-у-у, как мило."
    y "Я так понимаю, вечером?"
    mc "Да, примерно к ужину, может, немного позже."
    y ce "Что ж, тогда я определённо могу присутствовать."
    mm m4 "П-правда?"
    show miyuki m9
    y oe "Конечно, Миюки, магазин не будет открыт так поздно в канун Рождества, так что я могу пойти на твою вечеринку."
    mm om "С-спасибо, тётя Юри."
    y "Не думай об этом, я уверена, что это будет веселый вечер для всех."
    y neut "Кстати об этом, кто ещё придёт?"
    mc "Хех, пока что только ты."
    mc "Хотя, я думаю, Сайори тоже придёт."
    mc "Мы уже навестили Нацуки, но она не уверена, сможет ли она."
    y sad "Как жаль."
    mc "Да, но, надеюсь, она ещё сможет заглянуть к нам."
    show yuri neut
    mc "Я также спрошу своего брата, а у Моники есть друг, которого она приглашает, так что посмотрим, как все пойдёт."
    y happ "Ну, даже если нас будет всего несколько человек, я уверена, что всё равно будет весело."
    mc "Конечно, будет, правда, Мию?"
    mm b1 "Да, папа."
    mc "Хорошо, я полагаю, мы оставим тебя в покое."
    y ce "О, это не проблема, вы удачно зашли."
    y oe "Во второй половине дня посетителей мало."
    mm "Можно я куплю книгу, папа?"
    mc "До Рождества меньше недели, Мию."
    mm b2 m4 "Но у меня есть карманные деньги!"
    show miyuki m9 
    mc "...А хотя, знаешь? Ты права."
    mc "Ты можешь купить книгу, если сможешь заплатить за неё."
    mm e4 b1 om "Ура!"
    mc "Иди и найди себе что-нибудь."
    mm e7 "Хорошо, скоро вернусь!"
    #fade out Miyu
    show miyuki at thide
    hide miyuki
    show yuri at t11
    mc "Я сомневаюсь, что она скоро вернётся."
    y "Никогда не угадаешь, она может увидеть что-то, что сразу привлечёт её внимание."
    mc "Это маловероятно, если только на обложке нет блёсток."
    y "Верно."
    y ce "Я уверена, что она найдёт то, что увлечёт её."
    mc "Наверное."
    show yuri neut oe
    mc "Как дела, помимо работы?"
    y "Ох, знаешь, довольно спокойно."
    y "Кроме работы, у меня мало дел."
    y happ "Только я и мои книги дома."
    y ce "Но я в порядке."
    mc "Это самое главное."
    y oe "Что насчёт тебя?"
    mc "То же самое, только с дочерью, ха-ха-ха."
    mc "Я слишком много работаю, чтобы заниматься другими делами, но когда я дома, она держит меня в тонусе."
    y ce "Ожидаемо."
    y oe "Если бы не она, то наверняка бы Моника."
    mc "Поверь мне, держит."
    mc "Миюки наверняка переняла это от матери."
    y "Я уверена в этом."
    show yuri at t21
    show miyuki winter at t22
    mm om "Нашла!"
    mc "Только одну? Я удивлён."
    mm "Мне хватает денег только на одну, папа."
    mc "Ну, я знал это."
    mc "Я просто не знал, знаешь ли ты."
    mm b3 m4 "Я не глупая."
    show miyuki m9
    mc "Никогда так не говорил."
    mc "Ты вырастешь такой же умной, как твоя мама."
    mm b1 om e4 "Так и есть."
    mc "Готова идти?"
    mm e7 "Угу!"
    mc "Замечательно, иди заплати за свою книгу, а потом мы пойдем к тётушке Сайори."
    mm e4 "Ура! Тётушка Сайори!"
    mc "М-м-м, но сначала ты должна заплатить за книгу."
    mm e7 "О да, держи, тётя Юри."
    y ce "Спасибо, Миюки, я пойду возьму сдачу." #fadeout Yuri
    show yuri at thide
    hide yuri
    "Глупышка."
    #fadeout
    stop music fadeout 1.0
    
    scene bg grocery with fadehold
    show miyuki winter at t11
    play music clubs
    
    mc "Хорошо, Мию, теперь вспомни, тётя Сайори работа-"
    show miyuki at t22
    show sayori work happ cm oe at t21
    mm e4 "Тётя Сайори!!!" #show sayo
    show miyuki e4
    s ce "А вот и моя Мию!"
    mc "Боже, никто никогда так не рад видеть меня."
    show miyuki e7
    s oe "Ты разве милый ребёнок?"
    mc "Я был им."
    mc "Нацуки тоже так сказала."
    s neut "О, ты виделся с Нацуки?"
    mc "Да, сегодня мы встречаемся со всеми."
    s happ "О, это весело, несколько дружеских визитов ради Мию?"
    mc "Нет, в этом есть причина."
    mm "Да!"
    mc "Ну же, Мию."
    mm "Можешь прийти к нам на вечеринку?!"
    s neut "Вечеринка?"
    s sad "Ой, подождите, не говорите мне, что я забыла о чьём-то дне рождения."
    mm "Нет, это вечерника в канун Рождества!"
    s nerv ce "О, слава Богу, я уже начала чувствовать себя очень плохо, хе-хе."
    mm "Так ты можешь прийти к нам, тётя Сайори?!"
    s neut oe "Когда вечеринка?"
    mc "В канун Рождества."
    s sad "О, я не совсем уверена, смогу ли я это сделать."
    mm b2 m4 "Оу-у-у, почему нет?"
    show miyuki m9
    s "Я не планировала это, так что мне, возможно, придётся работать."
    mc "..."
    mc "Сайори, ты же знаешь, что я составляю расписание, правильно?"
    show miyuki b1
    s nerv "...Это был длинный день, ладно?"
    mc "Здесь каждый день длинный."
    s happ "Для тебя, может быть, я всегда стараюсь изо всех сил."
    s nerv "Я плохо спала прошлой ночью."
    show sayori happ
    mc "Ну, не беспокойся, я просто попрошу Чеда прийти пораньше."
    mc "Он всё равно хотел поработать дольше."
    "Не то, чтобы он их заработал, или что-то в этом роде."
    s ce "Отлично, тогда я точно смогу сделать это, Мию!"
    mm e4 "Ура!"
    mm om "Я так рада, что ты будешь там, тётушка Сайори!"
    s oe "Я стараюсь не упускать шанс провести больше времени с моей маленькой Мию."
    mm e7 "Мне тоже нравится проводить с тобой время, тётя."
    mc "Если хочешь, можешь провести больше времени с ней."
    s "Конечно, хочу."
    mc "Отлично, приходи на несколько часов раньше и возьми её с собой, пока мы всё приготовим."
    s "Звучит как план."
    s ce "Я придумаю что-нибудь весёлое, чем мы можем заняться, Мию."
    show sayori oe
    mm e4 "Не могу дождаться!"
    show miyuki e7
    mc "Что ж, тебе придётся, моя дорогая, ещё несколько дней."
    mm "Я знаю, просто очень возбуждена."
    mc "Побереги силы на канун Рождества."
    mm e4 "Я буду спать спокойно, папа, я не ребёнок."
    mc "Знаю, знаю, просто говорю."
    show miyuki e7
    s "Теперь, Миюки, ты всегда будешь маменькиным ребёнком."
    mm "Тётя, это другое."
    s "Эй, если ты хочешь, иди выбери что-нибудь из конфетного отдела, я угощаю."
    mm back om "Правда?! Хорошо!"
    #fade out Miyu
    show miyuki at thide
    hide miyuki

    show sayori at t11
    mc "Ты балуешь её, знаешь?"
    s "Кто будет баловать её, если не я?"
    mc "Мистер Миттенс."
    s "Он получает достаточно, поверь."
    mc "Давать ей сахар так поздно, ты действительно собираешься делать это со мной, да?"
    s ce "Что сказать, я весёлая тётя."
    mc "Угу."
    mc "Как прошёл день?"
    s oe "Ничего необычного."
    s "Ничего, с чем я не могу справиться."
    mc "Хорошо, меньше поводов беспокоиться о завтрашнем дне."
    s ce "Ага."
    show sayori oe
    mc "Мию, поторопись, пожалуйста!"
    mm "Очень сложно выбрать!" #offscreen
    mc "Хех, она звучит как ты."
    s "Выбирать конфету не легко."
    mc "Говорит тот, кто просто скупает их все."
    s ce "Это экономит мне время." #gleeful
    mc "Твой стоматолог, должно быть, любит тебя."
    s nerv oe "Я получаю от него рождественские открытки, так что, может быть, хе-хе."
    mc "Да, это имеет смысл..."
    show sayori happ at t21
    show miyuki winter at t22
    mm om "Хорошо, думаю, я нашла."
    mc "...Тебе понадобилось так много времени, чтобы выбрать Кит-кат?"
    mm e4 "У него есть много видов!"
    s "Она права, знаешь ли."
    show miyuki e7
    mc "Да-да-да."
    mc "Пусть тётя заплатит за это, а потом отправимся домой к маме."
    mm "Спасибо, тётя Сайори."
    s ce "Не за что, Мию."
    show sayori oe
    mc "Удачный день для тебя, Миюки?"
    mm "Да, сегодня было весело."
    "Для неё, может быть, ну а у меня свидание с любящей женой и чашка кофе после этого."
    "Ходить целый день утомительно."
    s "Держи, Мию."
    mm e4 "Вкусно! Спасибо ещё раз."
    show miyuki e7
    s "Всегда пожалуйста."
    mc "Отлично, мы отправляемся."
    mc "Передай Чеду, чтобы он не наделал глупостей."
    s "Я поняла."
    mm "До свидания, тётя Сайори, скоро увидимся!"
    s "Обязательно, спокойной ночи, Мию."
    mc "Увидимся, Сай."
    #fade out
    
    scene bg living_room_day with fadehold
    show miyuki winter at t11
    
    mc "Мы дома!"
    mm "Мама, ты где?"
    show monika forward_yellow happ cm oe at t21 
    show miyuki at t22 
    m ce "Всегда рядом, ага, привет."
    show monika oe
    mm e4 "Привет, мама!"
    mc "Эй, детка."
    m "Привет, любимый."
    #hug/kiss
    show monika ce at h11:
        ease .3 zoom 3.8 yoffset 1900 
    #hug/kiss
    window hide dissolve
    pause 2.0
    show monika at h21:
        ease .5 zoom 1.0 yoffset 0
    m "Та-а-ак, как прошёл день?"
    mm e7 "Весело!"
    mc "Утомительно."
    mc "Нужен кофе."
    m "На кухне есть немного."
    mc "Отлично, скоро вернусь."
    #fadeout miyu and monika, then switch to kitchen bg
    scene bg kitchen with wipeleft
    "{cps=*1.5}Кофе кофе кофе кофе кофе кофе кофе кофе кофе кофе кофе кофе кофе кофе кофе кофе кофе кофе кофе кофе кофе кофе кофе кофе кофе кофе кофе кофе кофе кофе кофе кофе кофе кофе кофе кофе кофе кофе кофе кофе кофе кофе кофе кофе кофе кофе кофе кофе кофе{/cps} {nw}"
    "В такие дни, как этот, я благодарю бога, что Моника тоже любит кофе."
    "Я просто наполню самую большую чашку, которая у нас есть, этого должно хватить на весь вечер."
    "Странно, что нам с Моникой обоим нравится чёрный кофе."
    "Я имею в виду, каковы шансы."
    "...Хм, ужин не готовился, я что, забыл приготовить его в один из вечеров?"
    #remove textbox, back to living room
    mc "Не говори мне, что я забыл приготовить ужин..."
    show monika forward_yellow happ cm oe at t21
    show miyuki casual at t22
    m rhip "О, нет-нет, я только что заказала ужин, день выдался немного длинным, поэтому мне не хотелось готовить."
    m rdown "Я надеюсь, что всё в порядке."
    mc "Меня это устраивает."
    m "Что насчёт тебя?"
    mc "А, да!"
    mc "Ты сказала ей, Мию?"
    mm pose "Вроде!" #like the screenshot
    show miyuki neutral
    m ce "Ага, она упомянула булочку с корицей, книгу и конфету."
    m oe "Я не могу поверить, что это всё, из чего состоял день."
    mc "Не совсем, ха-ха."
    m "Теперь, если можешь, заполни недостающие пробелы."
    mc "Что ж, длинные истории вкратце."
    mc "Булочка с корицей досталась от Нацуки, которая, скорее всего, не сможет прийти."
    m neut "О, что ж, это прискорбно."
    mm "Я надеюсь, что она сможет найти способ навестить нас."
    m happ "Я тоже на это надеюсь, милая."
    m "Так, ты принёс мне одну?"
    mc "Нет, но я действительно вёл себя как ребёнок, чтобы заполучить её."
    m neut "Что?"
    mm e4 "Папа просто ведёт себя глупо, он этого не делал."
    mc "Конечно, нет."
    show miyuki e7
    m laug ce "Слава Богу."
    show monika happ oe 
    mc "Я просто пригрозил, и это было всё, что требовалось."
    m anno "Х-х-х-х, конечно, ты это сделал."
    mc "Если это поможет, в то время там больше никого не было, и это было действительно забавно."
    m "Почему-то я не чувствую себя лучше."
    mc "Это потому, что я не принёс тебе ещё одну, не так ли?"
    m happ "...Возможно."
    mc "Я возьму одну, когда в следующий раз буду там проезжать."
    m ce "Спасибо."
    m oe "А что насчёт Юри и Сайори?"
    mc "Что ж, Сайори, очевидно, сможет прийти, и вот откуда взялись конфеты."
    m "Очевидно."
    mc "Сайори действительно нравится баловать её."
    mm "Тётя Сайори действительно милая."
    m "Да, это так, особенно для тебя."
    mm e4 "Э-хе-хе-хе."
    mc "Юри тоже может прийти."
    mm e7 "Я купила книгу, мама!"
    mm back "Можем мы прочитать её вместе позже?"
    m neut cm "М-м-м?"
    mc "Она купила книгу на свои «карманные» деньги."
    "И это не прямо чтобы домашние дела, вроде мытья посуды."
    "Мы просто заставляем её делать маленькие вещи, чтобы научить её ответственности."
    m happ "Это довольно круто."
    m "Конечно, мы можем прочесть это позже, после ужина звучит хорошо?"
    mm neutral "Угу."
    m "Возможно Нацуки, Сайори и Юри, да?"
    mc "Ага."
    mc "Что насчёт твоего друга?"
    m "Кото сказала, что она, вероятно, сможет задержаться ненадолго."
    mc "Отлично."
    m "А твой брат?"
    mc "..."
    m neut "Ты забыл написать ему, не так ли?"
    mc "Нет..."
    mc "Ладно, возможно."
    mc "Вот, я напишу ему прямо сейчас."
    
    mc_nvl "Быстрый вопрос, ты можешь прийти на вечеринку в канун Рождества?"
    mc_nvl "Твоей племяннице понравится, если ты сможешь."
    
    mc "Готово."
    mc "Посмотрим, что он ответит."
    mc "Даже если он не сможет, у нас и так достаточно людей для вечеринки."
    m happ "Похоже на то, пока никто ничего не придумал."
    mc "Тем не менее, худшее, что может быть, это небольшое собрание."

    m neut "Правда."
    m happ "Ну, мы просто сделаем всё возможное."
    mm e4 "Да!"
    mm e7 "Будет весело."
    m "Конечно, будет, милая."
    m "А что касается вас, мистер, можете ли вы принести ёлку завтра?"
    mc "Вероятно после работы."
    "Моя вина, что я так долго ждал."
    m "Хорошо."
    m "Я могу отвести Мию в торговый центр завтра, чтобы купить украшения и прочее."
    mc "Это сработает."
    mm e4 "Торговый день с мамой."
    show miyuki e7
    m ce "Да, немного времени мамы и Мию."
    mm e4 "Ура!"
    mc "Что ж, надеюсь, вам двоим понравится этот день, и я обязательно куплю ёлку, прежде чем вернусь домой."
    show miyuki e7
    m oe "Великолепно."
    mc "Может, посмотрим телевизор, пока еду не доставили?"
    m "Конечно."
    mm "Давайте посмотрим рождественский фильм."
    mc "Хорошо, выбери тот, который будем смотреть."
    "Думаю, это будет достаточно весёлый способ провести вечер."
    "Хороший способ закончить день."
    "А завтра снова на работу."
    "Ура."
    stop music fadeout 1.0
    #fadeout

