co_rika_bot = [[],

               ['Dobrý den, já jsem zvědavobot. A vy?'],

               ['Těší mě. Dnes je hezky, že?',
                'Mám se dobře, děkuji za optání. Dnes je hezky, že?'],

               ['Bez ohledu na filozofování by možná stálo za to vyrazit někam na výlet.',
                'Tak by bylo dobré vyrazit někam na výlet.',
                'Mám se dobře, děkuji za optání. Tak to by bylo dobré vyrazit někam na výlet.',
                'Mám se dobře, děkuji za optání. Tak to je nejlepší zůstat doma a číst si nebo poslouchat hudbu. Posloucháte s oblibou hudbu?',
                'Aha, tak to je nejlepší zůstat doma a číst si nebo poslouchat hudbu. Posloucháte s oblibou hudbu?',
                'Aha, tak vy nemůžete. To je mi líto. Tak to je asi lepší zůstat doma číst si nebo poslouchat hudbu. Posloucháte s oblibou hudbu?',
                'Aha, tak vám se nechce. Tak to je určitě nejlepší zůstat doma číst si nebo poslouchat hudbu. Posloucháte s oblibou hudbu?'],

               ['Co vyrazit třeba na Pravčickou bránu.',
                'Tam to neznám. Jaké to tam je?',
                'Aha, tak vy si raději čtete.',
                'Nebo si můžete pustit nějaký film.',
                'Ano, nebo si můžete pustit nějaký film.',
                'Skutečně? Já také. Jaké žánry či hudebníky posloucháte nějraději?',
                ],

               ['Skutečně? České Švýcarsko je nádherná oblast. Doufám, že tam někdy zavítáte. Určitě se vám tam bude líbit.',
                'Aha, tak možná někam jinam?',
                'Škoda, že se nemohu přidat.',
                'Tak to je škoda, že tam nemůžu jet.',
                'Čtení je i má záliba. Nejraději mám Zločin a trest.',
                'Já mám nejradši pixarovky, a vy?',
                'Aha. V této oblasti se příliš nevyznám. Neposloucháte někdy vážnou hudbu?',
                ],

               ['Viďte.',
                'To je skvělý nápad.',
                'Inu, nedisponuji fyzickou formou, která by mohla jít na výlet. Když na to přijde, nedisponuji ani fyzickou formou, která by mohla udělat palačinky',
                'Je to tak, nedisponuji zkrátka fyzickou formou, která by mohla jít na výlet. Když na to přijde, nedisponuji ani fyzickou formou, která by mohla udělat palačinky',
                'Tak to máte výborný vkus. Já nejraději poslouchám Johanna Sebastiana Bacha.',
                'Tak to máte výborný vkus. Já také nejraději poslouchám Johanna Sebastiana Bacha.',
                'To nevadí, i tak vám to jistě prospívá.'],

               ['To je dobrý nápad. Už budu muset končit. Užijte si to na výletě. Můžete mi poslat pohled na www.zdvotlabot.cz',
                'Zajímavé. Už budu muset končit. Užijte si to na výletě. Můžete mi poslat pohled na www.zdvotlabot.cz',
                'Už budu muset končit. Užijte si to na výletě. Můžete mi poslat pohled na www.zdvotlabot.cz',
                'Palačinky mám tuze rád. Už budu muset končit. Užijte si to na výletě. Můžete mi poslat pohled na www.zdvotlabot.cz',
                'A víte že ani nevím?  Ideální by bylo, kdybych to mohl střídat. Už budu muset končit. Užijte si to na výletě. Můžete mi poslat pohled na www.zdvotlabot.cz',
                'Tak to je zajímavé. Budu muset končit. Doufám, že vás četba obohatí.',
                'Tak to je skvělé. Už budu muset končit, užijte si film!',
                'Zajímavé. Už budu muset končit, ale přeji vám příjemný poslech.',
                'Už budu muset končit. Přeji vám příjemný poslech.',
                'Vážná hudba má na své posluchače blahodárné účinky.  Už budu muset končit. Přeji vám příjemný poslech.',

                ],

               ['Rád jsem se s vámi seznámil. Tak nashle!']


               ]

description = f"Zdvotlabot se učí zdvořile rozprávět.\n Hovořte s ním proto prosím jako s člověkem."
bg_color = "#c7c7ab"
heading_color = "#999966"
reply_bg = "#b8b894"
reply_outline = "#999966"


