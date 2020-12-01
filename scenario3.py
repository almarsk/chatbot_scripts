from pathlib import Path
from corpy.morphodita import Tagger

description = """
Scénář 3 slouží k demonstraci lemmatizace a morfologického značkování
vstupů od uživatele pomocí systému MorphoDiTa.
""".strip()

# Před použitím scénáře je potřeba stáhnout model, na základě kterého se
# značkování provede, a uložit ho ve stejném adresáři jako scénář.
# Seznam dostupných modelů pro systém MorphoDiTa je zde:
# http://ufal.mff.cuni.cz/morphodita#language_models
script_dir = Path(__file__).parent
model_path = str(script_dir / "czech-morfflex-pdt-161115.tagger")
tagger = Tagger(model_path)


def reply(user_reply, nick, cs):
    tagged = list(tagger.tag(user_reply or "", convert="strip_lemma_id"))
    return f"Odpověď uživatele {nick} obohacená o lemmatizaci a morfologické značkování: {tagged}"
