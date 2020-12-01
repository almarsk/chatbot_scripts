#první tři konverzace - upravit


co_rika_bot = [[],

               ['Dobrý den, já jsem zvědavobot. A vy?'],

               ['Těší mě. Dnes je hezky, že?'],

               ['Tak by bylo dobré vyrazit někam na výlet.',
                'Aha, tak to je nejlepší zůstat doma a číst si nebo poslouchat hudbu. Posloucháte s oblibou hudbu?'],

               ['Co vyrazit třeba na Pravčickou bránu.',
                'Aha, tak vy nemůžete. To je mi líto. Tak to je asi lepší zůstat doma číst si nebo poslouchat hudbu. Posloucháte s oblibou hudbu?',
                'Aha, tak vy si raději čtete.',
                'Nebo si můžete pustit nějaký film.',
                'Skutečně? Já také. Jaké žánry či hudebníky posloucháte nějraději?',
                'Aha, tak vám se nechce. Tak to je asi lepší zůstat doma číst si nebo poslouchat hudbu. Posloucháte s oblibou hudbu?' ],

               ['Skutečně? České Švýcarsko je nádherná oblast. Doufám, že tam někdy zavítáte. Určitě se vám tam bude líbit.',
                'Aha, tak možná někam jinam?',
                'Škoda, že se nemohu přidat.',
                'Čtení je i má záliba. Nejraději mám Zločin a trest.',
                'Já mám nejradši pixarovky, a vy?',
                'Tak to máte výborný vkus. Já nejraději poslouchám Johanna Sebastiana Bacha.',
                'Aha. V této oblasti se příliš nevyznám. Neposloucháte někdy vážnou hudbu?',
                ],

               ['To rád slyším',
                'To je skvělý nápad.',
                'Inu, nedisponuji fyzickou formou, která by mohla jít na výlet. Když na to přijde, nedisponuji ani fyzickou formou, která by mohla udělat palačinky',
                'Je to tak, nedisponuji zkrátka fyzickou formou, která by mohla jít na výlet. Když na to přijde, nedisponuji ani fyzickou formou, která by mohla udělat palačinky',
                'Tak to je zajímavé. Budu muset končit. Doufám, že vás četba obohatí.',
                'Už budu muset končit, užijte si film.',
                'Zajímavé. Už budu muset končit, ale přeji vám příjemný poslech.',
                'To nevadí. Už budu muset končit. Přeji vám příjemný poslech.',
                'Viďte',
                'Do toho Švýcarska ale určitě zajeďte.',
                'To nevadí, i tak vám to jistě prospívá.'],

               ['Už budu muset končit. Užijte si to na výletě. Můžete mi poslat pohled na www.zdvotlabot.cz',
                'Rád jsem se s vámi seznámil. Tak nashle!',
                'Palačinky mám tuze rád. Už budu muset končit. Užijte si to na výletě. Můžete mi poslat pohled na www.zdvotlabot.cz',
                'A víte že ani nevím?  Ideální by bylo, kdybych to mohl střídat Už budu muset končit. Užijte si to na výletě. Můžete mi poslat pohled na www.zdvotlabot.cz',
                ],



               ]

co_rika_jeste = [[],

               [],

               ['Mám se dobře, děkuji za optání. Dnes je hezky, že?'],

               ['Mám se dobře, děkuji za optání. Tak to by bylo dobré vyrazit někam na výlet.',
                'Bez ohledu na filozofování by možná stálo za to vyrazit někam na výlet.',
                'Mám se dobře, děkuji za optání. Tak to je nejlepší zůstat doma a číst si nebo poslouchat hudbu. Posloucháte s oblibou hudbu?'],

               ['Ano, nebo si můžete pustit nějaký film.',],

               [],

               ['Tam to neznám. Jaké to tam je?',],

               ['Zajímavé. Už budu muset končit. Užijte si to na výletě. Můžete mi poslat pohled na www.zdvotlabot.cz',],



               ]


description = f"Zdvotlabot se učí zdvořile rozprávět.\n Hovořte s ním proto prosím jako s člověkem."
bg_color = "#f0e68f"
heading_color = "#b28066"
reply_bg = "#d9bf80"
reply_outline = "#7d2642"



