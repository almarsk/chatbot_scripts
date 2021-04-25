from pathlib import Path
from corpy.morphodita import Tagger
from ufal.morphodita import TaggedLemmasForms

description = """
Scénář 3 slouží k demonstraci lemmatizace a morfologického značkování
vstupů od uživatele pomocí systému MorphoDiTa.
""".strip()

# Před použitím scénáře je potřeba stáhnout model, na základě kterého se
# značkování provede, a uložit ho ve stejném adresáři jako scénář.
# Seznam dostupných modelů pro systém MorphoDiTa je zde:
# http://ufal.mff.cuni.cz/morphodita#language_models
script_dir = Path(__file__).parent
model_path = str(script_dir / "czech-morfflex-pdt-161115" / "czech-morfflex-pdt-161115.tagger")
tagger = Tagger(model_path)


def reply(user_reply, nick, cs):
    tagged = list(tagger.tag(user_reply or "", convert="strip_lemma_id"))
    přísudek = []
    for token in tagged:
        if token.tag[0]== "V":
            přísudek.append(token.lemma)

    return f"{přísudek}"


print(reply("Okolí na Křístkovi oceňovalo přátelský a kolegiální přístup, vstřícnost ke studentům a vlídný humor.","test", {"row":1, "col":1}))

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

print("Všechny tvary lemmatu plést:")
tagger.generate("plést")
print()
print("Jen tvary, které jsou dle tagu slovesa v 2. os. pl.:")
tagger.generate("plést", "V??P???2")
print()
print("Ten, který patrně chcete:")
tagger.generate("plést", "VB-P---2P-AA")
