class tts(object):

# Original English voices
VOICES = [
    "nova", "alloy", "ash", "coral", "echo",
    "fable", "onyx", "sage", "shimmer"
]

# Indian languages mapping for ttsmp3.com API
INDIAN_LANGUAGES = {
    "malayalam": "Malayalam",
    "hindi": "Hindi", 
    "tamil": "Tamil",
    "bengali": "Bengali",
    "telugu": "Telugu",
    "marathi": "Marathi",
    "gujarati": "Gujarati",
    "kannada": "Kannada",
    "punjabi": "Punjabi",
    "urdu": "Urdu",
    "english": "coral",  # Default English voice
}

# Language detection patterns using Unicode ranges
LANGUAGE_PATTERNS = {
    "malayalam": re.compile(r'[\u0d00-\u0d7f]'),  # Malayalam
    "hindi": re.compile(r'[\u0900-\u097f]'),      # Devanagari (Hindi)
    "tamil": re.compile(r'[\u0b80-\u0bff]'),      # Tamil
    "bengali": re.compile(r'[\u0980-\u09ff]'),    # Bengali
    "telugu": re.compile(r'[\u0c00-\u0c7f]'),     # Telugu
    "gujarati": re.compile(r'[\u0a80-\u0aff]'),   # Gujarati
    "kannada": re.compile(r'[\u0c80-\u0cff]'),    # Kannada
    "marathi": re.compile(r'[\u0900-\u097f]'),    # Devanagari (Marathi)
    "punjabi": re.compile(r'[\u0a00-\u0a7f]'),    # Gurmukhi (Punjabi)
    "urdu": re.compile(r'[\u0600-\u06ff]'),       # Arabic script (Urdu)
}
