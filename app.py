import sqlalchemy
from flask import Flask, render_template, request, redirect, session
import datetime



d = dict(row=0, col=0)

co_rika_bot = [[],

               ['Dobrý den, já jsem zvědavobot. A vy?'],

               ['Těší mě. Dnes je hezky, že?'],

               ['Tak by bylo dobré vyrazit někam na výlet.', 'Aha, tak to je lepší zůstat doma a číst si nebo poslouchat hudbu. Posloucháte s oblibou hudbu?'],

               ['Co vyrazit třeba na Pravčickou bránu.', 'Aha, tak vy nemůžete. To je mi líto. Tak to je asi lepší zůstat doma číst si nebo poslouchat hudbu. Posloucháte s oblibou hudbu?', 'Aha, tak vy si raději čtete.', 'Nebo si můžete pustit nějaký film.', 'Skutečně? Já také. Jaké žánry či hudebníky posloucháte nějraději?','Aha, tak vám se nechce. To je mi líto. Tak to je asi lepší zůstat doma číst si nebo poslouchat hudbu. Posloucháte s oblibou hudbu?' ],

               ['Skutečně? České Švýcarsko je nádherná oblast. Doufám, že tam někdy zavítáte. Určitě se vám tam bude líbit.', 'Aha, tak možná někam jinam?', 'Škoda, že se nemohu přidat.', 'Čtení je i má záliba. Nejraději mám Zločin a trest.', 'Já mám nejradši pixarovky, a vy?', 'Tak to máte výborný vkus. Já nejraději poslouchám Johanna Sebastiana Bacha.', 'Aha. V této oblasti se příliš nevyznám. Neposloucháte někdy vážnou hudbu?' ],

               ['To rád slyším', 'To je skvělý nápad.', 'Inu, nedisponuji fyzickou formou, která by mohla jít na výlet. Když na to přijde, nedisponuji ani fyzickou formou, která by mohla udělat palačinky', 'Je to tak, nedisponuji zkrátka fyzickou formou, která by mohla jít na výlet. Když na to přijde, nedisponuji ani fyzickou formou, která by mohla udělat palačinky', 'Tak to je zajímavé. Budu muset končit. Doufám, že vás četba obohatí.', 'Už budu muset končit, užijte si film.', 'To je dobře. Už budu muset končit, ale přeji vám příjemný poslech.', 'To nevadí. Už budu muset končit. Přeji vám příjemný poslech.', 'Viďte', 'Do toho Švýcarska ale určitě zajeďte.' ],

               ['Už budu muset končit. Užijte si to na výletě. Můžete mi poslat pohled na www.zdvotlabot.cz', 'Rád jsem se s vámi seznámil. Tak nashle!']

               ]