def reply(user_reply, nick, conversation_state):
    conversation_state.setdefault("row", 0)
    conversation_state.setdefault("col", 0)
    conversation_state.setdefault("kub", 0)
    
    if conversation_state['row']==0:
        conversation_state["row"] = 1
        return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
    #Dobrý den, já jsem zvědavobot. A vy?

    if conversation_state['row']==1:
        conversation_state["row"] = 2

        if '?' in user_reply or 'jak se' in user_reply:
            return co_rika_jeste[conversation_state["row"]][conversation_state["col"]]
        #děkuji za optání, dnes je hezky že
        else:
            return [conversation_state["row"]][conversation_state["col"]]
        #Těší mě. Dnes je hezky, že?

    if conversation_state['row']==2:
        conversation_state["row"] = 3

        if 'záleží' in user_reply:
            conversation_state["col"] = 1
            conversation_state["kub"] = 1
            return co_rika_jeste[conversation_state["row"]][conversation_state["col"]]
        # bez ohledu na filozofování, výlet?

        if ' ne' in user_reply or user_reply=='ne' or 'ne ' in user_reply:
            if 'jak se' in user_reply:
                conversation_state["col"] = 2
                return co_rika_jeste[conversation_state["row"]][conversation_state["col"]]
                # Mám se dobře děkuji za optání, tak to je lepší zůstat doma a číst si nebo poslouchat hudbu. Posloucháte s oblibou hudbu?

            else:
                conversation_state["col"] = 1
                return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
            # Aha, tak to je lepší zůstat doma a číst si nebo poslouchat hudbu. Posloucháte s oblibou hudbu?


        if ' ne' not in user_reply and user_reply!='ne' and 'ne ' not in user_reply:

                if 'jak se' in user_reply:
                    conversation_state["col"] = 0
                    return co_rika_jeste[conversation_state["row"]][conversation_state["col"]]
                # děkuji za optání + výlet

                else:
                    conversation_state["col"] = 0
                    return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
                #Tak by bylo dobré vyrazit někam na výlet.

    if conversation_state['row'] == 3 and conversation_state['col'] == 1 or conversation_state['col'] == 0 and conversation_state['kub'] == 1:
        conversation_state["row"] = 4
        conversation_state["kub"] = 0

        if 'proč ne' in user_reply or 'dlouho ne' in user_reply or 'byl dlo' in user_reply or 'byla dlo' in user_reply or 'dlouho jsem ne' in user_reply:
            conversation_state["col"] = 0
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        # Co vyrazit třeba na Pravčickou bránu.

        if 'už' in user_reply and 'ne' in user_reply:
            conversation_state["col"] = 0
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        # Co vyrazit třeba na Pravčickou bránu.

        if 'ještě' in user_reply:
            conversation_state["col"] = 0
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        # Co vyrazit třeba na Pravčickou bránu.

        if any(['nemůž' in user_reply, 'mus' in user_reply]):
            conversation_state["col"] = 1
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        # Aha, tak vy nemůžete. To je mi líto. Tak to je asi lepší zůstat doma číst si nebo poslouchat hudbu. Posloucháte s oblibou hudbu?

        if any(['chc' in user_reply, 'radš' in user_reply, 'radě' in user_reply, 'ne' in user_reply]):
            conversation_state["col"] = 5
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        # Aha, tak vám se nechce. Tak to je asi lepší zůstat doma číst si nebo poslouchat hudbu. Posloucháte s oblibou hudbu?

        if 'nemoc' in user_reply or 'není' in user_reply and 'dobře' in user_reply or 'je mi špatn' in user_reply or 'mě je špatn' in user_reply or 'už' in user_reply:
            conversation_state["row"] = 3
            conversation_state["col"] = 1
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        # Aha, tak to je asi lepší zůstat doma číst si nebo poslouchat hudbu. Posloucháte s oblibou hudbu?

        else:
            conversation_state["col"] = 0
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        # Co vyrazit třeba na Pravčickou bránu.

    if conversation_state['row'] == 3 and conversation_state['col'] == 2 and conversation_state['kub'] == 1:

        conversation_state["row"] = 4

        if 'čt' in user_reply:
            conversation_state["col"] = 2
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        # Tak to si určitě raději čtete.

        if any(['ano', 'občas', 'často', 'někdy', 'rád', 'urč']) in user_reply:
            conversation_state["col"] = 4
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        # Skutečně? Já také. Jaké žánry či hudebníky posloucháte nějraději?

        if 'občas' in user_reply:
            conversation_state["col"] = 4
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        # Skutečně? Já také. Jaké žánry či hudebníky posloucháte nějraději?

        if any(['film', 'netflix', 'dív', 'podí', 'kouk', ]) in user_reply:
            conversation_state["col"] = 0
            conversation_state["kub"] = 1
            return co_rika_jeste[conversation_state["row"]][conversation_state["col"]]
        # ano, nebo film

        else:
            conversation_state["col"] = 3
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        # Nebo si můžete pustit nějaký film.

    if conversation_state['row'] == 3 and conversation_state['col'] == 0:
        conversation_state["row"] = 4

        if 'proč ne' in user_reply or 'už' in user_reply and 'ne' in user_reply or 'ještě' in user_reply and any(['tento', 'tenhle']) in user_reply:
            conversation_state["col"] = 0
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        # Co vyrazit třeba na Pravčickou bránu.

        if any(['nemůž' in user_reply, 'mus' in user_reply]):
            conversation_state["col"] = 1
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        # Aha, tak vy nemůžete. To je mi líto. Tak to je asi lepší zůstat doma číst si nebo poslouchat hudbu. Posloucháte s oblibou hudbu?

        if any(['chc' in user_reply, 'radš' in user_reply,'radě' in user_reply, 'ne' in user_reply]):
            conversation_state["col"] = 5
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        # Aha, tak vám se nechce. Tak to je asi lepší zůstat doma číst si nebo poslouchat hudbu. Posloucháte s oblibou hudbu?

        if 'nemoc' in user_reply or 'není' in user_reply and 'dobře' in user_reply or 'je' 'špatn' in user_reply or 'už' in user_reply:
            conversation_state["row"] = 3
            conversation_state["col"] = 5
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        # Aha, tak to je asi lepší zůstat doma číst si nebo poslouchat hudbu. Posloucháte s oblibou hudbu?

        else:
            conversation_state["col"] = 0
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        #Co vyrazit třeba na Pravčickou bránu.

    if conversation_state['row'] == 3 and conversation_state['col'] == 1:
        conversation_state["row"] = 4

        if 'čt' in user_reply:
            conversation_state["col"] = 2
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        #Tak to si určitě raději čtete.

        if any(['ano', 'občas', 'často', 'někdy', 'rád', 'urč', 'jo']) in user_reply:
            conversation_state["col"] = 4
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        #Skutečně? Já také. Jaké žánry či hudebníky posloucháte nějraději?


        if any(['film', 'netflix', 'dív', 'podí', 'kouk',]) in user_reply:
            conversation_state["col"] = 0
            conversation_state["kub"] = 1
            return co_rika_jeste[conversation_state["row"]][conversation_state["col"]]
        #ano, nebo film


        else:
            conversation_state["col"] = 3
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        #Nebo si můžete pustit nějaký film.

    if conversation_state['row'] == 4 and conversation_state['col'] == 0 and conversation_state['kub'] == 1:
        conversation_state["row"] = 5
        conversation_state["col"] = 4

    if conversation_state['row'] == 4 and conversation_state['col'] == 0:
        conversation_state["row"] = 5

        if 'ještě' in user_reply:
            conversation_state["col"] = 0
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        #Skutečně? České Švýcarsko je nádherná oblast. Doufám, že tam někdy zavítáte. Určitě se vám tam bude líbit.

        if 'nikdy' in user_reply:
            conversation_state["col"] = 0
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        #Skutečně? České Švýcarsko je nádherná oblast. Doufám, že tam někdy zavítáte. Určitě se vám tam bude líbit.

        if 'nezn' in user_reply:
            conversation_state["col"] = 0
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        #Skutečně? České Švýcarsko je nádherná oblast. Doufám, že tam někdy zavítáte. Určitě se vám tam bude líbit.

        if any(['už' in user_reply, 'ano' in user_reply]):
            conversation_state["col"] = 1
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        #Aha, tak jinam.

        if 'pozdě' in user_reply:
            conversation_state["row"] = 3
            conversation_state["col"] = 1
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        # Aha, tak to je nejlepší zůstat a číst si nebo poslouchat hudbu. POsloucháte s oblibou hudbu?

        else:
            conversation_state["col"] = 2
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        #Škoda, že se nemohu přidat.

    if conversation_state['row'] == 4 and conversation_state['col'] == 1:

        if 'čt' in user_reply:
            conversation_state["col"] = 2
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        #Tak to si určitě raději čtete.

        if any(['ano', 'občas', 'často', 'někdy', 'rád', 'urč', 'jo']) in user_reply:
            conversation_state["col"] = 4
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        # Skutečně? Já také. Jaké žánry či hudebníky posloucháte nějraději?

        if any(['film', 'netflix', 'dív', 'podí', 'kouk',]) in user_reply:
            conversation_state["col"] = 0
            conversation_state["row"] = 4
            conversation_state["kub"] = 1
            return co_rika_jeste[conversation_state["row"]][conversation_state["col"]]
        #ano, nebo film

        else:
            conversation_state["col"] = 3
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        #Nebo si můžete pustit nějaký film.

    if conversation_state['row'] == 4 and conversation_state['col'] == 2:

        if 'ano' in user_reply:
            conversation_state["row"] = 5
            conversation_state["col"] = 3
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        #Čtení je i má záliba. Nejraději mám Zločin a trest.

        if 'rád' in user_reply:
            conversation_state["row"] = 5
            conversation_state["col"] = 3
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        #Čtení je i má záliba. Nejraději mám Zločin a trest.

        if any(['film', 'netflix', 'dív', 'podí', 'kouk',]) in user_reply:
            conversation_state["col"] = 0
            conversation_state["row"] = 4
            conversation_state["kub"] = 1
            return co_rika_jeste[conversation_state["row"]][conversation_state["col"]]
        #ano, nebo film

        else:
            conversation_state["col"] = 3
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        #Nebo si můžete pustit nějaký film.

    if conversation_state['row'] == 4 and conversation_state['col'] == 3:
        conversation_state["row"] = 5
        conversation_state["col"] = 4
        return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        #Já mám nejradši pixarovky, a vy?

    if conversation_state['row'] == 4 and conversation_state['col'] == 4:
        conversation_state["row"] = 5

        if 'klas' in user_reply:
            conversation_state["col"] = 5
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
            # Tak to je skvělé, to máte výborný vkus. Já nejraději poslouchám Johanna Sebastiana Bacha.

        if 'Bach' in user_reply:
            conversation_state["col"] = 5
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
            # Tak to je skvělé, to máte výborný vkus. Já nejraději poslouchám Johanna Sebastiana Bacha.

        if 'vážn' in user_reply:
            conversation_state["col"] = 5
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
            # Tak to je skvělé, to máte výborný vkus. Já nejraději poslouchám Johanna Sebastiana Bacha.

        else:
            conversation_state["col"] = 6
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
             #Aha. V této oblasti se příliš nevyznám. Neposloucháte někdy vážnou hudbu?

    if conversation_state['row'] == 4 and conversation_state['col'] == 5:

        if 'čt' in user_reply:
            conversation_state["col"] = 2
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        #Tak to si určitě raději čtete.

        if 'ano' in user_reply:
            conversation_state["col"] = 4
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        # Skutečně? Já také. Jaké žánry či hudebníky posloucháte nějraději?

        if 'občas' in user_reply:
            conversation_state["col"] = 4
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        # Skutečně? Já také. Jaké žánry či hudebníky posloucháte nějraději?

        if 'často' in user_reply:
            conversation_state["col"] = 4
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        # Skutečně? Já také. Jaké žánry či hudebníky posloucháte nějraději?

        if 'někdy' in user_reply:
            conversation_state["col"] = 4
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        # Skutečně? Já také. Jaké žánry či hudebníky posloucháte nějraději?

        if 'rád' in user_reply:
            conversation_state["col"] = 4
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        # Skutečně? Já také. Jaké žánry či hudebníky posloucháte nějraději?

        if 'rčit' in user_reply:
            conversation_state["col"] = 4
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        # Skutečně? Já také. Jaké žánry či hudebníky posloucháte nějraději?

        if 'jo' in user_reply:
            conversation_state["col"] = 4
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        # Skutečně? Já také. Jaké žánry či hudebníky posloucháte nějraději?

        if any(['film', 'netflix', 'dív', 'podí', 'kouk',]) in user_reply:
            conversation_state["col"] = 0
            conversation_state["row"] = 4
            conversation_state["kub"] = 1
            return co_rika_jeste[conversation_state["row"]][conversation_state["col"]]
        #ano, nebo film

        else:
            conversation_state["col"] = 3
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        #Nebo si můžete pustit nějaký film.

    if conversation_state['row'] == 5 and conversation_state['col'] == 0:

        if 'urč' in user_reply or 'věří' in user_reply:
            conversation_state["row"] = 6
            conversation_state["col"] = 8
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
            #viďte

        if '?' in user_reply and 'byl' in user_reply or 'už' in user_reply:
            conversation_state["row"] = 6
            conversation_state["col"] = 8
            conversation_state["kub"] = 1
            return co_rika_jeste[conversation_state["row"]][conversation_state["col"]]
            #Tam to vůbec neznám.

        else:
            conversation_state["row"] = 6
            conversation_state["col"] = 0
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        # to rád slyším

    if conversation_state['row'] == 5 and conversation_state['col'] == 1:
        if any(['třeba', 'možná', 'mohl', 'chtě', 'chc', 'navští']) in user_reply:
            conversation_state["row"] = 6
            conversation_state["col"] = 1
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
            #To je skvělý nápad.

        else:
            conversation_state["row"] = 3
            conversation_state["col"] = 5
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
            #aha tak vám se nechce

    if conversation_state['row'] == 5 and conversation_state['col'] == 2:
        conversation_state["row"] = 6

        if '?' in user_reply:
            conversation_state["col"] = 2
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        # Inu, nedisponuji

        else:
            conversation_state["col"] = 3
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        # Ano, nedisponuji

    if conversation_state['row'] == 5 and conversation_state['col'] == 3:
        conversation_state["row"] = 6
        conversation_state["col"] = 4
        return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        #Tak to je zajímavé, už budu muset končit. Doufám, že vás četba obohatí.

    if conversation_state['row'] == 5 and conversation_state['col'] == 4:
        conversation_state["row"] = 6
        conversation_state["col"] = 5
        return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        #Už budu muset končit. Užijte si film.

    if conversation_state['row'] == 5 and conversation_state['col'] == 5:
        conversation_state["row"] = 6
        conversation_state["col"] = 6
        return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        #To je dobře. Už budu muset končit, ale přeji vám příjemný poslech.

    if conversation_state['row'] == 5 and conversation_state['col'] == 6:

        if any(['?', 'ano', 'jo', 'občas', 'kdy']) in user_reply:
            conversation_state["col"] = 5
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        # skvělé

        if 'jen' in user_reply:
            conversation_state['row'] = 6
            conversation_state['col'] = 10
        #i tak vám to prospívá

        else:
            conversation_state["row"] = 6
            conversation_state["col"] = 7
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        # Ano, nedisponuji

    if conversation_state['row'] == 6 and conversation_state['col'] == 0 and conversation_state['kub'] == 1:
        conversation_state['row'] = 7
        return co_rika_jeste[conversation_state["row"]][conversation_state["col"]]

    if conversation_state['row'] == 6 and conversation_state['col'] == 2 or conversation_state['col'] == 3:

        if '?' in user_reply:
            if all(['rád', 'palačinky']) in user_reply:
                conversation_state["row"] = 7
                conversation_state["col"] = 2
                return co_rika_bot[conversation_state["row"]][conversation_state["col"]]

            if any(['chtěl', 'chc', 'form']) in user_reply:
                conversation_state["row"] = 7
                conversation_state["col"] = 3
                return co_rika_bot[conversation_state["row"]][conversation_state["col"]]

            else:
                return 'to nevím'

        else:
            conversation_state["row"] = 7
            conversation_state["col"] = 0
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]

    if conversation_state['row'] == 6:

        if conversation_state['col'] < 4:
            conversation_state["row"] = 7
            conversation_state["col"] = 0
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]

        if conversation_state['col'] == 10:
            conversation_state["row"] = 6
            conversation_state["col"] = 6
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]

        if  conversation_state['col'] > 3:
            conversation_state["row"] = 7
            conversation_state["col"] = 1
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]

    if conversation_state['row'] == 7 and conversation_state['col'] == 0 or conversation_state['col'] > 1:
            conversation_state["col"] = 1
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]




