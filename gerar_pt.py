#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Constrói `README.pt-BR.md` a partir do `README.md`.

A DIREÇÃO AQUI É INVERSA à dos outros repositórios, e é a norma sendo cumprida,
não quebrada: a matriz é a FONTE, e esta foi escrita em inglês. O perfil é a
primeira página que um recrutador abre, e ele nasceu em inglês de propósito —
inglês abre o mundo. O português não fica de fora: fica a um clique, declarado
num `> [!NOTE]` que o GitHub desenha como caixa.

O português aqui é DERIVADO. Editar o `README.pt-BR.md` à mão é o defeito: na
próxima correção do inglês, a edição some sem aviso.

    python3 gerar_pt.py
"""
import os
import sys

import i18n

AQUI = os.path.dirname(os.path.abspath(__file__))
FONTE = os.path.join(AQUI, "README.md")
ALVO = os.path.join(AQUI, "README.pt-BR.md")


def main():
    i18n.PARA = "pt"
    raw = open(FONTE, encoding="utf-8").read()
    tab = i18n.ler_tabela(i18n.caminho_tabela(FONTE, os.path.join(AQUI, "traducao")))
    if not tab.get("blocos"):
        print("sem tabela em traducao/ — nada a construir")
        return 1
    pt_md, pend, cercas = i18n.aplicar_md(i18n.sem_troca_idioma(raw), tab)
    if pend:
        print("REPROVADO: %d bloco(s) sem tradução." % len(pend))
        for k, en, tipo in pend[:6]:
            print("   %s  %s" % (k, en.strip()[:64].replace("\n", " ")))
        return 1
    open(ALVO, "w", encoding="utf-8").write(
        i18n.troca_idioma_md(pt_md, "pt", os.path.basename(FONTE)))
    open(FONTE, "w", encoding="utf-8").write(
        i18n.troca_idioma_md(raw, "en", os.path.basename(ALVO)))
    print("README.pt-BR.md%s" % ("  [%d cerca(s) ainda em inglês]" % cercas
                                 if cercas else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
