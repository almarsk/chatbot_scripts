description = "Scénář 1 není určen ke zdvořilostní konverzaci, nýbrž pouze k testování."
bg_color = "blue"
heading_color = "green"
heading_outline = "red"


def reply(user_reply, nick, conversation_state):
    conversation_state.setdefault("x", 0)
    conversation_state["x"] += 1
    return f"Ahoj! Jsem bot ze scénáře 1. Mluvím s uživatelem {nick!r}. Konverzace je ve stavu {conversation_state}. Poslední replika uživatele byla: {user_reply!r}."
