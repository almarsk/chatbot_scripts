from pathlib import Path
from corpy.morphodita import Tagger

description = """
Lemmobot dovede rozeznat slovesa v druhé osobě ve vstupech od uživatele pomocí systému MorphoDita.
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


def reply(user_reply, nick, conversation_state):

        return f"bylo užito sloveso v druhé osobě"