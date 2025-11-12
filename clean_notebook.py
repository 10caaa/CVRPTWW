"""
Script to clean notebook outputs and make them more professional
"""

import json
import re

def clean_output_text(text):
    """Remove emojis and clean output text"""
    # Remove emojis
    emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\u2600-\u26FF"          # Miscellaneous Symbols
        u"\u2700-\u27BF"          # Dingbats
        "]+", flags=re.UNICODE)
    
    text = emoji_pattern.sub('', text)
    
    # Replace specific patterns
    replacements = {
        '✅': '',
        '🔧': '',
        '📊': '',
        '🚛': '',
        '📈': '',
        '⚠️': 'Warning:',
        '❌': 'Error:',
        'PHASE 1 TERMINÉE': 'Phase 1 completed',
        'PHASE 2 TERMINÉE': 'Phase 2 completed',
        'PHASE 3 TERMINÉE': 'Phase 3 completed',
        'PHASE 4 TERMINÉE': 'Phase 4 completed',
        'PHASE 5 TERMINÉE': 'Phase 5 completed',
        'PHASE 6 TERMINÉE': 'Phase 6 completed',
        'Imports OK': 'Imports loaded successfully',
        'Fonctions de parsing OK': 'Data parsing functions loaded',
        'Classes .* OK': 'Classes loaded',
        '=== * 60': '-' * 60,
        '=== * 70': '-' * 70,
    }
    
    for old, new in replacements.items():
        text = text.replace(old, new)
    
    return text.strip()

# This script demonstrates the pattern but actual notebook editing is done through edit_notebook_file
print("Cleaning patterns defined")
