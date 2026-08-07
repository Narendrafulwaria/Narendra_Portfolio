import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import utils.chatbot_engine as chatbot_engine


def test_get_response_falls_back_without_warning(monkeypatch):
    warnings = []
    monkeypatch.setattr(chatbot_engine.st, "warning", lambda msg: warnings.append(msg))
    monkeypatch.setattr(chatbot_engine, "_has_groq_key", lambda: True)

    def fail(*args, **kwargs):
        raise RuntimeError("simulated Groq failure")

    monkeypatch.setattr(chatbot_engine, "_groq_response", fail)

    response = chatbot_engine.get_response("Tell me about your projects", [])

    assert "Narendra has built 5 projects" in response
    assert warnings == []
