co_rika_bot = [[],

               ['Dobrý den, já jsem zvědavobot. A vy?'],

               ['Těší mě. Dnes je hezky, že?'],

               ['Tak by bylo dobré vyrazit někam na výlet.', 'Aha, tak to je nejlepší zůstat doma a číst si nebo poslouchat hudbu. Posloucháte s oblibou hudbu?'],

               ['Co vyrazit třeba na Pravčickou bránu.', 'Aha, tak vy nemůžete. To je mi líto. Tak to je asi lepší zůstat doma číst si nebo poslouchat hudbu. Posloucháte s oblibou hudbu?', 'Aha, tak vy si raději čtete.', 'Nebo si můžete pustit nějaký film.', 'Skutečně? Já také. Jaké žánry či hudebníky posloucháte nějraději?','Aha, tak vám se nechce. To je mi líto. Tak to je asi lepší zůstat doma číst si nebo poslouchat hudbu. Posloucháte s oblibou hudbu?' ],

               ['Skutečně? České Švýcarsko je nádherná oblast. Doufám, že tam někdy zavítáte. Určitě se vám tam bude líbit.', 'Aha, tak možná někam jinam?', 'Škoda, že se nemohu přidat.', 'Čtení je i má záliba. Nejraději mám Zločin a trest.', 'Já mám nejradši pixarovky, a vy?', 'Tak to máte výborný vkus. Já nejraději poslouchám Johanna Sebastiana Bacha.', 'Aha. V této oblasti se příliš nevyznám. Neposloucháte někdy vážnou hudbu?' ],

               ['To rád slyším', 'To je skvělý nápad.', 'Inu, nedisponuji fyzickou formou, která by mohla jít na výlet. Když na to přijde, nedisponuji ani fyzickou formou, která by mohla udělat palačinky', 'Je to tak, nedisponuji zkrátka fyzickou formou, která by mohla jít na výlet. Když na to přijde, nedisponuji ani fyzickou formou, která by mohla udělat palačinky', 'Tak to je zajímavé. Budu muset končit. Doufám, že vás četba obohatí.', 'Už budu muset končit, užijte si film.', 'To je dobře. Už budu muset končit, ale přeji vám příjemný poslech.', 'To nevadí. Už budu muset končit. Přeji vám příjemný poslech.', 'Viďte', 'Do toho Švýcarska ale určitě zajeďte.' ],

               ['Už budu muset končit. Užijte si to na výletě. Můžete mi poslat pohled na www.zdvotlabot.cz', 'Rád jsem se s vámi seznámil. Tak nashle!']

               ]

description = "Zdvotlabot dovede na krátkou chvíli zdvořile tlachat."


