from pathlib import Path
from corpy.morphodita import Tagger

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


def reply(user_reply, nick, cs):
    tagged = list(tagger.tag(user_reply or "", convert="strip_lemma_id"))
    cs.setdefault("row", 0)
    cs.setdefault("col", 0)
    if cs['row'] == 0:
        cs['row'] += 1
        return "Dobrý den, co děláte ve svém volném čase?"

    else:
        cs['row'] += 1
        if any(t.tag[0] == 'V' and t.tag[7] == '1' for t in tagged):
            prisudek_2 = {
                t.lemma
                for t in tagged
                if t.tag[7] == '2'
            }
            a= "Teda, " + str(prisudek_2) + " vůbec neumím."
            return a
        else:
            return f"V odpovědi sloveso v druhé osobě není {tagged}"
