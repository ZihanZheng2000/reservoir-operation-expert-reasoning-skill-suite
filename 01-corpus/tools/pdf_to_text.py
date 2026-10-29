"""Convert corpus PDFs to page-separated text with pypdf.

The original conversion script was not kept. This reconstruction was matched against the existing text files
(2026-10-28): pypdf PdfReader(...).pages[i].extract_text(), each page written as
'--- Page N ---\n' + text + '\n\n', UTF-8 without BOM, Windows CRLF line endings.
Check result with pypdf 6.14.2 on Python 3.13: all 55 files have identical content when whitespace is ignored;
11 are byte-identical and 44 differ only in spaces around punctuation and symbols, consistent with a different
pypdf version (the original version was not recorded).

Usage:
  python tools/pdf_to_text.py --check        compare regenerated text with development-50/text and heldout-5/text
  python tools/pdf_to_text.py --out DIR      write regenerated text to DIR/<split>/<ID>.txt
"""
import argparse, re, sys
from pathlib import Path
import pypdf

ROOT = Path(__file__).resolve().parents[1]
SPLITS = ['development-50', 'heldout-5']


def convert(pdf):
    pages = pypdf.PdfReader(pdf).pages
    return ''.join(f'--- Page {i + 1} ---\n{p.extract_text()}\n\n' for i, p in enumerate(pages))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true')
    ap.add_argument('--out')
    a = ap.parse_args()
    same = spacing = diff = 0
    for sp in SPLITS:
        for pdf in sorted((ROOT / sp / 'papers').glob('*.pdf')):
            txt = convert(pdf)
            if a.out:
                o = Path(a.out) / sp / f'{pdf.stem}.txt'
                o.parent.mkdir(parents=True, exist_ok=True)
                o.write_text(txt, encoding='utf-8', newline='\r\n')
            if a.check:
                old = (ROOT / sp / 'text' / f'{pdf.stem}.txt').read_bytes().decode('utf-8').replace('\r\n', '\n')
                if old == txt:
                    same += 1
                elif re.sub(r'\s', '', old) == re.sub(r'\s', '', txt):
                    spacing += 1
                else:
                    diff += 1
                    print(f'{pdf.stem}: content differs')
    if a.check:
        print(f'identical {same}, whitespace-only differences {spacing}, content differs {diff}')
        sys.exit(1 if diff else 0)


if __name__ == '__main__':
    main()
