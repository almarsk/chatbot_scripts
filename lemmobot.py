from pathlib import Path
from corpy.morphodita import Tagger
from ufal.morphodita import TaggedLemmasForms

description = """
Lemmobot dovede hlásit užití sloves v druhé osobě ve vstupech od uživatele pomocí systému MorphoDita.
""".strip()

bg_color = "#dbaf7d"
heading_color = "#c28a4a"
reply_bg = "#9e7d3a"
reply_outline = "#a35e0f"

# Před použitím scénáře je potřeba stáhnout model, na základě kterého se
# značkování provede, a uložit ho ve stejném adresáři jako scénář.
# Seznam dostupných modelů pro systém MorphoDiTa je zde:
# http://ufal.mff.cuni.cz/morphodita#language_models
script_dir = Path(__file__).parent
model_path = str(script_dir / "czech-morfflex-pdt-161115" / "czech-morfflex-pdt-161115.tagger")
tagger = Tagger(model_path)

def generate(tagger: Tagger, lemma: str, tag_wildcard: str = None):
    """Vygeneruje tvary pro dané lemma na základě morfologie z taggeru.

    Výsledky lze omezit jen na některé tvary pomocí tag_wildcard, což je
    řetězec ve formátu popsaném zde:
    <http://ufal.mff.cuni.cz/morphodita/api-tutorial#tutorial_tag_wildcard>

    """
    # generování se nedělá pomocí taggeru, ale pomocí morfologického
    # slovníku, který je součástí taggeru a je tedy potřeba jej z něj
    # nejprve vytáhnout
    morpho = tagger._tagger.getMorpho()
    results = TaggedLemmasForms()
    morpho.generate(lemma, tag_wildcard, morpho.GUESSER, results)

    # výsledků může být víc (záleží na tag_wildcard)
    for lemma in results:
        for form in lemma.forms:
            # pro testovací účely prostě všechny vygenerované výsledky
            # vytiskneme (tvar, lemma i tag)...
            print(form.form, lemma.lemma, form.tag, sep="\t")
            # ... ale v chatbotu patrně asi spíš budete chtít vrátit
            # prostě první vygenerovaný tvar? ↓
            # return form.form

# tímhle dodatečně přidáme funkci generate jako metodu na třídu Tagger,
# což není nutné, ale umožní nám to ji volat jako `tagger.generate(...)`
# místo `generate(tagger, ...)`
Tagger.generate = generate

def gen_rep(user_reply, nick):
    tagged = list(tagger.tag(user_reply or "", convert="strip_lemma_id"))

    tagged_dict = tagged.dict.fromkeys()

    if any(t.tag[7] == '2' for t in tagged):
        verb = [
            t.lemma
            for t in tagged
            if t.tag[7] == '2'
        ]

        if verb[0] == 'dělat':
            return 'Většinou čekám, až si se mnou začne někdo povídat.'





def reply(user_reply, nick, cs):
    tagged = list(tagger.tag(text = user_reply or "", sents=True, convert="strip_lemma_id"))
    cs.setdefault("row", 0)
    cs.setdefault("col", 0)


    if cs['row'] == 0:
        cs['row'] += 1
        return "Dobrý den"

    else:
        cs['row'] += 1
        return gen_rep(user_reply, nick)





