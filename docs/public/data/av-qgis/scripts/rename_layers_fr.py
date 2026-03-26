"""
Renommage des couches DMAV en français
======================================
Basé sur les modèles INTERLIS officiels DMAV :
  - https://models.geo.admin.ch/
  - https://www.cadastre-manual.admin.ch/fr/documentation-modele-dmav

Usage : exécuter depuis la console Python de QGIS.
"""

# fmt: off
TRANSLATIONS = {

    # ── Couverture du sol ──────────────────────────────────────────────────────
    "Bodenbedeckung":                   "CouvertureSol",
    "BBNachfuehrung":                   "MiseAJourCS",
    "Bodenbedeckungsart":               "GenreCouvertureSol",
    "Bodenbedeckung.Messpunkt":         "CouvertureSol.PointMesure",
    "Bodenbedeckung.Objektname":        "CouvertureSol.NomObjet",
    "Bodenbedeckung.Objektnummer":      "CouvertureSol.NumeroObjet",

    # ── Objets divers ─────────────────────────────────────────────────────────
    "Einzelobjekt":                     "ObjetDivers",
    "EONachfuehrung":                   "MiseAJourOD",
    "Einzelobjektart":                  "GenreObjetDivers",
    "Einzelobjekte.Flaechenelement":    "ObjetsDivers.ElementSurfacique",
    "Einzelobjekte.Linienelement":      "ObjetsDivers.ElementLineaire",
    "Einzelobjekte.Messpunkt":          "ObjetsDivers.PointMesure",
    "Einzelobjekte.Objektname":         "ObjetsDivers.NomObjet",
    "Einzelobjekte.Objektnummer":       "ObjetsDivers.NumeroObjet",
    "Einzelobjekte.Punktelement":       "ObjetsDivers.ElementPonctuel",

    # ── Immeubles ─────────────────────────────────────────────────────────────
    "Grundstueck":                              "Immeuble",
    "GSNachfuehrung":                           "MiseAJourIM",
    "Grundstuecksart":                          "GenreImmeuble",
    "Liegenschaft":                             "BienFonds",
    "Liegenschaft (Streitig)":                  "BienFonds (litigieux)",
    "SelbstaendigesDauerndesRecht":             "DroitDistinctPermanent",
    "SelbstaendigesDauerndesRecht (Streitig)":  "DroitDistinctPermanent (litigieux)",
    "Bergwerk":                                 "Mine",
    "Bergwerk (Streitig)":                      "Mine (litigieux)",
    "Grenzpunkt":                               "PointLimite",
    "Grenzpunktfunktion":                       "FonctionPointLimite",

    # ── Assiettes de servitudes ───────────────────────────────────────────────
    "Dienstbarkeitsgrenze":                     "AssietteDeServitude",
    "DiBNachfuehrung":                          "MiseAJourSV",
    "Dienstbarkeitsgrenzen.Flaechenelement":    "AssiettesDeServitudes.ElementSurfacique",
    "Dienstbarkeitsgrenzen.Linienelement":      "AssiettesDeServitudes.ElementLineaire",
    "Dienstbarkeitsgrenzen.Punktelement":       "AssiettesDeServitudes.ElementPonctuel",

    # ── Conduites ─────────────────────────────────────────────────────────────
    "Leitungsobjekt":               "ElementConduite",
    "RLNachfuehrung":               "MiseAJourCON",
    "Signal":                       "Signal",
    "Signalart":                    "GenreSignal",
    "Rohrleitungen.Flaechenelement":"Conduites.ElementSurfacique",
    "Rohrleitungen.Linienelement":  "Conduites.ElementLineaire",
    "Rohrleitungen.Messpunkt":      "Conduites.PointMesure",
    "Rohrleitungen.Punktelement":   "Conduites.ElementPonctuel",

    # ── Nomenclature ─────────────────────────────────────────────────────────
    "NKNachfuehrung":   "MiseAJourNC",
    "Flurname":         "NomLocal",
    "Ortsname":         "NomLieu",
    "Gelaendename":     "Lieudit",

    # ── Adresses de bâtiments ─────────────────────────────────────────────────
    "GANachfuehrung":       "MiseAJourAB",
    "Lokalisation":         "Localisation",
    "Lokalisationsart":     "GenreLocalisation",
    "Lokalisationsname":    "NomLocalisation",
    "Strassenstueck":       "TronconRue",
    "Gebaeudeeingang":      "EntreeBatiment",
    "Gebaeudebeschreibung": "DescriptionBatiment",
    "Gebaeudename":         "NomBatiment",
    "BenanntesGebiet":      "LieuDenomme",
    "Ortschaft":            "Localite",
    "PLZ":                  "CodePostal",
    "Nummerierungsprinzip": "PrincipeNumerotation",

    # ── Limites territoriales MO ──────────────────────────────────────────────
    "Gemeinde":                         "Commune",
    "Gemeindegrenze":                   "LimiteCommune",
    "Gemeindegrenze (Provisorisch)":    "LimiteCommune (provisoire)",
    "Gemeindegrenze (Streitig)":        "LimiteCommune (litigieux)",
    "Gemeindegrenze (Undefiniert)":     "LimiteCommune (indefinie)",
    "HHGNachfuehrung":                  "MiseAJourLT",
    "ProjGemeindegrenzabschnitt":       "PartieLimiteCommuneProjetee",
    "Bezirksgrenzabschnitt":            "PartieLimiteDistrict",
    "Kantonsgrenzabschnitt":            "PartieLimiteCanton",
    "Landesgrenze":                     "FrontiereNationale",

    # ── Territoires en mouvement permanent ────────────────────────────────────
    "DauerndeBodenverschiebung":    "TerritoireEnMouvementPermanent",
    "DBVNachfuehrung":              "MiseAJourTP",

    # ── Points fixes MO ───────────────────────────────────────────────────────
    "HFP1":                                 "PFH1",
    "HFP2":                                 "PFH2",
    "HFP3":                                 "PFH3",
    "HFP3Nachfuehrung":                     "MiseAJourPFH3",
    "LFP1":                                 "PFP1",
    "LFP2":                                 "PFP2",
    "LFP3":                                 "PFP3",
    "LFP3Nachfuehrung":                     "MiseAJourPFP3",
    "LFPArt":                               "GenrePFP",
    "FixpunkteAVKategorie2.Schutzart":      "PointsFixesMOCategorie2.GenreProtection",
    "FixpunkteAVKategorie3.Schutzart":      "PointsFixesMOCategorie3.GenreProtection",

    # ── Sous-unité registre foncier ───────────────────────────────────────────
    "DMAVSUP_UntereinheitGrundbuch_V1_0.UntereinheitGrundbuch.GrundbuchKreis":
        "DMAVSUP_SousUniteRegistreFoncier_V1_0.SousUniteRegistreFoncier.CercleRegistreFoncier",
    "DMAVSUP_UntereinheitGrundbuch_V1_1.UntereinheitGrundbuch.GrundbuchKreis":
        "DMAVSUP_SousUniteRegistreFoncier_V1_1.SousUniteRegistreFoncier.CercleRegistreFoncier",

    # ── Modèles avec préfixe complet ──────────────────────────────────────────
    "DMAV_HoheitsgrenzenAV_V1_0.HoheitsgrenzenAV.Gueltigkeit":
        "DMAV_LimitesTerritorialesMO_V1_0.LimitesTerritorialesMO.Validite",
    "DMAV_Toleranzstufen_V1_0.Toleranzstufen.Toleranzstufe":
        "DMAV_NiveauxTolerance_V1_0.NiveauxTolerance.NiveauTolerance",
    "HoheitsgrenzenLV.Gueltigkeit":         "LimitesTerritorialesLV.Validite",

    # ── Graphique / affichage ─────────────────────────────────────────────────
    "Symbolposition":               "PositionSymbole",
    "Textposition":                 "PositionTexte",
    "Textposition (Hinweisstrich)": "PositionTexte (ligne de reference)",
    "Flaechenelement (Sichtbar)":   "ElementSurfacique (visible)",
    "Schriftgroesse":               "TaillePolice",
    "DarstellungIn":                "RepresentationDans",
    "ImModul":                      "DansModule",

    # ── Mise à jour génériques ────────────────────────────────────────────────
    "TSNachfuehrung":   "MiseAJourTS",
    "PNF":              "CasMiseAJourProjet",

    # ── Qualité / métadonnées ─────────────────────────────────────────────────
    "Qualitaetsstandard":   "StandardQualite",
    "Objektstatus":         "StatutObjet",
    "Mutationsart":         "GenreMutation",
    "Herkunft":             "Provenance",
    "Versicherungsart":     "GenreAbornement",
    "Medium":               "Milieu",
    "Sprache":              "Langue",

    # ── Types du catalogue DMAVTYM ────────────────────────────────────────────
    "Actual_Status":                    "Statut_actuel",
    "Attribute_name":                   "Nom_attribut",
    "Boolean_type":                     "Type_booleen",
    "Bound_validity_type":              "Type_validite_limite",
    "Classe_name":                      "Nom_classe",
    "Completeness_type":                "Type_completude",
    "Control_point_Category":           "Categorie_point_controle",
    "Cut_out_surface_type":             "Type_surface_decoupee",
    "Fluid_type":                       "Type_fluide",
    "LCS_type":                         "Type_LCS",
    "Local_names_type":                 "Type_noms_locaux",
    "Mark_type":                        "Type_borne",
    "Other_territorial_bound_type":     "Autre_type_limite_territoriale",
    "QualityStandard_type":             "Type_standard_qualite",
    "RealEstate_type":                  "Type_immeuble",
    "Reliability_type":                 "Type_fiabilite",
    "SO_type":                          "Type_OD",
    "Terrain_edge_type":                "Type_bord_terrain",
    "Territorial_bound_Line_type":      "Type_ligne_limite_territoriale",
    "Text_type":                        "Type_texte",
    "Topic_name":                       "Nom_topic",
    "Validity_type":                    "Type_validite",
    "HALIGNMENT":                       "HALIGNMENT",
    "VALIGNMENT":                       "VALIGNMENT",
}
# fmt: on


def rename_layers(translations: dict) -> None:
    """Renomme les couches du projet QGIS courant selon le dictionnaire fourni."""
    # QgsProject est injecté par l'environnement QGIS (console Python ou plugin)
    project = QgsProject.instance()  # noqa: F821
    renamed = []
    not_found = []

    for layer in project.mapLayers().values():
        original_name = layer.name()
        if original_name in translations:
            new_name = translations[original_name]
            layer.setName(new_name)
            renamed.append((original_name, new_name))
        else:
            not_found.append(original_name)

    # ── Rapport ───────────────────────────────────────────────────────────────
    print(f"\n{'=' * 55}")
    print(f"  {len(renamed)} couche(s) renommée(s)")
    print(f"{'=' * 55}")
    for orig, new in renamed:
        print(f"  ✓  {orig!r:50s} → {new!r}")

    if not_found:
        print(f"\n{'─' * 55}")
        print(f"  {len(not_found)} couche(s) sans traduction")
        print(f"{'─' * 55}")
        for name in not_found:
            print(f"  ?  {name!r}")

    print()


rename_layers(TRANSLATIONS)