def reply(user_reply, nick, conversation_state):
    conversation_state.setdefault("row", 0)
    conversation_state.setdefault("col", 0)
    
    if conversation_state['row']==0:
        conversation_state["row"] = 1
        return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
    #Dobrý den, já jsem zvědavobot. A vy?

    if conversation_state['row']==1:
        conversation_state["row"] = 2
        return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
    #Těší mě. Dnes je hezky, že?

    if conversation_state['row']==2:
        conversation_state["row"] = 3

        if ' ne' in user_reply:
            conversation_state["col"] = 1
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        # Aha, tak to je lepší zůstat doma a číst si nebo poslouchat hudbu. Posloucháte s oblibou hudbu?

        else:
            conversation_state["col"] = 0
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        #Tak by bylo dobré vyrazit někam na výlet.

    if conversation_state['row'] == 3 and conversation_state['col'] == 0:
        conversation_state["row"] = 4

        if any(['můž' in user_reply, 'mus' in user_reply]):
            conversation_state["col"] = 1
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        # Aha, tak vy nemůžete. To je mi líto. Tak to je asi lepší zůstat doma číst si nebo poslouchat hudbu. Posloucháte s oblibou hudbu?

        if any(['chc' in user_reply, 'radš' in user_reply,'radě' in user_reply,]):
            conversation_state["col"] = 5
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        # Aha, tak vám se nechce. Tak to je asi lepší zůstat doma číst si nebo poslouchat hudbu. Posloucháte s oblibou hudbu?

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

        if 'ano' in user_reply:
            conversation_state["col"] = 4
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        #Skutečně? Já také. Jaké žánry či hudebníky posloucháte nějraději?

        if 'občas' in user_reply:
            conversation_state["col"] = 4
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        #Skutečně? Já také. Jaké žánry či hudebníky posloucháte nějraději?

        if 'často' in user_reply:
            conversation_state["col"] = 4
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        #Skutečně? Já také. Jaké žánry či hudebníky posloucháte nějraději?

        if 'někdy' in user_reply:
            conversation_state["col"] = 4
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        #Skutečně? Já také. Jaké žánry či hudebníky posloucháte nějraději?

        if 'rád' in user_reply:
            conversation_state["col"] = 4
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        #Skutečně? Já také. Jaké žánry či hudebníky posloucháte nějraději?

        if 'urč' in user_reply:
            conversation_state["col"] = 4
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        # Skutečně? Já také. Jaké žánry či hudebníky posloucháte nějraději?

        else:
            conversation_state["col"] = 3
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        #Nebo si můžete pustit nějaký film.

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

        else:
            conversation_state["col"] = 2
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        #Škoda, že se nemohu přidat.

    if conversation_state['row'] == 4 and conversation_state['col'] == 1:

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

        if 'urč' in user_reply:
            conversation_state["col"] = 4
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        # Skutečně? Já také. Jaké žánry či hudebníky posloucháte nějraději?

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

        if 'urč' in user_reply:
            conversation_state["col"] = 4
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        # Skutečně? Já také. Jaké žánry či hudebníky posloucháte nějraději?

        else:
            conversation_state["col"] = 3
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        #Nebo si můžete pustit nějaký film.

    if conversation_state['row'] == 5 and conversation_state['col'] == 0:
        if not 'taky' in user_reply:
            if 'tak' in user_reply:
                conversation_state["row"] = 6
                conversation_state["col"] = 0
                return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
                #To rád slyším

            if 'urč' in user_reply:
                conversation_state["row"] = 6
                conversation_state["col"] = 8
                return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
                #viďte
            else:
                conversation_state["row"] = 6
                conversation_state["col"] = 9
                return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
                # do toho švýcarska ale určitě zajeďte

        else:
            conversation_state["row"] = 6
            conversation_state["col"] = 8
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
            #do toho švýcarska ale určitě zajeďte

    if conversation_state['row'] == 5 and conversation_state['col'] == 1:
        conversation_state["row"] = 6
        conversation_state["col"] = 1
        return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        #To je skvělý nápad.

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

        if '?' in user_reply:
            conversation_state["col"] = 5
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        # skvělé

        if 'ano' in user_reply:
            conversation_state["col"] = 5
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        # skvělé

        if 'jo' in user_reply:
            conversation_state["col"] = 5
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        # skvělé

        if 'občas' in user_reply:
            conversation_state["col"] = 5
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        # skvělé

        if 'kdy' in user_reply:
            conversation_state["col"] = 5
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        # skvělé

        else:
            conversation_state["row"] = 6
            conversation_state["col"] = 7
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]
        # Ano, nedisponuji

    if conversation_state['row'] == 6:
        if conversation_state['col'] == 0:
            conversation_state["row"] = 7
            conversation_state["col"] = 0
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]

        if conversation_state['col'] == 1:
            conversation_state["row"] = 7
            conversation_state["col"] = 0
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]

        if conversation_state['col'] == 2:
            conversation_state["row"] = 7
            conversation_state["col"] = 0
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]

        if conversation_state['col'] == 3:
            conversation_state["row"] = 7
            conversation_state["col"] = 0
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]

        if  conversation_state['col'] == 4:
            conversation_state["row"] = 7
            conversation_state["col"] = 1
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]

        if  conversation_state['col'] == 5:
            conversation_state["row"] = 7
            conversation_state["col"] = 1
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]

        if  conversation_state['col'] == 6:
            conversation_state["row"] = 7
            conversation_state["col"] = 1
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]

        if  conversation_state['col'] == 7:
            conversation_state["row"] = 7
            conversation_state["col"] = 1
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]

        if  conversation_state['col'] == 8:
            conversation_state["row"] = 7
            conversation_state["col"] = 0
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]

        if  conversation_state['col'] == 9:
            conversation_state["row"] = 7
            conversation_state["col"] = 0
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]

    if conversation_state['row'] == 7 and conversation_state['col'] == 0:
            conversation_state["col"] = 1
            return co_rika_bot[conversation_state["row"]][conversation_state["col"]]