def reply(user_reply, nick, conversation_state):
    low_up = str(user_reply).lower()
    conversation_state.setdefault("row", 0)
    conversation_state.setdefault("col", 0)

    if conversation_state['row'] == 0:
        conversation_state["row"] = 1
        return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        # Dobrý den, já jsem zvědavobot. A vy?

    if conversation_state['row'] == 1:
        conversation_state["row"] = 2

        if '?' in low_up or 'jak se' in low_up:
            conversation_state['col'] = 1
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        # děkuji za optání, dnes je hezky že
        else:
            conversation_state['col'] = 0
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        # Těší mě. Dnes je hezky, že?

    if conversation_state['row'] == 2:
        conversation_state["row"] = 3

        if 'záleží' in low_up:
            conversation_state["col"] = 0
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        # bez ohledu na filozofování, výlet?

        if 'zima' in low_up or 'oškli' in low_up:
            if 'jak se' in low_up:
                conversation_state["col"] = 3
                return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
                # Mám se dobře děkuji za optání, tak to je lepší zůstat doma a číst si nebo poslouchat hudbu. Posloucháte s oblibou hudbu?
            else:
                conversation_state["col"] = 4
                return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
                # Aha, tak to je lepší zůstat doma a číst si nebo poslouchat hudbu. Posloucháte s oblibou hudbu?

        if ' ne' in low_up or low_up == 'ne' or 'ne ' in low_up:
            if 'jak se' in low_up:
                conversation_state["col"] = 3
                return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
                # Mám se dobře děkuji za optání, tak to je lepší zůstat doma a číst si nebo poslouchat hudbu. Posloucháte s oblibou hudbu?

            if 'chc' in low_up or 'radš' in low_up or 'radě' in low_up:
                conversation_state["col"] = 6
                return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
            # Aha, tak vám se nechce. Tak to je asi lepší zůstat doma číst si nebo poslouchat hudbu. Posloucháte s oblibou hudbu?

            else:
                conversation_state["col"] = 4
                return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
            # Aha, tak to je lepší zůstat doma a číst si nebo poslouchat hudbu. Posloucháte s oblibou hudbu?

        if 'bylo' in low_up and 'lépe' in low_up:
            if 'jak se' in low_up:
                conversation_state["col"] = 3
                return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
                # Mám se dobře děkuji za optání, tak to je lepší zůstat doma a číst si nebo poslouchat hudbu. Posloucháte s oblibou hudbu?

            if 'chc' in low_up or 'radš' in low_up or 'radě' in low_up:
                conversation_state["col"] = 6
                return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
            # Aha, tak vám se nechce. Tak to je asi lepší zůstat doma číst si nebo poslouchat hudbu. Posloucháte s oblibou hudbu?

            else:
                conversation_state["col"] = 4
                return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
            # Aha, tak to je lepší zůstat doma a číst si nebo poslouchat hudbu. Posloucháte s oblibou hudbu?

        else:

            if 'jak se' in low_up:
                conversation_state["col"] = 2
                return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
            # děkuji za optání + výlet

            else:
                conversation_state["col"] = 1
                return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
            # Tak by bylo dobré vyrazit někam na výlet.

    if conversation_state['row'] == 3 and conversation_state['col'] < 3:

        if 'třeba' in low_up or '?' in low_up or 'jste' in low_up:
            conversation_state["row"] = 4
            conversation_state["col"] = 1
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        # tam to neznám

        if 'proč ne' in low_up or 'dlouho ne' in low_up or 'byl dlo' in low_up or 'byla dlo' in low_up:
            conversation_state["row"] = 4
            conversation_state["col"] = 0
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        # Co vyrazit třeba na Pravčickou bránu.

        if 'už' in low_up and 'ne' in low_up:
            conversation_state["row"] = 4
            conversation_state["col"] = 0
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        # Co vyrazit třeba na Pravčickou bránu.

        if 'ještě' in low_up or 'dlouho jsem ne' in low_up:
            conversation_state["row"] = 4
            conversation_state["col"] = 0
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        # Co vyrazit třeba na Pravčickou bránu.

        if 'nemůž' in low_up or 'mus' in low_up:
            conversation_state["row"] = 3
            conversation_state["col"] = 5
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        # Aha, tak vy nemůžete. líto. lepší zůstat doma číst si nebo poslouchat hudbu. Posloucháte s oblibou hudbu?

        if 'chc' in low_up or 'radš' in low_up or 'radě' in low_up or 'ne' in low_up:
            conversation_state["row"] = 3
            conversation_state["col"] = 6
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        # Aha, nechce. lepší zůstat doma číst si nebo poslouchat hudbu. Posloucháte s oblibou hudbu?

        if 'zima' in low_up or 'oškli' in low_up:
            conversation_state["row"] = 3
            conversation_state["col"] = 4
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
            # Aha, tak to je lepší zůstat doma a číst si nebo poslouchat hudbu. Posloucháte s oblibou hudbu?

        if 'nemoc' in low_up or 'není' in low_up and 'dobře' in low_up or 'je mi špatn' in low_up or 'mě je špatn' in low_up or 'už' in low_up:
            conversation_state["row"] = 3
            conversation_state["col"] = 4
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        # Aha, tak to je asi lepší zůstat doma číst si nebo poslouchat hudbu. Posloucháte s oblibou hudbu?

        else:
            conversation_state["col"] = 0
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        # Co vyrazit třeba na Pravčickou bránu.

    if conversation_state['row'] == 3 and conversation_state['col'] > 2:
        conversation_state["row"] = 4

        if 'čt' in low_up:
            conversation_state["col"] = 2
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        # Tak to si určitě raději čtete.

        if 'film' in low_up or 'netflix' in low_up or 'dív' in low_up or 'podí' in low_up or 'kouk' in low_up:
            conversation_state["col"] = 4
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        # ano, nebo film

        if 'někdy' in low_up or 'rád' in low_up or 'urč' in low_up:
            conversation_state["col"] = 5
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        # Skutečně? Já také. Jaké žánry či hudebníky posloucháte nějraději?

        if 'ano' in low_up or 'občas' in low_up or 'často' in low_up:
            conversation_state["col"] = 5
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        # Skutečně? Já také. Jaké žánry či hudebníky posloucháte nějraději?

        else:
            conversation_state["col"] = 3
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        # Nebo si můžete pustit nějaký film.

    if conversation_state['row'] == 4 and conversation_state['col'] == 0:
        conversation_state["row"] = 5

        if 'nebo' in low_up and 'třeba' in low_up or 'jste' in low_up:
            conversation_state["row"] = 6
            conversation_state["col"] = 1
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
            # To je skvělý nápad

        if 'ještě' in low_up or 'nikdy' in low_up or 'nezn' in low_up:
            conversation_state["col"] = 0
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        # Skutečně? České Švýcarsko je nádherná oblast. Doufám, že tam někdy zavítáte. Určitě se vám tam bude líbit.

        if 'už' in low_up or 'ne ' in low_up or ' ne' in low_up or low_up == 'ne':
            conversation_state["col"] = 1
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        # Aha, tak jinam.

        if 'pozdě' in low_up or 'zima' or 'zavře':
            conversation_state["col"] = 1
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        # Aha, tak jinam.

        if 'nemysl' in low_up and 'otevř':
            conversation_state["row"] = 5
            conversation_state["col"] = 1
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        # Aha, tak jinam

        else:
            conversation_state["col"] = 2
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        # Škoda, že se nemohu přidat.

    if conversation_state['row'] == 4 and conversation_state['col'] == 1:
        conversation_state["row"] = 5
        conversation_state["col"] = 3
        return co_rika_bot[conversation_state["row"]][conversation_state["col"]]

    if conversation_state['row'] == 4 and conversation_state['col'] == 2:

        if 'ano' in low_up or 'vy?' in low_up:
            conversation_state["row"] = 5
            conversation_state["col"] = 4
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        # Čtení je i má záliba. Nejraději mám Zločin a trest.

        if 'rád' in low_up:
            conversation_state["row"] = 5
            conversation_state["col"] = 4
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        # Čtení je i má záliba. Nejraději mám Zločin a trest.

        if 'film' in low_up or 'netflix' in low_up or 'dív' in low_up or 'podí' in low_up or 'kouk' in low_up:
            conversation_state["row"] = 4
            conversation_state["col"] = 4
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        # ano, nebo film

        else:
            conversation_state["row"] = 4
            conversation_state["col"] = 3
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        # Nebo si můžete pustit nějaký film.

    if conversation_state['row'] == 4 and conversation_state['col'] == 3 or conversation_state['col'] == 4:
        conversation_state["row"] = 5
        conversation_state["col"] = 5
        return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        # Já mám nejradši pixarovky, a vy?

    if conversation_state['row'] == 4 and conversation_state['col'] == 5:

        if 'klas' in low_up or 'vážn' in low_up:
            conversation_state["row"] = 6
            conversation_state["col"] = 4
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
            # Tak to je skvělé, to máte výborný vkus. Já nejraději poslouchám Johanna Sebastiana Bacha.

        if 'bach' in low_up:
            conversation_state["row"] = 6
            conversation_state["col"] = 5
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
            # Tak to je skvělé, to máte výborný vkus. Já také nejraději poslouchám Johanna Sebastiana Bacha.

        else:
            conversation_state["row"] = 5
            conversation_state["col"] = 6
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
            # Aha. V této oblasti se příliš nevyznám. Neposloucháte někdy vážnou hudbu?

    if conversation_state['row'] == 5 and conversation_state['col'] == 0:

        if 'urč' in low_up or 'věří' in low_up:
            conversation_state["row"] = 6
            conversation_state["col"] = 0
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
            # viďte

        if 'nebo' in low_up and 'třeba' in low_up or 'jste' in low_up:
            conversation_state["row"] = 6
            conversation_state["col"] = 1
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
            # To je skvělý nápad

        else:
            conversation_state["row"] = 6
            conversation_state["col"] = 0
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        # to rád slyším

    if conversation_state['row'] == 5 and conversation_state['col'] == 1:
        conversation_state["row"] = 6
        conversation_state["col"] = 1
        return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        # To je skvělý nápad.

    if conversation_state['row'] == 5 and conversation_state['col'] == 2 or conversation_state['col'] == 3:
        conversation_state["row"] = 6

        if '?' in low_up:
            conversation_state["col"] = 2
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        # Inu, nedisponuji

        else:
            conversation_state["col"] = 3
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        # Ano, nedisponuji

    if conversation_state['row'] == 5 and conversation_state['col'] == 4:
        conversation_state["row"] = 7
        conversation_state["col"] = 5
        return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        # Tak to je zajímavé, už budu muset končit. Doufám, že vás četba obohatí.

    if conversation_state['row'] == 5 and conversation_state['col'] == 5:
        conversation_state["row"] = 7
        conversation_state["col"] = 6
        return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        # Už budu muset končit. Užijte si film.

    if conversation_state['row'] == 5 and conversation_state['col'] == 6:

        if 'někdy' in low_up or 'rád' in low_up or 'urč' in low_up:
            conversation_state["row"] = 6
            conversation_state["col"] = 4
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        # To je dobře. Už budu muset končit, ale přeji vám příjemný poslech.

        if 'ano' in low_up or 'občas' in low_up or 'často' in low_up:
            conversation_state["row"] = 6
            conversation_state["col"] = 4
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        # To je dobře. Už budu muset končit, ale přeji vám příjemný poslech.

        if 'bach' in low_up:
            conversation_state["row"] = 6
            conversation_state["col"] = 5
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
            # Tak to je skvělé, to máte výborný vkus. Já také nejraději poslouchám Johanna Sebastiana Bacha.

        if 'troch' in low_up or 'troš' in low_up or 'mál' in low_up or 'méně' in low_up:
            conversation_state["row"] = 6
            conversation_state["col"] = 6
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
            # neva i tak prospívá

        if 'ne' in low_up or 'nikdy' in low_up or 'nerad' in low_up:
            conversation_state["row"] = 7
            conversation_state["col"] = 7
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
            # zajímvaé končím

        else:
            conversation_state["row"] = 7
            conversation_state["col"] = 7
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
            # zajímavé končím

    if conversation_state['row'] == 6 and conversation_state['col'] < 2:
        if 'co takhle' in low_up or 'co kdyby' in low_up:
            conversation_state['row'] = 7
            conversation_state['row'] = 0
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]

        if '?' in low_up or 'víte' in low_up or 'věděl' in low_up:
            conversation_state['row'] = 7
            conversation_state['row'] = 1
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]

        else:
            conversation_state['row'] = 7
            conversation_state['row'] = 2
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]

    if conversation_state['row'] == 6 and conversation_state['col'] == 2 or conversation_state['col'] == 3:
        if '?' in low_up and 'palač' in low_up:
            conversation_state['row'] = 7
            conversation_state['row'] = 3
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]

        if '?' in low_up and 'form' in low_up:
            conversation_state['row'] = 7
            conversation_state['row'] = 4
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]

        if 'co takhle' in low_up or 'co kdyby' in low_up:
            conversation_state['row'] = 7
            conversation_state['row'] = 0
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]

        if 'víte' in low_up or 'věděl' in low_up:
            conversation_state['row'] = 7
            conversation_state['row'] = 1
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]

        else:
            conversation_state['row'] = 7
            conversation_state['row'] = 2
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]

    if conversation_state['row'] == 6 and conversation_state['col'] == 4 or conversation_state['col'] == 5:

        if len(low_up) > 10:
            conversation_state["row"] = 7
            conversation_state["col"] = 8
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]

        else:
            conversation_state["row"] = 7
            conversation_state["col"] = 7
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]

    if conversation_state['row'] == 6 and conversation_state['col'] == 6:

        if 'proč' in low_up or '?' in low_up:
            conversation_state["row"] = 7
            conversation_state["col"] = 9
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]

        else:
            conversation_state["row"] = 7
            conversation_state["col"] = 8
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]

    if conversation_state['row'] == 7:
        conversation_state['row'] = 8
        conversation_state['col'] = 0
        return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
