from pathlib import Path
from corpy.morphodita import Tagger

description = """
Lemmobot dovede rozeznat slovesa v druhé osobě ve vstupech od uživatele pomocí systému MorphoDita.
""".strip()

bg_color = "#F0FFFF"
heading_color = "#00e673"
reply_bg = "#ccffff"
reply_outline = "#000"

# Před použitím scénáře je potřeba stáhnout model, na základě kterého se
# značkování provede, a uložit ho ve stejném adresáři jako scénář.
# Seznam dostupných modelů pro systém MorphoDiTa je zde:
# http://ufal.mff.cuni.cz/morphodita#language_models
script_dir = Path(__file__).parent
model_path = str(script_dir / "czech-morfflex-pdt-161115" / "czech-morfflex-pdt-161115.tagger")
tagger = Tagger(model_path)

def reply(user_reply, nick, conversation_state):
    low_up = str(user_reply).lower()
    conversation_state.setdefault("row", 0)
    conversation_state.setdefault("col", 0)
    tagged = list(tagger.tag(user_reply or "", convert="strip_lemma_id"))

    if all(t.tag[10] == "N" for t in tagged and t.tag[8] == "2" for t in tagged):
        conversation_state['row'] = 1
        return f"{t.lemma}"