def rplx(odp, row_col_dict):
    if d['row']==0:
        row_col_dict["row"] = 1
        return co_rika_bot[row_col_dict["row"]][row_col_dict["col"]]
    #Dobrý den, já jsem zvědavobot. A vy?

    if d['row']==1:
        row_col_dict["row"] = 2
        return co_rika_bot[row_col_dict["row"]][row_col_dict["col"]]
    #Těší mě. Dnes je hezky, že?

    if d['row']==2:
        row_col_dict["row"] = 3

        if ' ne' in odp:
            row_col_dict["col"] = 1
            return co_rika_bot[row_col_dict["row"]][row_col_dict["col"]]
        # Aha, tak to je lepší zůstat doma a číst si nebo poslouchat hudbu. Posloucháte s oblibou hudbu?

        else:
            row_col_dict["col"] = 0
            return co_rika_bot[row_col_dict["row"]][row_col_dict["col"]]
        #Tak by bylo dobré vyrazit někam na výlet.

    if d['row'] == 3 and d['col'] == 0:
        row_col_dict["row"] = 4

        if any(['můž' in odp, 'mus' in odp]):
            row_col_dict["col"] = 1
            return co_rika_bot[row_col_dict["row"]][row_col_dict["col"]]
        # Aha, tak vy nemůžete. To je mi líto. Tak to je asi lepší zůstat doma číst si nebo poslouchat hudbu. Posloucháte s oblibou hudbu?

        if any(['chc' in odp, 'radš' in odp,'radě' in odp,]):
            row_col_dict["col"] = 5
            return co_rika_bot[row_col_dict["row"]][row_col_dict["col"]]
        # Aha, tak vám se nechce. Tak to je asi lepší zůstat doma číst si nebo poslouchat hudbu. Posloucháte s oblibou hudbu?

        else:
            row_col_dict["col"] = 0
            return co_rika_bot[row_col_dict["row"]][row_col_dict["col"]]
        #Co vyrazit třeba na Pravčickou bránu.

    if d['row'] == 3 and d['col'] == 1:
        row_col_dict["row"] = 4

        if 'čt' in odp:
            row_col_dict["col"] = 2
            return co_rika_bot[row_col_dict["row"]][row_col_dict["col"]]
        #Tak to si určitě raději čtete.

        if 'ano' in odp:
            row_col_dict["col"] = 4
            return co_rika_bot[row_col_dict["row"]][row_col_dict["col"]]
        #Skutečně? Já také. Jaké žánry či hudebníky posloucháte nějraději?

        if 'občas' in odp:
            row_col_dict["col"] = 4
            return co_rika_bot[row_col_dict["row"]][row_col_dict["col"]]
        #Skutečně? Já také. Jaké žánry či hudebníky posloucháte nějraději?

        if 'často' in odp:
            row_col_dict["col"] = 4
            return co_rika_bot[row_col_dict["row"]][row_col_dict["col"]]
        #Skutečně? Já také. Jaké žánry či hudebníky posloucháte nějraději?

        if 'někdy' in odp:
            row_col_dict["col"] = 4
            return co_rika_bot[row_col_dict["row"]][row_col_dict["col"]]
        #Skutečně? Já také. Jaké žánry či hudebníky posloucháte nějraději?

        if 'rád' in odp:
            row_col_dict["col"] = 4
            return co_rika_bot[row_col_dict["row"]][row_col_dict["col"]]
        #Skutečně? Já také. Jaké žánry či hudebníky posloucháte nějraději?

        if 'urč' in odp:
            row_col_dict["col"] = 4
            return co_rika_bot[row_col_dict["row"]][row_col_dict["col"]]
        # Skutečně? Já také. Jaké žánry či hudebníky posloucháte nějraději?

        else:
            row_col_dict["col"] = 3
            return co_rika_bot[row_col_dict["row"]][row_col_dict["col"]]
        #Nebo si můžete pustit nějaký film.

    if d['row'] == 4 and d['col'] == 0:
        row_col_dict["row"] = 5

        if 'ještě' in odp:
            row_col_dict["col"] = 0
            return co_rika_bot[row_col_dict["row"]][row_col_dict["col"]]
        #Skutečně? České Švýcarsko je nádherná oblast. Doufám, že tam někdy zavítáte. Určitě se vám tam bude líbit.

        if 'nikdy' in odp:
            row_col_dict["col"] = 0
            return co_rika_bot[row_col_dict["row"]][row_col_dict["col"]]
        #Skutečně? České Švýcarsko je nádherná oblast. Doufám, že tam někdy zavítáte. Určitě se vám tam bude líbit.

        if 'nezn' in odp:
            row_col_dict["col"] = 0
            return co_rika_bot[row_col_dict["row"]][row_col_dict["col"]]
        #Skutečně? České Švýcarsko je nádherná oblast. Doufám, že tam někdy zavítáte. Určitě se vám tam bude líbit.

        if any(['už' in odp, 'ano' in odp]):
            row_col_dict["col"] = 1
            return co_rika_bot[row_col_dict["row"]][row_col_dict["col"]]
        #Aha, tak jinam.

        else:
            row_col_dict["col"] = 2
            return co_rika_bot[row_col_dict["row"]][row_col_dict["col"]]
        #Škoda, že se nemohu přidat.

    if d['row'] == 4 and d['col'] == 1:

        if 'čt' in odp:
            row_col_dict["col"] = 2
            return co_rika_bot[row_col_dict["row"]][row_col_dict["col"]]
        #Tak to si určitě raději čtete.

        if 'ano' in odp:
            row_col_dict["col"] = 4
            return co_rika_bot[row_col_dict["row"]][row_col_dict["col"]]
        # Skutečně? Já také. Jaké žánry či hudebníky posloucháte nějraději?

        if 'občas' in odp:
            row_col_dict["col"] = 4
            return co_rika_bot[row_col_dict["row"]][row_col_dict["col"]]
        # Skutečně? Já také. Jaké žánry či hudebníky posloucháte nějraději?

        if 'často' in odp:
            row_col_dict["col"] = 4
            return co_rika_bot[row_col_dict["row"]][row_col_dict["col"]]
        # Skutečně? Já také. Jaké žánry či hudebníky posloucháte nějraději?

        if 'někdy' in odp:
            row_col_dict["col"] = 4
            return co_rika_bot[row_col_dict["row"]][row_col_dict["col"]]
        # Skutečně? Já také. Jaké žánry či hudebníky posloucháte nějraději?

        if 'rád' in odp:
            row_col_dict["col"] = 4
            return co_rika_bot[row_col_dict["row"]][row_col_dict["col"]]
        # Skutečně? Já také. Jaké žánry či hudebníky posloucháte nějraději?

        if 'urč' in odp:
            row_col_dict["col"] = 4
            return co_rika_bot[row_col_dict["row"]][row_col_dict["col"]]
        # Skutečně? Já také. Jaké žánry či hudebníky posloucháte nějraději?

        else:
            row_col_dict["col"] = 3
            return co_rika_bot[row_col_dict["row"]][row_col_dict["col"]]
        #Nebo si můžete pustit nějaký film.

    if d['row'] == 4 and d['col'] == 2:

        if 'ano' in odp:
            row_col_dict["row"] = 5
            row_col_dict["col"] = 3
            return co_rika_bot[row_col_dict["row"]][row_col_dict["col"]]
        #Čtení je i má záliba. Nejraději mám Zločin a trest.

        if 'rád' in odp:
            row_col_dict["row"] = 5
            row_col_dict["col"] = 3
            return co_rika_bot[row_col_dict["row"]][row_col_dict["col"]]
        #Čtení je i má záliba. Nejraději mám Zločin a trest.

        else:
            row_col_dict["col"] = 3
            return co_rika_bot[row_col_dict["row"]][row_col_dict["col"]]
        #Nebo si můžete pustit nějaký film.

    if d['row'] == 4 and d['col'] == 3:
        row_col_dict["row"] = 5
        row_col_dict["col"] = 4
        return co_rika_bot[row_col_dict["row"]][row_col_dict["col"]]
        #Já mám nejradši pixarovky, a vy?

    if d['row'] == 4 and d['col'] == 4:
        row_col_dict["row"] = 5

        if 'klas' in odp:
            row_col_dict["col"] = 5
            return co_rika_bot[row_col_dict["row"]][row_col_dict["col"]]
            # Tak to je skvělé, to máte výborný vkus. Já nejraději poslouchám Johanna Sebastiana Bacha.

        if 'Bach' in odp:
            row_col_dict["col"] = 5
            return co_rika_bot[row_col_dict["row"]][row_col_dict["col"]]
            # Tak to je skvělé, to máte výborný vkus. Já nejraději poslouchám Johanna Sebastiana Bacha.

        if 'vážn' in odp:
            row_col_dict["col"] = 5
            return co_rika_bot[row_col_dict["row"]][row_col_dict["col"]]
            # Tak to je skvělé, to máte výborný vkus. Já nejraději poslouchám Johanna Sebastiana Bacha.

        else:
            row_col_dict["col"] = 6
            return co_rika_bot[row_col_dict["row"]][row_col_dict["col"]]
             #Aha. V této oblasti se příliš nevyznám. Neposloucháte někdy vážnou hudbu?

    if d['row'] == 4 and d['col'] == 5:

        if 'čt' in odp:
            row_col_dict["col"] = 2
            return co_rika_bot[row_col_dict["row"]][row_col_dict["col"]]
        #Tak to si určitě raději čtete.

        if 'ano' in odp:
            row_col_dict["col"] = 4
            return co_rika_bot[row_col_dict["row"]][row_col_dict["col"]]
        # Skutečně? Já také. Jaké žánry či hudebníky posloucháte nějraději?

        if 'občas' in odp:
            row_col_dict["col"] = 4
            return co_rika_bot[row_col_dict["row"]][row_col_dict["col"]]
        # Skutečně? Já také. Jaké žánry či hudebníky posloucháte nějraději?

        if 'často' in odp:
            row_col_dict["col"] = 4
            return co_rika_bot[row_col_dict["row"]][row_col_dict["col"]]
        # Skutečně? Já také. Jaké žánry či hudebníky posloucháte nějraději?

        if 'někdy' in odp:
            row_col_dict["col"] = 4
            return co_rika_bot[row_col_dict["row"]][row_col_dict["col"]]
        # Skutečně? Já také. Jaké žánry či hudebníky posloucháte nějraději?

        if 'rád' in odp:
            row_col_dict["col"] = 4
            return co_rika_bot[row_col_dict["row"]][row_col_dict["col"]]
        # Skutečně? Já také. Jaké žánry či hudebníky posloucháte nějraději?

        if 'urč' in odp:
            row_col_dict["col"] = 4
            return co_rika_bot[row_col_dict["row"]][row_col_dict["col"]]
        # Skutečně? Já také. Jaké žánry či hudebníky posloucháte nějraději?

        else:
            row_col_dict["col"] = 3
            return co_rika_bot[row_col_dict["row"]][row_col_dict["col"]]
        #Nebo si můžete pustit nějaký film.

    if d['row'] == 5 and d['col'] == 0:
        if not 'taky' in odp:
            if 'tak' in odp:
                row_col_dict["row"] = 6
                row_col_dict["col"] = 0
                return co_rika_bot[row_col_dict["row"]][row_col_dict["col"]]
                #To rád slyším

            if 'urč' in odp:
                row_col_dict["row"] = 6
                row_col_dict["col"] = 8
                return co_rika_bot[row_col_dict["row"]][row_col_dict["col"]]
                #viďte
            else:
                row_col_dict["row"] = 6
                row_col_dict["col"] = 9
                return co_rika_bot[row_col_dict["row"]][row_col_dict["col"]]
                # do toho švýcarska ale určitě zajeďte

        else:
            row_col_dict["row"] = 6
            row_col_dict["col"] = 8
            return co_rika_bot[row_col_dict["row"]][row_col_dict["col"]]
            #do toho švýcarska ale určitě zajeďte

    if d['row'] == 5 and d['col'] == 1:
        row_col_dict["row"] = 6
        row_col_dict["col"] = 1
        return co_rika_bot[row_col_dict["row"]][row_col_dict["col"]]
        #To je skvělý nápad.

    if d['row'] == 5 and d['col'] == 2:
        row_col_dict["row"] = 6

        if '?' in odp:
            row_col_dict["col"] = 2
            return co_rika_bot[row_col_dict["row"]][row_col_dict["col"]]
        # Inu, nedisponuji

        else:
            row_col_dict["col"] = 3
            return co_rika_bot[row_col_dict["row"]][row_col_dict["col"]]
        # Ano, nedisponuji

    if d['row'] == 5 and d['col'] == 3:
        row_col_dict["row"] = 6
        row_col_dict["col"] = 4
        return co_rika_bot[row_col_dict["row"]][row_col_dict["col"]]
        #Tak to je zajímavé, už budu muset končit. Doufám, že vás četba obohatí.

    if d['row'] == 5 and d['col'] == 4:
        row_col_dict["row"] = 6
        row_col_dict["col"] = 5
        return co_rika_bot[row_col_dict["row"]][row_col_dict["col"]]
        #Už budu muset končit. Užijte si film.

    if d['row'] == 5 and d['col'] == 5:
        row_col_dict["row"] = 6
        row_col_dict["col"] = 6
        return co_rika_bot[row_col_dict["row"]][row_col_dict["col"]]
        #To je dobře. Už budu muset končit, ale přeji vám příjemný poslech.

    if d['row'] == 5 and d['col'] == 6:

        if '?' in odp:
            row_col_dict["col"] = 5
            return co_rika_bot[row_col_dict["row"]][row_col_dict["col"]]
        # Inu, nedisponuji

        else:
            row_col_dict["row"] = 6
            row_col_dict["col"] = 7
            return co_rika_bot[row_col_dict["row"]][row_col_dict["col"]]
        # Ano, nedisponuji

    if d['row'] == 6:
        if d['col'] == 0:
            row_col_dict["row"] = 7
            row_col_dict["col"] = 0
            return co_rika_bot[row_col_dict["row"]][row_col_dict["col"]]

        if d['col'] == 1:
            row_col_dict["row"] = 7
            row_col_dict["col"] = 0
            return co_rika_bot[row_col_dict["row"]][row_col_dict["col"]]

        if d['col'] == 2:
            row_col_dict["row"] = 7
            row_col_dict["col"] = 0
            return co_rika_bot[row_col_dict["row"]][row_col_dict["col"]]

        if d['col'] == 3:
            row_col_dict["row"] = 7
            row_col_dict["col"] = 0
            return co_rika_bot[row_col_dict["row"]][row_col_dict["col"]]

        if  d['col'] == 4:
            row_col_dict["row"] = 7
            row_col_dict["col"] = 1
            return co_rika_bot[row_col_dict["row"]][row_col_dict["col"]]

        if  d['col'] == 5:
            row_col_dict["row"] = 7
            row_col_dict["col"] = 1
            return co_rika_bot[row_col_dict["row"]][row_col_dict["col"]]

        if  d['col'] == 6:
            row_col_dict["row"] = 7
            row_col_dict["col"] = 1
            return co_rika_bot[row_col_dict["row"]][row_col_dict["col"]]

        if  d['col'] == 7:
            row_col_dict["row"] = 7
            row_col_dict["col"] = 1
            return co_rika_bot[row_col_dict["row"]][row_col_dict["col"]]

        if  d['col'] == 8:
            row_col_dict["row"] = 7
            row_col_dict["col"] = 0
            return co_rika_bot[row_col_dict["row"]][row_col_dict["col"]]

        if  d['col'] == 9:
            row_col_dict["row"] = 7
            row_col_dict["col"] = 0
            return co_rika_bot[row_col_dict["row"]][row_col_dict["col"]]

    if d['row'] == 7 and d['col'] == 0:
            row_col_dict["col"] = 1
            return co_rika_bot[row_col_dict["row"]][row_col_dict["col"]]

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///repliky.db'
#db = SQLAlchemy(app)
app.config['SECRET_KEY'] = 'a_random_string'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/intro", methods=['GET', 'POST'])
def intro():
    if request.method == "POST":
        if request.form.get("uziv"):
            return redirect('/chat')

        else:
            return redirect('/')

    if request.method == "GET":
        return render_template("intro.html")

