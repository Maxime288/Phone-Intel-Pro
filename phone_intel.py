#!/usr/bin/env python3
"""
📱 Phone-Intel Pro
Outil d'extraction d'informations OSINT pour numéros de téléphone.
"""

import phonenumbers
from phonenumbers import geocoder, carrier, timezone
import argparse
import sys

# ──────────────────────────────────────────────────────────────
# Couleurs ANSI & Style
# ──────────────────────────────────────────────────────────────
class C:
    RESET   = "\033[0m"
    BOLD    = "\033[1m"
    RED     = "\033[38;5;196m"
    GREEN   = "\033[38;5;82m"
    YELLOW  = "\033[38;5;226m"
    BLUE    = "\033[38;5;45m"
    CYAN    = "\033[38;5;51m"
    GRAY    = "\033[38;5;244m"
    ORANGE  = "\033[38;5;208m"

BANNER = fr"""
{C.CYAN}  _____  _                      {C.ORANGE} _____       _       _  {C.RESET}
{C.CYAN} |  __ \| |                     {C.ORANGE}|_   _|     | |     | | {C.RESET}
{C.CYAN} | |__) | |__   ___  _ __   ___ {C.ORANGE}  | |  _ __ | |_ ___| | {C.RESET}
{C.CYAN} |  ___/| '_ \ / _ \| '_ \ / _ \{C.ORANGE}  | | | '_ \| __/ _ \ | {C.RESET}
{C.CYAN} | |    | | | | (_) | | | |  __/{C.ORANGE} _| |_| | | | ||  __/ | {C.RESET}
{C.CYAN} |_|    |_| |_|\___/|_| |_|\___|{C.ORANGE}|_____|_| |_|\__\___|_| {C.RESET}
{C.GRAY}          OSINT Phone Number Analyzer v1.0{C.RESET}
"""

def analyze_phone_number(number_str):
    try:
        # Parsing du numéro (format international requis : +33...)
        parsed_number = phonenumbers.parse(number_str)
        
        if not phonenumbers.is_valid_number(parsed_number):
            print(f"{C.RED}[!] Erreur : Le numéro n'est pas valide au format international.{C.RESET}")
            return

        print(f" {C.BOLD}[*]{C.RESET} Analyse terminée pour : {C.GREEN}{number_str}{C.RESET}\n")
        
        # 1. Informations de base
        print(f" {C.CYAN}🔍 INFORMATIONS GÉNÉRALES{C.RESET}")
        print(f"  {C.BOLD}Format International :{C.RESET} {phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)}")
        print(f"  {C.BOLD}Format National      :{C.RESET} {phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.NATIONAL)}")
        print(f"  {C.BOLD}Code Pays            :{C.RESET} +{parsed_number.country_code}")
        
        # 2. Géographie (OSINT)
        location = geocoder.description_for_number(parsed_number, "fr")
        print(f"\n {C.CYAN}🌍 GÉOGRAPHIE{C.RESET}")
        print(f"  {C.BOLD}Localisation         :{C.RESET} {location if location else 'Inconnue'}")
        
        # 3. Opérateur & Réseau
        operator = carrier.name_for_number(parsed_number, "fr")
        zones = timezone.time_zones_for_number(parsed_number)
        print(f"\n {C.CYAN}📡 RÉSEAU & TEMPS{C.RESET}")
        print(f"  {C.BOLD}Opérateur d'origine  :{C.RESET} {operator if operator else 'Non détecté'}")
        print(f"  {C.BOLD}Fuseaux horaires     :{C.RESET} {', '.join(zones)}")

    except Exception as e:
        print(f"{C.RED}[!] Erreur lors de l'analyse : {e}{C.RESET}")

def main():
    print(BANNER)
    parser = argparse.ArgumentParser(description="Analyseur OSINT de numéro de téléphone")
    parser.add_argument("-n", "--number", required=True, help="Numéro au format international (ex: +33612345678)")
    args = parser.parse_args()

    analyze_phone_number(args.number)
    print(f"\n{C.GRAY}Analyse terminée.{C.RESET}")

if __name__ == "__main__":
    main()
