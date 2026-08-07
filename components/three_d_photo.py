# components/three_d_photo.py — 3D tilt card effect via st.components.v1.html()
import base64
import os
import streamlit as st
import streamlit.components.v1 as components


def render_3d_photo(image_path: str = "assets/profile_placeholder.png", height: int = 340):
    """
    Renders a 3D perspective-tilt card around the profile photo.
    Uses pure HTML/CSS/JS injected via st.components.v1.html().
    Falls back gracefully if the image file does not exist yet.
    """
    # Encode image to base64 so it works in both local and cloud environments
    img_src = _load_image_b64(image_path)

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <style>
      * {{ margin: 0; padding: 0; box-sizing: border-box; }}

      body {{
        background: transparent;
        display: flex;
        justify-content: center;
        align-items: center;
        min-height: {height}px;
        overflow: hidden;
      }}

      .scene {{
        width: 240px;
        height: 280px;
        perspective: 700px;
      }}

      .card-3d {{
        width: 100%;
        height: 100%;
        position: relative;
        border-radius: 20px;
        transform-style: preserve-3d;
        transition: transform 0.08s linear, box-shadow 0.2s ease;
        cursor: pointer;
        box-shadow: 0 20px 60px rgba(37, 99, 235, 0.2);
        background: linear-gradient(145deg, #FFFFFF, #EFF6FF);
        border: 2px solid rgba(37, 99, 235, 0.35);
        overflow: hidden;
      }}

      .card-3d img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
        border-radius: 18px;
        display: block;
      }}

      /* Glare overlay */
      .glare {{
        position: absolute;
        inset: 0;
        border-radius: 18px;
        background: radial-gradient(
          ellipse at var(--mx, 50%) var(--my, 50%),
          rgba(255,255,255,0.18) 0%,
          transparent 65%
        );
        pointer-events: none;
        transition: opacity 0.2s ease;
        opacity: 0;
        z-index: 2;
      }}

      /* Floating ring glow behind card */
      .glow-ring {{
        position: absolute;
        width: 260px;
        height: 300px;
        border-radius: 22px;
        border: 1px solid rgba(37, 99, 235, 0.2);
        top: -10px;
        left: -10px;
        pointer-events: none;
        animation: pulseRing 3s ease-in-out infinite;
      }}

      @keyframes pulseRing {{
        0%,100% {{ box-shadow: 0 0 20px rgba(37,99,235,0.15); opacity: 0.6; }}
        50%      {{ box-shadow: 0 0 40px rgba(37,99,235,0.3); opacity: 1.0; }}
      }}

      /* Placeholder shown when no image is provided */
      .placeholder {{
        width: 100%;
        height: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        background: linear-gradient(145deg, #EFF6FF, #FFFFFF);
        border-radius: 18px;
        color: #475569;
        gap: 0.75rem;
      }}

      .placeholder .avatar-icon {{
        font-size: 5rem;
        line-height: 1;
      }}

      .placeholder .avatar-text {{
        font-size: 0.85rem;
        font-family: sans-serif;
        color: #64748B;
      }}
    </style>
    </head>
    <body>
      <div class="scene">
        <div class="glow-ring"></div>
        <div class="card-3d" id="card">
          {"<img src='" + img_src + "' alt='Narendra Fulwaria' />" if img_src else _placeholder_html()}
          <div class="glare" id="glare"></div>
        </div>
      </div>

      <script>
        const card  = document.getElementById('card');
        const glare = document.getElementById('glare');
        const MAX_TILT = 18;

        card.addEventListener('mousemove', (e) => {{
          const rect = card.getBoundingClientRect();
          const cx   = rect.left + rect.width  / 2;
          const cy   = rect.top  + rect.height / 2;
          const dx   = (e.clientX - cx) / (rect.width  / 2);   // -1 to +1
          const dy   = (e.clientY - cy) / (rect.height / 2);   // -1 to +1

          const rotY =  dx * MAX_TILT;
          const rotX = -dy * MAX_TILT;

          card.style.transform =
            `perspective(700px) rotateX(${{rotX}}deg) rotateY(${{rotY}}deg) scale(1.04)`;
          card.style.boxShadow =
            `${{-dx*20}}px ${{dy*20}}px 60px rgba(37,99,235,0.35)`;

          // Move glare with cursor
          const mx = ((e.clientX - rect.left) / rect.width  * 100).toFixed(1);
          const my = ((e.clientY - rect.top)  / rect.height * 100).toFixed(1);
          glare.style.setProperty('--mx', mx + '%');
          glare.style.setProperty('--my', my + '%');
          glare.style.opacity = '1';
        }});

        card.addEventListener('mouseleave', () => {{
          card.style.transform =
            'perspective(700px) rotateX(0deg) rotateY(0deg) scale(1)';
          card.style.boxShadow =
            '0 20px 60px rgba(37,99,235,0.2)';
          glare.style.opacity  = '0';
        }});
      </script>
    </body>
    </html>
    """
    components.html(html, height=height, scrolling=False)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _load_image_b64(path: str) -> str | None:
    """Return base64 data-URI string for the image, or None if file missing."""
    if not os.path.exists(path):
        return None
    ext = os.path.splitext(path)[-1].lower().lstrip(".")
    mime = {"jpg": "jpeg", "jpeg": "jpeg", "png": "png", "webp": "webp"}.get(ext, "png")
    with open(path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    return f"data:image/{mime};base64,{b64}"


def _placeholder_html() -> str:
    """Avatar placeholder shown before the real photo is added."""
    return """
    <div class="placeholder">
      <div class="avatar-icon">👤</div>
      <div class="avatar-text">Add photo to assets/</div>
    </div>
    """