@app.route("/chat", methods=['GET', 'POST'])
def chat():
    print(request.form)
    if request.method == "POST":
        if request.form.get("odpik"):
            post_odp = request.form['odp']
            corb = rplx(post_odp, d)
            if not corb:
                return redirect('outro')

            else:
                opn = open("prepistest.txt", "a")
                opn.write(f"\n\nuživatel:{post_odp}\n"f"\nzvědavobot:{corb}")
                opn.close()
                return render_template('/chat.html', crb=corb)

        elif request.form.get("ukončit"):
            opn = open("prepistest", "a")
            opn.write("respondent shledal konverzaci npeřirozenou")
            opn.close()
            return redirect('/outro')

        else:
            corb = rplx('', d)
            opn = open("prepistest.txt", "a")
            opn.write(f"\nzvědavobot:{corb}")
            opn.close()
            return render_template("chat.html", crb=corb)

    if request.method == 'GET':
        corb = rplx('', d)
        opn = open("prepistest.txt", "a")
        opn.write(f"\nzvědavobot:{corb}")
        opn.close()
        return render_template("chat.html", crb = corb)

@app.route("/outro", methods=['GET', 'POST'])
def outro():

    if request.method == "GET":
        return render_template("outro.html")

    if request.method == "POST":
        číslo = request.form['chov']
        koment = request.form['komnt']
        opn = open("prepistest", "a")
        opn.write("\n\nrespondent ohodnotil chování bota známkou: " + číslo + "\n\nkomentář: " + koment)
        opn.close()
        return redirect('/konec')

@app.route("/konec", methods=['GET', 'POST'])
def konec():

    if request.method == "GET":
        return render_template("konec.html")



if __name__ == "__main__":
    app.run(debug=True)
