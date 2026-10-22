#!/usr/bin/env python3
"""Build en/index.html (areizos.com/en/) from index.html.

The English page is the same page, opened in English, with English
preview tags (title, description, share image). Edit index.html only;
this script (and the GitHub Action that runs it) keeps en/ in sync.
Run: python3 scripts/build-en.py
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

SWAPS = [
    ('<!doctype html><html lang="es">',
     '<!doctype html><!-- Generated from /index.html by scripts/build-en.py. Edit index.html, not this file. --><html lang="en">'),
    ('<meta name="description" content="Alexandros Reïzos: diseño web, optimización y estrategia de marketing digital para tu negocio. Más de quince años de experiencia.">',
     '<meta name="description" content="Alexandros Reïzos: web design, optimisation and digital marketing strategy for your business. Over fifteen years of experience.">'),
    ('<link rel="canonical" href="https://areizos.com/">',
     '<link rel="canonical" href="https://areizos.com/en/">'),
    ('<meta property="og:url" content="https://areizos.com/">',
     '<meta property="og:url" content="https://areizos.com/en/">'),
    ('<meta property="og:locale" content="es_ES"><meta property="og:locale:alternate" content="en_GB">',
     '<meta property="og:locale" content="en_GB"><meta property="og:locale:alternate" content="es_ES">'),
    ('<meta property="og:title" content="areïzos · Tu web y tus herramientas, en buenas manos">',
     '<meta property="og:title" content="areïzos · Your website and your tools, in good hands">'),
    ('<meta property="og:description" content="Diseño web, optimización y estrategia de marketing digital para tu negocio.">',
     '<meta property="og:description" content="Web design, optimisation and digital marketing strategy for your business.">'),
    ('<meta property="og:image" content="https://areizos.com/og.png">',
     '<meta property="og:image" content="https://areizos.com/og-en.png">'),
    ('<meta property="og:image:alt" content="areïzos · Tu web y tus herramientas, en buenas manos.">',
     '<meta property="og:image:alt" content="areïzos · Your website and your tools, in good hands.">'),
    ('<meta name="twitter:image" content="https://areizos.com/og.png">',
     '<meta name="twitter:image" content="https://areizos.com/og-en.png">'),
    ('<meta name="twitter:title" content="areïzos · Tu web y tus herramientas, en buenas manos">',
     '<meta name="twitter:title" content="areïzos · Your website and your tools, in good hands">'),
    ('<meta name="twitter:description" content="Diseño web, optimización y estrategia de marketing digital para tu negocio.">',
     '<meta name="twitter:description" content="Web design, optimisation and digital marketing strategy for your business.">'),
    ('<title>Alexandros Reïzos · Diseño web, optimización y marketing digital | areïzos</title>',
     '<title>Alexandros Reïzos · Web design, optimisation and digital marketing | areïzos</title>'),
    ('href="https://pleko.es/blog" data-href-es=',
     'href="https://pleko.es/en/blog" data-href-es='),
    ("setLang('es');", "setLang('en');"),
]

src = (ROOT / 'index.html').read_text(encoding='utf-8')
out = src
for old, new in SWAPS:
    n = out.count(old)
    if n != 1:
        raise SystemExit(f'build-en: expected 1 match, found {n}: {old[:80]}')
    out = out.replace(old, new)
(ROOT / 'en').mkdir(exist_ok=True)
(ROOT / 'en' / 'index.html').write_text(out, encoding='utf-8')
print('en/index.html built')
